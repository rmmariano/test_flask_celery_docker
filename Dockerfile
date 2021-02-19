FROM python:3.8.5-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
