## Objetivo do desafio
Criar uma aplicação web que implemente um CRUD de veículos. Um veículo é um carro ou moto com as seguintes características:

### Carro:
- Montadora (Chevrolet, Ford, Honda, ...)
- Modelo (Monza, Fusion, Maverick, ...)
- Cor (azul, verde, vermelho, ...)
- Kilometragem (0km, 5000km, 12000km, ...)
- Motor (1.0, 1.4, 2.0, ...)

### Moto:
- Montadora (Ducati, Yamaha, Honda, ...)
- Modelo (Burgman, Tenere, MT-03, ...)
- Cor
- Kilometragem
- Motor (150, 660, 1200, ...)

A aplicação é apenas um CRUD sem usuários (não existe autenticação). Deve ser possível:
- Inserir, editar e deletar uma montadora, um modelo ou um veículo
- Pesquisar os veículos disponíveis com a possibilidade de filtrar por quaisquer características ou combinação de características disponíveis. Também deve ser possível filtrar por faixas de valores. Por exemplo:
* Motos da Yamaha com kilometragem menor que 10000km;
* Carros Chevrolet com motor maior que 1.4

A interface de uso fica a critério do desenvolvedor. A UI/UX da aplicação não será avaliada, o únicos critérios que devem atendendidos são os requisitos funcionais. 

## Requisitos:
- A aplicação deve executar as operações de CRUD através de chamadas AJAX. É um diferencial positivo se a aplicação for uma SPA (single-page application). Outro diferencial bastante positivo é o frontend ser desenvolvido em AngularJS.
- Backend desenvolvido em qualquer linguagem dinamicamente tipada. É um diferencial positivo se for desenvolvido em Python. É mais positivo se utilizar o framework Django.
- Processo de desenvolvimento versionado via Git em algum repositório público do github ou bitbucket.
- Relatório de cobertura dos testes unitários de backend.
- Readme que explique como rodar o projeto, como gerar o relatório de cobertura e como executar quaisquer scripts necessários.
- A aplicação deve possuir um script que popula o banco inicialmente com alguns veículos para demonstração.


## 

[![Build Status](https://travis-ci.org/mfilipelino/vdbackend.svg?branch=master)](https://travis-ci.org/mfilipelino/vdbackend)

Criar uma aplicação web que implemente um CRUD de veículos. [vivadecora/backend-test](https://github.com/vivadecora/backend-teste)

## Dependências

- python3
- pip
- node
- npm

## Automação de tarefas

- `make install` para instalação de dependências
- `make build` para criar o banco e populá-lo
- `make test` para rodar os testes 
- `make pycoverage` acessar coverage/index.html
- `make run-server` iniciar o servidor htpp://localhost:8000


# Tecnologias 

## Frameworks

- django
- django-rest-framework
- angular

## Testes

- coverage
- django-test

## Qualidade de código

- jslint
- flake8

## Gerenciador de dependências

- pip
- bower

## Integração continua

- travis

# Referências 

- [djangular3](https://github.com/tonylampada/djangular3)
- [angular-phonecat](https://github.com/angular/angular-phonecat)
