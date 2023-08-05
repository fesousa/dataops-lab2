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

<img height="200" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img1.1.png" />

4.  Adicione um novo arquivo clicando em <img height="22" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img2.1.png" /> e depois em `New File`

5. Salve o arquivo com o nome `s3-notification.yaml` na pasta `lab2` apertando as teclas `ctrl` e `s` juntas. Ao abrir a janela de salvar, lembre-se de selecionar a pasta `lab2`

<img height="400" src="https://raw.github.com/fesousa/dataops-lab2/master/images/img5.1.png" />


### Provisionar Bucket S3

1.  No arquivo `s3-notification.yaml` coloque o seguinte código para configurar o template do CloudFormation e provisionar um Bucket S3. código também está [neste arquivo](https://github.com/fesousa/dataops-lab2/blob/master/code/s3.yaml).
Não esqueça de salvar o arquivo.

```yaml
${code/s3.yaml}
```

2.	Na AWS procure por CloudFormation e selecione o serviço

3.	Clique em  <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img8.png" />

5.	Selecione a opção <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img9.png" />

6.	Na tela de criação da Pilha:

    a.	Selecione a opção <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img10.png" />

    b. Faça o download do arquivo `s3-notification.yaml` do Cloud9 (clique com o botão direito no arquivo e escolha `Download`)

    c.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img11.png" />    
    
    d.  Escolha o arquivo `s3-notification.yaml` que acabou de baixar

    e.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img12.png" />. Se receber uma mensagem de erro, verifique se salvou o arquivo.

    f. Na próxima tela, em  `Stack name` coloque `dataops-lab2`

    g. Na seção `Parameters` coloque o seu nome e sobrenome no campo `SufixoBucket`, onde está com o valor `nomesobrenome`. Por exemplo: `fernandosousa`. Este parâmetro será utilizado no nome do bucket

    h.	 Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img13.png" /> nas próximas duas telas

    i.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img14.png" height='25' />

7.	Será mostrada a tela de execução da stack. Espere até o status mudar para <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img15.png" />

    a.	Atualize de vez em quando clicando em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img16.png" /> no canto superior direito

8.	Quando a stack terminar a execução, acesse o S3 para verificar o bucket criado

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img17.png" width='100%' />

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img18.png" width='100%' />


### Atualização do template e dos recursos

1.	Volte para o Cloud9 e adicione no arquivo `s3-notification.yaml` o provisionamento do tópico SNS, assinatura do tópico e política do tópico SNS dentro da seção `Resources` do template. O novo código está entre os comentários `INÍCIO DA ALTERAÇÃO` e `FIM DA ALTERAÇÃO`. Troque o valor de `Endpoint` pelo seu e-mail para poder receber a notificação. Lembre-se de salvar o arquivo.

```yaml
${code/s3-notification.yaml}
```

2.	Volte para o console da AWS e acesse o serviço CloudFormation novamente

3.	Selecione a stack criada anteriormente (`dataops-lab2`) clicando no radio button

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img19.png" width='100%'/>

4.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img20.png" />

5.	Selecione  <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img21.png" height='30'  />

6.	Selecione <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img22.png" height='30'  />

7. Faça o download no arquivo `s3-notification.yaml` do Cloud9 novamente

8.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img23.png" />

9.	Escolha o arquivo `s3-notification.yaml` que acabou de alterar

10. Clique em <img height='25' src="https://raw.github.com/fesousa/dataops-lab2/master/images/img24.png" />

11. Na seção `Parameters`, coloque o e-mail que quer receber as notificaçõs no parâmetro `EmailNotificacao`.

12.	Clique em <img height='25' src="https://raw.github.com/fesousa/dataops-lab2/master/images/img24.png" /> até o final

13.	Clique em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img14.png" height='25' />

14.	Será mostrada a tela de execução da stack. Espere até o status mudar para <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img26.png" />

    a.	Atualize de vez em quando clicando em <img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img27.png" /> no canto superior direito

15.	Quando a stack terminar a execução, acesse o SNS para verificar o tópico e a assinatura criadas

<img src="https://raw.github.com/fesousa/dataops-lab2/master/images/img28.png" width='100%' />
 
16.	Acesse seu e-mail para confirmar a assinatura do tópico 



### Inclusão do evento no S3

1. Volte para o VSCode e adicione no arquivo `s3-notification.yaml` a configuração do evento de inclusão e remoção de arquivos do S3 do recurso do bucket criado anteriormente. Adicione a propriedade `NotificationConfiguration` dentro de `Properties` no provisionamento do bucket S3, conforme o código abaixo O novo código está entre os comentários `INÍCIO DA ALTERAÇÃO` e `FIM DA ALTERAÇÃO`. Lembre-se de salvar o arquivo.

```yaml
${code/s3-notification-update.yaml}
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
    {{update}}
</div>