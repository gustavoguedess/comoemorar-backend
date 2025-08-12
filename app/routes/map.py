from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_map_data():
    # Implementar entrega de dados para mapas
    return {"message": "Dados do mapa"}
