FROM python:3.7-alpine

COPY entrypoint.sh /
COPY requirements.txt /
ADD src /app

RUN apk update && \
    pip install -r /requirements.txt && \
    rm /requirements.txt && \
    rm -rf /var/cache/apk/*

WORKDIR /app

ENTRYPOINT ["sh", "/entrypoint.sh"]