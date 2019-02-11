#!/bin/sh

if [ -z "$SERVICE_DISCOVERY" ]
then
        echo "Não há variável de ambiente para 'SERVICE_DISCOVERY'. É Requerido!"
        exit
fi

gunicorn --bind 0.0.0.0:5000 manage:app

