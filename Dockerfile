FROM python:3.8

ENV CACHEBUSTER=true
ENV PYTHONUNBUFFERED=1
ENV APP_DIR=/app

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

RUN pip install -r requirements.txt

ENTRYPOINT ${APP_DIR}/docker-entrypoint-dev.sh