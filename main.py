from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


class Pessoa(BaseModel):
    nome: str
    numero: str
    endereco: str


MONGO_URI = "mongodb+srv://Admin:Admin@cluster0.nazx3vn.mongodb.net/?retryWrites=true&w=majority"
client = AsyncIOMotorClient(MONGO_URI)


db = client["API_roni"]
colecao = db["Usuários"]

@app.post("/pessoas")
async def criar_pessoa(pessoa: Pessoa):
    # Substituindo dict() por model_dump(), conforme recomendado no Pydantic V2
    nova_pessoa = pessoa.model_dump()
    resultado = await colecao.insert_one(nova_pessoa)
    return {"id": str(resultado.inserted_id), "mensagem": "Pessoa cadastrada"}
