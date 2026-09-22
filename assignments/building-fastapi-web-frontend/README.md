# 📘 Assignment: Building a Web Frontend for FastAPI

## 🎯 Objetivo

Crie uma interface web que consuma a API de itens construída com FastAPI. Você praticará estruturação de páginas HTML, manipulação do DOM, requisições `fetch()` e envio de dados JSON para uma API.

## 📝 Tarefas

### 🛠️ Criar a estrutura da interface

#### Descrição

Construa uma página HTML para exibir os itens retornados pela API e oferecer um formulário para cadastrar novos itens.

#### Requisitos

A página concluída deve:

- Conter uma seção para listar os itens da API.
- Conter um formulário com campos para nome e descrição do item.
- Incluir mensagens ou elementos visuais para indicar carregamento e erros.
- Usar HTML semântico e rótulos associados aos campos do formulário.

### 🛠️ Carregar itens da API

#### Descrição

Use JavaScript e `fetch()` para buscar os itens no endpoint `GET /items` e renderizá-los na página.

#### Requisitos

O programa concluído deve:

- Fazer uma requisição `GET` para o endpoint `/items`.
- Renderizar o nome e a descrição de cada item na interface.
- Atualizar a lista sem recarregar a página inteira.
- Exibir uma mensagem adequada quando não houver itens ou quando a requisição falhar.

### 🛠️ Enviar novos itens pelo formulário

#### Descrição

Conecte o formulário ao endpoint `POST /items` para permitir que o usuário crie itens diretamente pela interface.

#### Requisitos

O programa concluído deve:

- Interceptar o envio do formulário com JavaScript.
- Enviar os dados como JSON no corpo de uma requisição `POST` para `/items`.
- Atualizar a lista com o item criado quando a API retornar sucesso.
- Limpar o formulário após o cadastro bem-sucedido.
- Exibir uma mensagem de erro quando a API rejeitar a requisição.

Exemplo de corpo enviado:

```json
{
  "name": "Caderno",
  "description": "Caderno para anotações"
}
```
