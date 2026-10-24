FROM node:22.23.4-alpine AS web
# Refresh the system certificate store when rebuilding this image.
RUN apk add --no-cache --upgrade ca-certificates && update-ca-certificates
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build
FROM nginx:1.27-alpine
# Refresh the system certificate store when rebuilding this image.
RUN apk add --no-cache --upgrade ca-certificates && update-ca-certificates
COPY --from=web /app/out /usr/share/nginx/html
EXPOSE 80
