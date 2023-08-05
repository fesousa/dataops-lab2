# CloudFormation: Bucket S3 + notificação SNS

## DataOps - Lab2 - CloudFormation

### Objetivos

*  Utilizar CloudFormation para provisionar recursos na AWS
*  Criar um bucket S3 para armazenar arquivos
*  Criar um Tópico SNS para enviar mensagens
*  Criar uma assinatura de e-mail para o tópico SNS
*  Configurar S3 para enviar uma mensagem para SNS quando incluir ou excluir ar-quivo

### Arquitetura da solução

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/lab2.png" width='100%'/>

### Criar Ambiente de Desenvolvimento no Cloud9

1. No ambiente da AWS, procure e abra o serviço Cloud9
2. Clique no botão <img height="25" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img29.png" />  
3. No campo `Nome` escreva `ambiente-dev-dataops`
3. Em `Tempo limite`, coloque `4 horas`
4. Em `Configurações de rede` selecione a opção `Secure Shell (SSH)` 

<img height="80" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img31.png" />  

5. Clique em <img height="25" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img30.png" />  . O resultado deve ser o seguinte:

<img width="100%" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img32.png" />  

5. Na tela da imagem anterior selecione o ambiente criado e clique em  <img height="25" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img34.png" />. O ambiente de desenvolvimento do Cloud9 será aberto em uma nova aba

<img width="100%" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img33.png" />  

### Criar Template do CloudFormation

1.  Abra o Cloud9, se ainda não estiver aberto
2.  Na seção do lado esquerdo do ambiente, clique com o botão direito do mouse na pasta principal do ambiente (`ambiente-dev-dataops`) e depois em `New Folder`
3. Coloque o nome `lab2` na pasta

<img height="150" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img1.1.png" />

4.  Adicione um novo arquivo clicando em <img height="25" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img2.1.png" /> e depois em `New File`

5. Salve o arquivo com o nome `s3-notification.yaml` na pasta `lab2` apertando as teclas `ctrl` e `s` juntas. Ao abrir a janela de salvar, lembre-se de selecionar a pasta `lab2`

<img height="170" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img5.1.png" />


### Provisionar Bucket S3

1.  No arquivo `s3-notification.yaml` coloque o seguinte código para configurar o template do CloudFormation e provisionar um Bucket S3. O Código está no arquivo `s3.yaml` neste repositório.

    a. Troque `nomesobrenome` pelo seu nome e sobrenome.

    b. Não esqueça de salvar o arquivo.

```yaml
# Versão do template - não alterar
AWSTemplateFormatVersion: "2010-09-09"

# Descrição que será utilizada na stack
Description:
  Criacao de bucket S3 e disparo de mensagem SNS

# Parâmetros
Parameters:
  SufixoBucket:
    Type: String
    Default: nomesobrenome

# Recursos que serão provisionados
Resources:  
  # Provisionar um Bucket S3 privado
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: Private
      BucketName: !Sub dataops-deploy-${SufixoBucket}-${AWS::AccountId}-${AWS::Region}

#Saídas mostradas no CloudFormation
Outputs:
  ArnBucket:
    Description: Nome do bucket
    Value: 
      !Join
        - ""
        - - "arn:aws:s3:::"
          - !Ref 'S3Bucket'
  NomeBucket:
    Description: Nome do bucket
    Value: !Ref 'S3Bucket'
```

2.	Inicie seu ambiente da AWS no AWS Academy

3.	Na barra superior procure por CloudFormation e selecione o serviço

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img7.png" width='100%' />

4.	Clique em  <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img8.png" />

5.	Selecione a opção <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img9.png" />

6.	Na tela de criação da Pilha:

    a.	Selecione a opção <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img10.png" />

    b.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img11.png" />

    c.	 Escolha o arquivo `s3.yaml` que acabou de criar

    d.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img12.png" />. Se receber uma mensagem de erro, verifique se salvou o arquivo no VSCode

    e.	 `Nome da pilha`: `dataops-lab2`

    f. Na seção `Parâmetros` coloque o seu nome e sobrenome no campo `SufixoBucket`, onde está com o valor `nomesobrenome`. Por exemplo: `fernandosousa`. Este parâmetro será utilizado no nome do bucket

    g.	 Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img13.png" /> nas próximas duas telas

    h.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img14.png" height='25' />

