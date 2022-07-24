FROM node:lts-alpine

WORKDIR /app

RUN npm install -g npm
RUN npm install -g @vue/cli

COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "serve"]
