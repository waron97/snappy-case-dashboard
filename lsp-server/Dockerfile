FROM node:20-alpine
RUN npm install -g basedpyright
WORKDIR /server
COPY package.json .
RUN npm install
COPY server.js .
COPY workspace/ /workspace/

EXPOSE 3000
CMD ["node", "server.js"]
