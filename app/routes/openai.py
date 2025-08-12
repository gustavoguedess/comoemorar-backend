from fastapi import APIRouter

router = APIRouter()

@router.post('/query')
def query_openai():
    # Implementar consulta à OpenAI
    return {"message": "Consulta OpenAI"}
