from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Items API")

items = {
    1: {
        "name": "Caderno",
        "description": "Caderno para anotações",
    },
    2: {
        "name": "Caneta",
        "description": "Caneta azul",
    },
}


class ItemCreate(BaseModel):
    name: str
    description: str


@app.get("/")
def read_root():
    # TODO: Retornar uma mensagem informando que a API está funcionando.
    pass


@app.get("/items")
def list_items():
    # TODO: Retornar todos os itens.
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Retornar o item ou gerar HTTP 404 quando ele não existir.
    pass


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    # TODO: Criar um identificador, salvar o item e retorná-lo.
    pass


# Execute com: uvicorn starter-code:app --reload
