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

# INSTRUÇÕES:

### VirtualEnv

O projeto foi desenvolvido em maquina virtual. Foi utilizado o `virtualenvwrapper` e sua instalação pode ser feita da seguinte forma: 
    
    ```
    Linux e Mac:
    sudo pip3 install virtualenvwrapper

    windows:
    pip3 install virtualenvwrapper-win
    ```

Para ativar o virtualenv deve-se executar o comando: 

    `
    workon selecao
    `
Com o ambiente carregado deve-se preencher os requerimentos:

    `
    $ virtualenv selecao
    $ source selecal/bin/activate
    (selecao)$ pip install -r requirements.txt
    `

Pronto! Já podemos executar o projeto. execute o seguinte comando:


    `
    python manage.py runserver
    `

O projeto será iniciado e você pdoerá acessa-lo pelo endereço: http://127.0.0.1:8000/

# Utilização

. Ao inserir a URL no campo indicado e pressionar o botão "Encurtar URL", será gerada uma chave de 10 caracteres que logo em seguida é apresentada ao usuário na seguinte forma: 'Rob.to/XXXXXXXXXX'

Para ter acesso a url, deve-se copiar os 10 caracteres referentes a chave (XXXXXXXXXX) e cola-lo logo após o endereço da pagina, ficando da seguinte forma: http://127.0.0.1:8000/XXXXXXXXXX

# Funcionamento

Quando a URL é inserida e o botão de "Encrutar URL" digitado, a view irá gerar um código de 10 caracteres aleatórios e salva-lo no banco de dados junto com a URL inserida. 

Quando a URL encurtada for acessada, a view irá consultar no model o valor 'short' referente a chave de 10 caracteres e, se encontrar o valor inserido, ela irá redirecionar a página correta.

    