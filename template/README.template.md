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

```yaml
${code/s3.yaml}
```

2.	Inicie seu ambiente da AWS no AWS Academy

3.	Na barra superior procure por CloudFormation e selecione o serviço

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img7.png" />

4.	Clique em  <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img8.png" />

5.	Selecione a opção <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img9.png" />

6.	Na tela de criação da Pilha:

    a.	Selecione a opção <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img10.png" />

    b.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img11.png" />

    c.	 Escolha o arquivo `s3-notification.yaml` que acabou de criar

    d.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img12.png" /> Se receber uma mensagem de erro, verifique se salvou o arquivo no VSCode

    e.	 `Stack Name`: `dataops-lab2`

    f.	 Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img13.png" /> nas próximas duas telas

    g.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img14.png" />

7.	Será mostrada a tela de execução da stack. Espere até o status mudar para <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img15.png" />

a.	Atualize de vez em quando clicando em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img16.png" /> no canto superior direito

8.	Quando a stack terminar a execução, acesse o S3 para verificar o bucket criado



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
