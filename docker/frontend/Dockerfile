FROM node:lts-alpine

WORKDIR /data/

COPY ./src/frontend/package.json /data/

RUN npm install
ENV PATH=/data/node_modules/.bin:$PATH

COPY . /data/app/
WORKDIR /data/app/

CMD ["npm", "run", "serve"]
