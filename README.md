# Sistema de Autenticação com Django

Este é um projeto de estudo que implementa um sistema básico de autenticação usando o framework Django. O objetivo é explorar os conceitos de cadastro de usuários, autenticação e proteção de rotas com login obrigatório.

## Funcionalidades

- Cadastro de novos usuários com nome de usuário, email e senha.
- Verificação de existência de usuário para evitar duplicatas.
- Autenticação de usuários com base no nome de usuário e senha fornecidos.
- Proteção de rotas usando o decorator `@login_required`.
- Redirecionamento para a página inicial após o login bem-sucedido.

## Requisitos

- Python 3.x
- Django 3.x

## Instalação

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado e configurado corretamente.
3. Crie um ambiente virtual (opcional, mas recomendado) e ative-o.
5. Execute as migrações do Django para criar as tabelas do banco de dados usando o comando `python manage.py migrate`.
6. Inicie o servidor de desenvolvimento com o comando `python manage.py runserver`.

## Uso

- Acesse a página de cadastro em `/auth/cadastro` para criar um novo usuário.
- Faça o login em `/auth/login` usando as credenciais do usuário cadastrado.
- Após o login bem-sucedido, você será redirecionado para a página inicial em `/auth/home`.

## Senha de Admin
login: admin
senha: admin1234

Sinta-se à vontade para personalizar e adicionar mais informações ao README de acordo com as características específicas do seu projeto. É uma boa prática fornecer uma descrição clara do projeto, instruções de instalação e uso, requisitos, e qualquer outra informação relevante para que outros desenvolvedores possam entender e contribuir para o projeto.
