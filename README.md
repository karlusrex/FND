# FND
Flask-Nginx-Docker template for svelte ts and vite using pnpm

---
## Requirements
- Docker
- Python (Optional for local development)
- pnpm (Optional for local development)

---
## Running the app with Docker 
To start the container, run the following command:

```bash
docker-compose up -d
```

To stop the container, run the following command:

```bash
docker-compose down
```

if you want to make changes to the web or flask app you have to rebuild the container with the following command:

```bash
docker-compose up -d --build web
```
```bash
docker-compose up -d --build flask
```
---
## Running the web (svelte) app
navigate to the web app:

```bash
cd web
```

run the svelte app by:

```bash
pnpm install
pnpm run dev
```

the svelte application is now running on `localhost:5173` with hot reloading enabled

---
## Picture of app
![image](https://github.com/karlusrex/FND/assets/90254802/af0facc4-2e31-4797-80b8-2bc1c6a28f76)