7.	Será mostrada a tela de execução da stack. Espere até o status mudar para <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img15.png" />

    a.	Atualize de vez em quando clicando em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img16.png" /> no canto superior direito

8.	Quando a stack terminar a execução, acesse o S3 para verificar o bucket criado

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img17.png" width='100%' />

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img18.png" width='100%' />


### Atualização do template e dos recursos

1.	Volte para o VSCode e adicione no arquivo `s3-notification.yaml` o provisionamento do tópico SNS, assinatura do tópico e política do tópico SNS dentro da seção `Resources` do template. O novo código está entre os comentários `INÍCIO DA ALTERAÇÃO` e `FIM DA ALTERAÇÃO`. Troque o valor de `Endpoint` pelo seu e-mail para poder receber a notificação. Lembre-se de salvar o arquivo.

```yaml

# Versão do template - não alterar
AWSTemplateFormatVersion: "2010-09-09"

# Descrição que será utilizada na stack
Description:
  Criacao de bucket S3 e disparo de mensagem SNS

# Parâmetros
Parameters:
  SufixoBucket:
    Type: String
    Default: nomesobrenome

  ##########
  # INÍCIO DA ALTERAÇÃO
  ##########
  EmailNotificacao:
    Type: String
    Default: email@email.com
  ##########
  # FIM DA ALTERAÇÃO
  ##########

# Recursos que serão provisionados
Resources:  
  # Provisionar um Bucket S3 privado
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: Private
      BucketName: !Sub dataops-deploy-${SufixoBucket}-${AWS::AccountId}-${AWS::Region}

  ##########
  # INÍCIO DA ALTERAÇÃO
  ##########
  # Provisionar Tópico SNS
  SnsTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: Topico-Evento-Deploy-S3

  # Provisionar assinatura do tópico
  SNSSubscription:
    Type: AWS::SNS::Subscription
    Properties:      
      Protocol: email
      Endpoint: !Sub ${EmailNotificacao}
      TopicArn: !Ref 'SnsTopic'

  # Provisionar política do tópico - receber publicacao do S3
  SNSTopicPolicy:
    Type: AWS::SNS::TopicPolicy
    Properties:
      Topics:
        - !Ref 'SnsTopic'
      PolicyDocument: 
        Id: TopicPolicyNotificationS3
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: 
              Service: s3.amazonaws.com
            Action: sns:Publish
            Resource: !Ref 'SnsTopic'
            Condition:
              ArnLike: 
                aws:SourceArn: 
                  !Join
                    - ""
                    - - "arn:aws:s3:::"
                      - !Ref 'S3Bucket'

  ##########
  # FIM DA ALTERAÇÃO
  ##########

#Saídas mostradas no CloudFormation
Outputs:
  ArnBucket:
    Description: Nome do bucket
    Value: 
      !Join
        - ""
        - - "arn:aws:s3:::"
          - !Ref 'S3Bucket'
  NomeBucket:
    Description: Nome do bucket
    Value: !Ref 'S3Bucket'
```

2.	Volte para o console da AWS e acesse o serviço CloudFormation novamente

3.	Selecione a stack criada anteriormente (`dataops-lab2`) clicando no radio button

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img19.png" width='100%'/>

4.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img20.png" />

5.	Selecione  <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img21.png" height='30'  />

6.	Selecione <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img22.png" height='30'  />

7.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img23.png" />

8.	Escolha o arquivo `s3-notification.yaml` que acabou de alterar

9. Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img24.png" />

10. Na seção `Parâmetros`, coloque o e-mail que quer receber as notificaçõs no parâmetro `EmailNotificacao`.

11.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img24.png" /> até o final

12.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img14.png" height='25' />

13.	Será mostrada a tela de execução da stack. Espere até o status mudar para <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img26.png" />

    a.	Atualize de vez em quando clicando em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img27.png" /> no canto superior direito

14.	Quando a stack terminar a execução, acesse o SNS para verificar o tópico e a assinatura criadas

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img28.png" width='100%' />
 
