FROM node:16 as build

WORKDIR /usr/src/app/web

COPY . ./
RUN npm install -g pnpm
RUN pnpm install --shamefully-hoist --force
RUN pnpm run build

FROM nginx:latest
COPY --from=build /usr/src/app/web/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/
RUN apt-get update && apt-get install -y

