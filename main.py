from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# ✅ Modelo de dados
class Pessoa(BaseModel):
    nome: str
    numero: str
    endereco: str

# ✅ Conexão com o MongoDB Atlas (substitua com seu usuário e senha reais)
MONGO_URI = "mongodb+srv://Admin:Admin@cluster0.nazx3vn.mongodb.net/?retryWrites=true&w=majority"
client = AsyncIOMotorClient(MONGO_URI)

# ✅ Banco e coleção
db = client["API_roni"]
colecao = db["Usuários"]  # use 'colecao' para manter igual com o resto do código

# ✅ Rota para inserir dados
@app.post("/pessoas")
async def criar_pessoa(pessoa: Pessoa):
    nova_pessoa = pessoa.dict()
    resultado = await colecao.insert_one(nova_pessoa)
    return {"id": str(resultado.inserted_id), "mensagem": "Pessoa cadastrada"}
