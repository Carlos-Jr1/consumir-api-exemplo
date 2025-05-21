import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

from main import app  # Certifique-se de que 'main.py' é o nome correto do seu arquivo principal

# Dados simulados para a criação de uma pessoa
pessoa_exemplo = {
    "nome": "João da Silva",
    "numero": "11999999999",
    "endereco": "Rua das Flores, 123"
}

@pytest.mark.asyncio
async def test_criar_pessoa():
    # Cria um mock para insert_one que retorna um objeto com inserted_id simulado
    mock_insert = AsyncMock()
    mock_insert.return_value.inserted_id = "fake_id_123"

    # Usa patch para substituir colecao.insert_one por esse mock
    with patch("main.colecao.insert_one", mock_insert):
        # Usando TestClient ao invés de AsyncClient
        client = TestClient(app)
        response = client.post("/pessoas", json=pessoa_exemplo)

    assert response.status_code == 200
    assert response.json() == {
        "id": "fake_id_123",
        "mensagem": "Pessoa cadastrada"
    }
