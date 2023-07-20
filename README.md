##Troca de Senha

## Visão Geral

Este projeto implementa uma nova funcionalidade de "Troca de Senha". A funcionalidade permite que os usuários alterem suas senhas de forma segura e eficiente.

## Funcionalidades

- Os usuários podem acessar a página "Trocar Senha" a partir de sua conta.
- Os usuários devem fornecer a "Senha Antiga" e a "Nova Senha" para concluir a troca de senha.
- As senhas são verificadas para garantir que a "Senha Antiga" fornecida seja válida.
- A nova senha deve ser confirmada digitando-a novamente.
- A página exibirá mensagens de erro se as senhas não corresponderem ou se houver outros problemas ao tentar alterar a senha.

## Tecnologias Utilizadas

- Linguagem de programação: Python
- Framework web: Django
- Front-end: HTML, CSS

## Configuração do Ambiente

1. Clone o repositório do projeto para sua máquina local.
2. Certifique-se de ter o Python [inserir versão] instalado.
3. Instale o Django executando o seguinte comando no terminal:

```
pip install django
```


## Executando o Projeto

1. Navegue até o diretório raiz do projeto no terminal.
2. Execute o seguinte comando para iniciar o servidor de desenvolvimento do Django:

```
python manage.py runserver
```

3. Abra o navegador e acesse `http://localhost:8000` para visualizar o aplicativo.

## Como Utilizar a Funcionalidade de Troca de Senha

1. Faça o login em sua conta no aplicativo.
2. Navegue até a página "Trocar Senha".
3. Digite sua "Senha Antiga" no campo apropriado.
4. Digite sua "Nova Senha" no campo apropriado.
5. Digite novamente a "Nova Senha" no campo de confirmação.
6. Clique no botão "Salvar" para confirmar a troca de senha.
7. Se todas as informações forem válidas, sua senha será alterada com sucesso e uma mensagem de sucesso será exibida.
8. Se houver algum problema, como senhas não coincidindo ou senha antiga incorreta, mensagens de erro serão exibidas.

