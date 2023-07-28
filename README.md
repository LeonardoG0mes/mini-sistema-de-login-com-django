**Atualização do Método de Verificação de Email - README**

Este repositório contém uma nova atualização no método de verificação de email para a autenticação de usuários em um sistema web. Abaixo estão detalhadas as mudanças realizadas e as configurações necessárias para garantir o correto funcionamento.

### Novidades da Atualização

1. **Tempo de Expiração do Código:** Agora o código de autenticação possui um tempo de expiração de 2 minutos. Caso o usuário não insira o código dentro desse período, o código será considerado inválido e o usuário precisará solicitar um novo.

2. **Reenvio do Código:** Caso o usuário não tenha recebido ou tenha perdido o código de autenticação, foi adicionado um botão para reenviar o código para o email cadastrado. Esse recurso ajudará o usuário a obter um novo código válido.

3. **Proteção Contra Reenvio Indevido:** Para evitar reenvios indevidos, se o usuário estiver logado e tentar acessar a página de verificação de código pela URL, será redirecionado para a página inicial. Assim, o usuário não poderá reenviar o código sem necessidade.

### Configurações Necessárias

1. **Configuração do Ambiente:** Certifique-se de ter um ambiente Python configurado. É altamente recomendado utilizar uma virtualenv para garantir que as dependências não conflitem com outros projetos.

2. **Configurações do Django:** Verifique as configurações do Django em seu projeto. Certifique-se de que a aplicação "auth" esteja adicionada ao `INSTALLED_APPS` e de que o `AUTH_USER_MODEL` esteja definido corretamente. Além disso, confirme se as configurações de email no arquivo `settings.py` estão corretas para enviar os emails de autenticação.

3. **Configurações do Banco de Dados:** Antes de executar o projeto, certifique-se de que as migrações do Django foram aplicadas corretamente para criar a tabela do modelo `PerfilUsuario`.

4. **Configuração de Email:** É importante configurar corretamente as configurações de email em `settings.py`. Por exemplo:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_smtp_host'
EMAIL_PORT = 'your_smtp_port'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

Substitua os campos `your_smtp_host`, `your_smtp_port`, `your_email@example.com` e `your_email_password` pelos valores de configuração corretos do seu servidor de email.

### Como Usar

1. **Cadastro de Usuário:** Para criar um novo usuário, acesse a página de cadastro e preencha os campos obrigatórios: nome de usuário, email e senha. O sistema verificará se o nome de usuário e o email já estão em uso.

2. **Verificação de Email:** Após o cadastro, o usuário receberá um código de autenticação no email cadastrado. Digite o código na página de verificação de código. Caso o código seja válido e dentro do prazo de expiração, o usuário será autenticado e redirecionado para a página inicial.

3. **Reenvio de Código:** Se o usuário não tiver recebido o código ou ele tiver expirado, é possível solicitar um novo código clicando no link ou botão "Reenviar Código". Um novo código será gerado e enviado ao email cadastrado.
Certifique-se de ter o Django instalado no seu ambiente virtual Python. Caso ainda não tenha instalado, você pode fazê-lo usando o seguinte comando:

###Configurações necessarias 

Copy code
pip install django
Após garantir que o Django está instalado, verifique se o seu aplicativo Django está configurado corretamente. No seu caso, parece que o aplicativo está configurado com o nome "users", pois você importou o modelo "PerfilUsuario" do arquivo "models.py" no código anterior.

Abra um terminal e navegue até o diretório raiz do seu projeto Django, onde se encontra o arquivo "manage.py".

Agora, para criar as migrações iniciais, execute o seguinte comando no terminal:

Copy code
python manage.py makemigrations
Esse comando irá analisar o modelo do seu aplicativo e criar um arquivo de migração para as alterações detectadas.

Em seguida, aplique as migrações para atualizar o banco de dados usando o comando:

Copy code
python manage.py migrate
Esse comando aplicará as migrações pendentes e atualizará o banco de dados de acordo com as alterações no modelo.

Se você tiver definido algum código para criar usuários ou realizar outras operações no arquivo "views.py", certifique-se de que ele esteja correto e funcione conforme esperado.

Agora, seu banco de dados deve estar configurado com as tabelas necessárias para o modelo "PerfilUsuario" e outras tabelas padrão do Django, como a tabela de usuários.

Com esses passos, você deve ter realizado as migrações necessárias e configurado corretamente o seu aplicativo para trabalhar com o modelo "PerfilUsuario". Lembre-se de garantir que suas configurações de segurança e autenticação estejam adequadas para proteger informações sensíveis no aplicativo.

Caso ainda enfrente algum problema ou precise de mais ajuda, não hesite em perguntar!
### Observações

O projeto ainda está em desenvolvimento e possui algumas limitações, como o erro na página de verificação de código quando o usuário já está autenticado. Esse problema será resolvido em uma futura atualização.

Agradecemos por utilizar este método de verificação de email em seu projeto! Caso tenha alguma dúvida ou encontre problemas, fique à vontade para entrar em contato e contribuir com o desenvolvimento deste projeto.

**Atenção:** Este é o quinto branch do repositório. Certifique-se de estar utilizando a versão mais atualizada do código para aproveitar todas as funcionalidades implementadas.

---
*Espero que este README tenha sido útil e que você consiga configurar e utilizar o método de verificação de email em seu projeto de forma eficiente. Se tiver alguma dúvida, não hesite em perguntar!*
