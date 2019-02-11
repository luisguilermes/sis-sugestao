FROM nginx:1.15.8-alpine

RUN apk update && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

COPY default.conf /etc/nginx/conf.d/default.conf
ADD ./template /usr/share/nginx/html
COPY entrypoint.sh /entrypoint.sh
COPY wait-for /wait-for

ENTRYPOINT ["/entrypoint.sh"]

#CMD ["nginx", "-g", "daemon off;"]