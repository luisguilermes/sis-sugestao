#!/bin/sh

set -e


if [ -z "$AWS_ACCESS_KEY_ID" or -z "$AWS_SECRET_ACCESS_KEY" ]
then
        echo "Não há variável de ambiente definida para 'AWS_ACCESS_KEY_ID' ou 'AWS_SECRET_ACCESS_KEY'. É Requerido!"
        exit 1
fi

if [ -z "$S3_BUCKET_NAME" ]
then
        echo "Não há variável de ambiente definida para 'S3_BUCKET_NAME'. É Requerido!"
        exit 1
fi

if [ -z "$QUEUE_NAME" ]
then
        echo "Não há variável de ambiente definida para 'QUEUE_NAME'. É Requerido!"
        exit 1
fi

sed -i "s|{{S3_BUCKET_NAME}}|$S3_BUCKET_NAME|;s|{{QUEUE_NAME}}|$QUEUE_NAME|" /terraform/main.tf

cd /terraform
/usr/bin/terraform init
/usr/bin/terraform apply -auto-approve

if [ $? -eq 0 ]
then
    curl -s http://etcd:2379/v2/keys/sqs_id -XPUT -d value="$(terraform output sqs_id)"
    curl -s http://etcd:2379/v2/keys/sqs_name -XPUT -d value="$(terraform output sqs_name)"
    curl -s http://etcd:2379/v2/keys/aws_access_key_id -XPUT --data-urlencode value="$AWS_ACCESS_KEY_ID"
    curl -s http://etcd:2379/v2/keys/aws_secret_access_key -XPUT --data-urlencode value="$AWS_SECRET_ACCESS_KEY"
else
    exit 1
fi
