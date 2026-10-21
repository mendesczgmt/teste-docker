from fastapi import APIRouter

router = APIRouter(prefix="/inicio", tags=["Inicio"])

@router.get("/")
def inicio():
    return {"mensagem": "Esse é o inicio"}