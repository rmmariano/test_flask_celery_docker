# test_flask_celery_docker

Repository to test Flask + Celery + RabbitMQ + Docker.


## Instructions

Build Docker image:

```
$ docker build -t test_flask_celery_docker -f Dockerfile . --no-cache
```

Run apps:

```
$ docker-compose -f docker-compose.yml up
```

You can execute the task with cURL:

```
$ curl "localhost:5000/add?first_num=3&second_num=2"
```

This repository has been created based on: https://blog.carbonteq.com/python-flask-celery-docker/
