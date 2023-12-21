# FND
Flask-Nginx-Docker template based on jinja2 and gunicorn

---
## Requirements
- Docker
- Python  (optional for local development, see below)

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

if you want to make changes to the flask app you have to rebuild the container with the following command:

```bash
docker-compose up -d --build flask
```

---
## Running the app with Flask
To start the app, run the following command:

navigate to the flask directory:
```bash
cd flask
```

install the requirements:
```bash
pip3 install -r requirements.txt
```

run the app:
```bash
python3 wsgi.py
```
---
## Picture of app
![image](https://github.com/karlusrex/FND/assets/90254802/875292ea-7214-46df-b1b4-833c452d4463)