15.	Acesse seu e-mail para confirmar a assinatura do tópico 



### Inclusão do evento no S3

1. Volte para o VSCode e adicione no arquivo `s3-notification.yaml` a configuração do evento de inclusão e remoção de arquivos do S3 do recurso do bucket criado anteriormente. Adicione a propriedade `NotificationConfiguration` dentro de `Properties` no provisionamento do bucket S3, conforme o código abaixo O novo código está entre os comentários `INÍCIO DA ALTERAÇÃO` e `FIM DA ALTERAÇÃO`. Lembre-se de salvar o arquivo.

```yaml
# Atualização para incluir notificação de SNS no S3
# Versão do template - não alterar
AWSTemplateFormatVersion: "2010-09-09"

# Descrição que será utilizada na stack
Description:
  Criacao de bucket S3 e disparo de mensagem SNS

# Parâmetros
Parameters:
  SufixoBucket:
    Type: String
    Default: nomesobrenome
  EmailNotificacao:
    Type: String
    Default: email@email.com

# Recursos que serão provisionados
Resources:  
  # Provisionar um Bucket S3 privado
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: Private
      BucketName: !Sub dataops-deploy-${SufixoBucket}-${AWS::AccountId}-${AWS::Region}

      ##########
      # INICIO DA ALTERAÇÃO
      ##########
      # Configuração de notificação
      NotificationConfiguration:
        TopicConfigurations:
          - Topic: !Ref 'SnsTopic'
            Event: 's3:ObjectCreated:*'
          - Topic: !Ref 'SnsTopic'
            Event: 's3:ObjectRemoved:*'
      ##########
      # FIM DA ALTERAÇÃO
      ##########

  # Provisionar Tópico SNS
  SnsTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: Topico-Evento-Deploy-S3

  # Provisionar assinatura do tópico
  SNSSubscription:
    Type: AWS::SNS::Subscription
    Properties:      
      Protocol: email
      Endpoint: !Sub ${EmailNotificacao}
      TopicArn: !Ref 'SnsTopic'

  # Provisionar política do tópico - receber publicacao do S3
  SNSTopicPolicy:
    Type: AWS::SNS::TopicPolicy
    Properties:
      Topics:
        - !Ref 'SnsTopic'
      PolicyDocument: 
        Id: TopicPolicyNotificationS3
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: 
              Service: s3.amazonaws.com
            Action: sns:Publish
            Resource: !Ref 'SnsTopic'
            Condition:
              ArnLike: 
                aws:SourceArn: 
                  !Join
                    - ""
                    - - "arn:aws:s3:::"
                      - !Ref 'S3Bucket'

#Saídas mostradas no CloudFormation
Outputs:
  ArnBucket:
    Description: Nome do bucket
    Value: 
      !Join
        - ""
        - - "arn:aws:s3:::"
          - !Ref 'S3Bucket'
  NomeBucket:
    Description: Nome do bucket
    Value: !Ref 'S3Bucket'
```

2.	Atualize a stack da mesma forma que fez anteriormente

3.	Faça um teste inserindo e removendo arquivos do bucket. Você deve receber as notificações


## Questionário sobre o Lab 2

Responda ao questionário no sobre a realização deste laboratório.

## Documentação extra para referência

### Implantação do template CloudFormation

Troque `nomesobrenome` por seu nomesobrenome, para criar um nome único para o bucket.

Troque `email@email.com` ppelo e-mail que vai receber a notificação SNS.

```console
aws cloudformation deploy --template-file s3-notification.yaml --stack-name s3-notification-stack --parameter-overrides SufixoBucket=nomedobrenome EmailNotificacao=email@email.com
```

### Atualização template CloudFormation

Troque `nomesobrenome` por seu nomesobrenome, para criar um nome único para o bucket.

Troque `email@email.com` pelo e-mail que vai receber a notificação SNS.

```console
aws cloudformation deploy --template-file s3-notification-update.yaml --stack-name s3-notification-stack --parameter-overrides SufixoBucket=nomesobrenome EmailNotificacao=email@email.com`
```


<div class="footer">
    &copy; 2023 Fernando Sousa
    <br/>
    
Last update: 2023-08-05 20:05:12
</div>