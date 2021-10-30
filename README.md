# CloudFormation: Buceket S3 + notificação SNS

## DataOps - Lab2 - CloudFormation

### Objetivos

*  Utilizar CloudFormation para provisionar recursos na AWS
*  Criar um bucket S3 para armazenar arquivos
*  Criar um Tópico SNS para enviar mensagens
*  Criar uma assinatura de e-mail para o tópico SNS
*  Configurar S3 para enviar uma mensagem para SNS quando incluir ou excluir ar-quivo

### Arquitetura da solução

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/lab2.png" height='330'/>

### Criar Template do CloudFormation

1.  Abra o VSCode
2.  Selecione o menu `File --> Open Folder`
3.  Escolha uma pasta do computador para manter seus projetos e códigos

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img1.png" />

4.  Nas opções da lateral esquerda, clique no nome da pasta que selecionou

    a. No exemplo, foi selecionada a pasta `CODES`

5.  Clique no segundo ícone <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img2.png" />  para adicionar uma nova pasta
6.  Coloque o nome `lab2` e aperte `Enter`

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img3.png"/>

7.  Com a pasta selecionada, clique no primeiro ícone [ <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img4.png" /> ] para adicionar um novo arquivo
8.  Coloque o nome `s3-notification.yaml` e aperte `Enter`. O Arquivo será aberto automaticamente no editor a direita

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img5.png" />

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img6.png" />

### Provisionar Bucket S3

1.  No arquivo `s3-notification.yaml` coloque o seguinte código para configurar o template do CloudFormation e provisionar um Bucket S3. O Código está no arquivo `s3.yaml` neste repositório.

    a. Troque `nomesobrenome` pelo seu nome e sobrenome.

    b. Não esqueça de salvar o arquivo.

<div id="code-element"></div>

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>

      axios({method: 'get',  url: 'https://raw.github.com/fesousa/dataops-lab2/master/s3.yaml' }).then(function (response) {document.getElementById("code-element").innerHTML = response.data;});

</script>




---

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
