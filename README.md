# Sistema de Autenticação com Django

Este é um projeto de estudo que implementa um sistema de autenticação básico usando o Django.

## Novas atualizações

### Validação de Senha
- Adicionada validação de senha durante o cadastro do usuário.
- Agora a senha deve ter no mínimo 8 caracteres.
- A senha não pode ser uma senha comum, baseada em dicionários ou igual ao nome de usuário.

### Melhorias no Front-end
- Aprimoramento do layout das páginas de cadastro e login.
- A adição de estilos CSS deixou as páginas mais atraentes e profissionais.
- Os campos de senha agora ficam destacados em vermelho caso a senha seja curta ou inválida.

### Mensagens de Erro Personalizadas
- As mensagens de erro foram aprimoradas e passaram a ser exibidas diretamente na página.
- Os usuários recebem mensagens claras e precisas caso ocorram erros durante o cadastro ou login.

### Melhorias de Usabilidade
- Implementada validação em tempo real no formulário de login usando JavaScript.
- O botão de login só fica habilitado se todos os campos estiverem preenchidos.
- Isso impede que o usuário envie o formulário com campos vazios acidentalmente.

## Como executar o projeto

1. Clone o repositório para o seu ambiente local.
2. Crie e ative um ambiente virtual para o projeto.
3. Instale as dependências (Django)
4. Execute as migrações do banco de dados com o comando `python manage.py migrate`.
5. Inicie o servidor de desenvolvimento com o comando `python manage.py runserver`.
6. Acesse o sistema através do seu navegador no endereço `http://localhost:8000/auth/`.

## Login de Admin
Login: admin
senha: admin1234
