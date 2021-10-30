# CloudFormation: Buceket S3 + notificação SNS

## DataOps - Lab2 - CloudFormation

### Objetivos

* Utilizar CloudFormation para provisionar recursos na AWS
* Criar um bucket S3 para armazenar arquivos
* Criar um Tópico SNS para enviar mensagens
* Criar uma assinatura de e-mail para o tópico SNS
* Configurar S3 para enviar uma mensagem para SNS quando incluir ou excluir ar-quivo

### Arquitetura da solução

![Diagrama  lab 2](https://raw.github.com/fesousa/dataops-lab2/master/images/lab2.png){ width=50% }



## Implantação

### Configuração de acesso à AWS

```console
aws configure set aws_access_key_id "YOUR_AWS_ACCESS_KEY_ID"
aws configure set aws_secret_access_key "YOUR_AWS_SECRET_ACCESS_KEY"
aws configure set region "YOUR_REGION"
#Se estiver utilizando SESSION TOKEN
aws configure set aws_session_token "YOUR_AWS_SESSION_TOKEN"`
```

### Implantação do template CloudFormation

Troque `nomesobrenome` por seu nomesobrenome, para criar um nome único para o bucket.

Troque `email@email.com` ppelo e-mail que vai receber a notificação SNS.

```console
aws cloudformation deploy --template-file s3-notification.yaml --stack-name s3-notification-stack --parameter-overrides SufixoBucket=nomedobrenome EmailNotificacao=email@email.com
```

### Atualização template CloudFormation

Troque `nomesobrenome` por seu nomesobrenome, para criar um nome único para o bucket.

Troque `email@email.com` ppelo e-mail que vai receber a notificação SNS.

```console
aws cloudformation deploy --template-file s3-notification-update.yaml --stack-name s3-notification-stack --parameter-overrides SufixoBucket=nomesobrenome EmailNotificacao=email@email.com`
```
