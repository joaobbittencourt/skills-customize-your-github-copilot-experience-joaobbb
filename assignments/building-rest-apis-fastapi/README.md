# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST simples usando o framework FastAPI. Você praticará a criação de rotas, o uso de parâmetros de caminho e o recebimento de dados JSON para criar recursos em memória.

## 📝 Tarefas

### 🛠️ Configurar a aplicação FastAPI

#### Descrição

Use o arquivo `starter-code.py` para criar a aplicação e uma rota inicial que confirme que a API está funcionando.

#### Requisitos

O programa concluído deve:

- Criar uma instância de `FastAPI`.
- Disponibilizar uma rota `GET /`.
- Retornar uma resposta JSON com uma mensagem indicando que a API está funcionando.
- Permitir a execução local com um servidor compatível, como Uvicorn.

### 🛠️ Implementar consultas de itens

#### Descrição

Adicione uma coleção em memória e rotas para listar todos os itens e consultar um item pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Disponibilizar uma rota `GET /items` que retorne todos os itens.
- Disponibilizar uma rota `GET /items/{item_id}` que receba o identificador como parâmetro de caminho.
- Retornar o item correspondente quando o identificador existir.
- Retornar um erro HTTP `404` quando o item não existir.

### 🛠️ Criar novos itens

#### Descrição

Implemente uma rota para receber dados JSON e adicionar um novo item à coleção em memória.

#### Requisitos

O programa concluído deve:

- Definir um modelo de dados usando `pydantic` para validar o corpo da requisição.
- Disponibilizar uma rota `POST /items`.
- Aceitar pelo menos um nome e uma descrição para o novo item.
- Gerar ou atribuir um identificador ao item criado.
- Retornar o item criado com status HTTP `201`.

Exemplo de requisição:

```json
{
  "name": "Caderno",
  "description": "Caderno para anotações"
}
```
