# Stack DevOps - API Rest para captura de sugestões

## Dependências do Projeto

- Docker Engine release 18.06.0+
- Docker Compose 1.23.2+
- Conta AWS

## Para Iniciar o Projeto
1 - Criar Bucket S3 para armazenar o estado da infraestrutura gerada pelo Terraform.

    Ex.: terraform-state-xptodaeigha


2 - Criar Policy AWS IAM com a permissão abaixo, substituindo {{NOME_BUCKET}} pelo bucket criado anteriormente:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::{{NOME_BUCKET}}",
            "Action": "s3:ListBucket"
        },
        {
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::{{NOME_BUCKET}}/state/terraform.tfstate",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "sqs:*",
            "Resource": "*"
        }
    ]
}
```

3 - Criar Usuário AWS IAM e atachar a politica criada anteriormente ao usuário.
    
    OBS: Atentar para salvar AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY

4 - Exportar variáveis de ambiente necessárias para execução do projeto atentando para as devidas subistituições.

    export AWS_ACCESS_KEY_ID="{{AWS_SECRET_ACCESS_KEY}"
    export AWS_SECRET_ACCESS_KEY="{{AWS_SECRET_ACCESS_KEY}}"
    export S3_BUCKET_NAME="{{CRIADO_NO_ITEM_1}}"
    export QUEUE_NAME="{{DEFINIR_UM_NOME_PARA_A_QUEUE_SQS}}"

     
5 - A partir do diretório do projeto, executar:

```
docker-compose -f docker-compose.yml up -d --build
```

6 - Fim da execução 
    
    A stack estará disponível quando o Frontend  http://<IP-HOST-DOCKER> estiver acessível.

## URLs do Projeto

- Form Sugestões: http://<IP-HOST-DOCKER>
- Backend: http://<IP-HOST-DOCKER>/api/sugestao
- http://<IP-HOST-DOCKER>/api/sugestao/healthcheck

## Detalhes Técnicos do Projeto

### Service - terraform

- Responsável por provisionar o ambiente AWS e inserir informações dos serviços no ETCD(Service Discovery). 

    - O Build(Dockerfile) do container instala o terraform na image Base alpine:3.8
    - O entrypoint do container provisiona os recursos AWS baseado nas variáveis de ambiente. 

### Service - Mongo

- Banco NoSQL reponsável por persistir as sugestões provenientes do SQS.
    
    - Utilizado imagem oficial do serviço sem autenticação.

### Service - etcd

- Banco chave-valor, atuando como um Service Dicovery para aplicações da Stack.
    
    - Utilizado imagem oficial do serviço sem autenticação.  

### Service - api-rest

- A aplicação foi construída utilizando a linguagem python e o microframework flask.
- A aplicação trabalha recebendo o verbo HTTP POST, para cadastro das sugestões no SQS.
- A aplicação possui um healthcheck trabalhando com o verbo GET na URI http://<IP-HOST-DOCKER>/api/sugestao/healthcheck   

### Service - worker

- A aplicação foi construída utilizando a linguagem python.
- A aplicação trabalha como um scheduler conectando ao SQS, processando e armazenando no Mongo.


### Service - frontend

- Foi construido utilizando o servidor WEB NGINX, atuando como um servidor de conteúdo estático que entrega um Form HTML
e proxy reverso para o serviço api-rest.
- Há um script wait-for que aguarda os serviçõs de backend estarem disponíveis para disponibilizar 
a "aplicação" frontend.


