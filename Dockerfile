FROM python:3.8.5-slim-buster

WORKDIR /app

ADD requirements.txt .
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1

CMD ["flask", "run", "--host=0.0.0.0"]
