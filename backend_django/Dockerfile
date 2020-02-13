FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD . /app

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    git bash make && \
    pip install -r requirements.txt
EXPOSE 8000

# CMD uvicorn feature_flag_backend.asgi:application
CMD python manage.py runserver 0.0.0.0:8000