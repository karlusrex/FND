FROM node:16 as build

WORKDIR /usr/src/app/web

COPY package.json ./
COPY pnpm-lock.yaml ./
COPY . ./
RUN npm install -g pnpm
RUN pnpm install --shamefully-hoist --force
RUN pnpm add vite --force
