FROM alpine:3.8

ENV TERRAFORM_VERSION=0.11.11

RUN apk update && \
    apk add curl jq python bash ca-certificates git openssl unzip wget && \
    cd /tmp && \
    wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/* && \
    rm -rf /var/tmp/*

ADD terraform /terraform
COPY entrypoint.sh /

WORKDIR /terraform

ENTRYPOINT ["sh", "/entrypoint.sh"]