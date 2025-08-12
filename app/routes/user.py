from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_user():
    # Implementar busca de dados do usuário
    return {"message": "Dados do usuário"}
