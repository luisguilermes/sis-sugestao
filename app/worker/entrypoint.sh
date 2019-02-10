#!/bin/sh

if [ -z "$SERVICE_DISCOVERY" ]
then
        echo "Não há variável de ambiente para 'SERVICE_DISCOVERY'. É Requerido!"
        exit
fi

python /app/run.py

