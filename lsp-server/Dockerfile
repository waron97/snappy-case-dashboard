FROM node:20-alpine
RUN npm install -g basedpyright
WORKDIR /server
COPY package.json .
RUN npm install
COPY server.js .
COPY workspace/ /workspace/

# Patch typeshed: copy only stdlib/ from bundled typeshed, append custom builtins
RUN BUILTIN=$(find /usr/local/lib/node_modules/basedpyright -name "builtins.pyi" -path "*/stdlib/*" | head -1) && \
    STDLIB=$(dirname "$BUILTIN") && \
    mkdir -p /workspace/typeshed && \
    cp -r "$STDLIB" /workspace/typeshed/stdlib && \
    cat /workspace/typings/builtins.pyi >> /workspace/typeshed/stdlib/builtins.pyi && \
    rm -rf /workspace/typings

EXPOSE 3000
CMD ["node", "server.js"]
