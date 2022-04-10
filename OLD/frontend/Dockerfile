FROM node:lts-alpine

WORKDIR /app

RUN npm install -g npm
RUN npm install -g @vue/cli@4.5.15

COPY package.json .
COPY package-lock.json .

RUN npm install

CMD ["npm", "run", "serve"]

