# test_flask_celery_docker

Build Docker image:

```
$ docker build -t test_flask_celery_docker -f Dockerfile . --no-cache
```

Run apps:

```
$ docker-compose -f docker-compose.yml up
```

This repository has been created based on: https://blog.carbonteq.com/python-flask-celery-docker/
