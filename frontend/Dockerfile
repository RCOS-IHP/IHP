FROM node:alpine as builder
WORKDIR /app
COPY . /app/
RUN npm ci
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /var/www/html/
COPY ./ihp.conf /etc/nginx/conf.d/default.conf
