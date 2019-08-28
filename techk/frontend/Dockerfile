FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /frontend
COPY package*.json ./
RUN npm install
RUN npm install bootstrap-vue
RUN npm install axios
COPY . .
RUN npm run build
