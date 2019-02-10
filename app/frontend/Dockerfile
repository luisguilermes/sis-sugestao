FROM nginx:1.15.8-alpine



COPY default.conf /etc/nginx/conf.d/default.conf
ADD ./template /usr/share/nginx/html
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]