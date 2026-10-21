from fastapi.testclient import TestClient

from apps.main import app

client = TestClient(app)


def test_raiz():
    resposta = client.get("/")
    assert resposta.status_code == 201
    assert resposta.json()["mensagem"] == "API no ar com sucesso"


def test_inicio():
    resposta = client.get("/inicio/")
    assert resposta.status_code == 201
    assert resposta.json() == {"mensagem": "Esse é o inicio"}


def test_inicio_teste():
    resposta = client.get("/inicio/teste")
    assert resposta.status_code == 201
    assert resposta.json() == {"mensagem": "Esse é o teste"}


def test_rota_inexistente():
    resposta = client.get("/nao-existe")
    assert resposta.status_code == 404
