const { WebSocketServer } = require("ws");
const { spawn } = require("child_process");

const wss = new WebSocketServer({ port: 3000 });

wss.on("connection", (ws) => {
  const proc = spawn("basedpyright-langserver", ["--stdio", "--verbose"], {
    cwd: "/workspace",
    stdio: ["pipe", "pipe", "pipe"],
  });

  // WebSocket message (raw JSON) → LSP-framed stdin
  ws.on("message", (data) => {
    const message = data.toString();
    const header = `Content-Length: ${Buffer.byteLength(message, "utf8")}\r\n\r\n`;
    proc.stdin.write(header + message);
  });

  // LSP-framed stdout → WebSocket (raw JSON)
  // Keep buffer as bytes: Content-Length is in bytes, not characters.
  // Mixing chunk.toString() with byte-count slicing corrupts multi-byte UTF-8.
  let buffer = Buffer.alloc(0);
  proc.stdout.on("data", (chunk) => {
    buffer = Buffer.concat([buffer, chunk]);
    while (true) {
      const headerEnd = buffer.indexOf("\r\n\r\n");
      if (headerEnd === -1) break;
      const header = buffer.slice(0, headerEnd).toString("utf8");
      const match = header.match(/Content-Length:\s*(\d+)/i);
      if (!match) {
        buffer = buffer.slice(headerEnd + 4);
        continue;
      }
      const length = parseInt(match[1], 10);
      const bodyStart = headerEnd + 4;
      if (buffer.length < bodyStart + length) break;
      const body = buffer.slice(bodyStart, bodyStart + length).toString("utf8");
      buffer = buffer.slice(bodyStart + length);

      if (ws.readyState === ws.OPEN) {
        ws.send(body);
      }
    }
  });

  proc.stderr.on("data", (chunk) => {
    console.error("[basedpyright stderr]", chunk.toString());
  });

  const cleanup = () => {
    try {
      proc.kill();
    } catch (_) {}
  };

  ws.on("close", cleanup);
  ws.on("error", cleanup);
  proc.on("exit", () => {
    if (ws.readyState === ws.OPEN) ws.close();
  });
});

console.log("LSP WebSocket server listening on port 3000");
