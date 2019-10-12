# dockerized-flask-hello-world
A simple example of a dockerized flask application.

```
docker build -t docker-flask:latest .
docker run --name flaskapp -p8000:8000 docker-flask:latest
```
