# Celery and Flask Learning Repository

This repository contains my code and resources as I work through the course "The Definitive Guide to Celery and Flask." The primary goal is to learn how to integrate Celery, an asynchronous task queue, with Flask, a Python-based web framework, for managing background tasks and improving application performance.

## Setup

There's a `.env` directory in the project root, and it should have a file called `.dev-sample` that contains the following:

```
FLASK_DEBUG=1
FLASK_CONFIG=development
DATABASE_URL=postgresql://flask_celery:flask_celery@db/flask_celery
SECRET_KEY=my_precious
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
SOCKETIO_MESSAGE_QUEUE=redis://redis:6379/0
```

## Commands

`$ docker-compose up -d --build`

Build the project and run the services.

`$ docker-compose logs -f`

Look at the logs for the services.

`$ curl -X POST http://localhost:5010/users/webhook_test/ -d {'data':'ping'}`

Test an endpoint with data from the CLI.

`$ docker-compose exec celery_worker bash`

Get a shell in a running container.

## About the Course

I didn't write the course - I just found it online and found it useful. The book covers the basics of Celery and producer/consumer-based task queues in general. By the end of the book, the reader is expected to be able to:

- Explain why they may want to use a task queue like Celery
- Describe the basic producer/consumer model and how it relates to Celery
- Implement Celery in a Flask application to handle background tasks

## Course

[The Definitive Guide to Celery and Flask](https://testdriven.io/courses/flask-celery/intro/).
