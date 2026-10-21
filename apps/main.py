from fastapi import FastAPI


from apps.inicio.router import router as inicio_router


app = FastAPI()
app.include_router(inicio_router)


@app.get("/")
def status():
    return {
        "status code": 200,
        "mensagem": "API no ar com sucesso"
    }