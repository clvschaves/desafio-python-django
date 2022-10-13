## Projeto para vaga de estágio

A ideia do projeto é ver a capacidade de desenvolver a aplicação descrita abaixo.

# O que preciso fazer?

* Faça um "fork" desse projeto para sua conta GitHub.
* Implemente o desafio descrito no tópico abaixo.
* Faça um push para seu repositório com o desafio implementado.
* Envie um email para (cloves.chaves@recife.gov.br) avisando que finalizou o desafio com a url do seu fork.

## Encurtador de URL

Tecnologias:
- Python 3
- Django 3
- Bootstrap como template html (https://getbootstrap.com/)

O interessado pode ficar a vontade na escolha da interface, é apenas necessário que use o Bootstrap. A ideia é ter uma tela inicial onde o usuário possa preencher a url que deseja encurtar e um código como (teste-legal), e após o envio da URL ela seja salva no banco de dados e gere uma url no serguinte formato: http://url.py/teste-legal/

Onde o teste-legal é um conjunto de letras que o usuário indicou como código para aquela URL, esse código deve ser único no banco de dados.
Para fins de teste, ao acessar a aplicação localmente: http://localhost:8000/teste-legal/ deverá ser redirecionado para a url que foi salva com o código teste-legal

### Arquitetura e documentação

No arquivo README do projeto explique o funcionamento e a arquitetura da solução adotada na sua implementação. Descreva também os passos para executar corretamente seu projeto.
