FROM node:lts-alpine
ARG MOCKED_VALUES
ENV VUE_APP_USE_MOCKED_VALUES=$MOCKED_VALUES
ENV VUE_APP_DOCKERIZED=true
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080

CMD [ "http-server", "dist" ]