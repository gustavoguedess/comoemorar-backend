
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.firebase_service import create_user, get_user
from app.services.auth_service import hash_password, verify_password, create_access_token, decode_access_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    return payload

router = APIRouter()

class UserRegister(BaseModel):
    uid: str
    nome: str
    email: str
    senha: str

class UserLogin(BaseModel):
    email: str
    senha: str

@router.post('/register')
def register(user: UserRegister):
    # Verifica se usuário já existe
    existing = get_user(user.uid)
    if existing:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    data = {
        "nome": user.nome,
        "email": user.email,
        "senha": hash_password(user.senha)
    }
    create_user(user.uid, data)
    return {"message": "Usuário cadastrado com sucesso", "uid": user.uid}


@router.post('/login')
def login(login_data: UserLogin):
    from app.services.firebase_service import db
    users = db.collection('users').where('email', '==', login_data.email).stream()
    user = None
    for u in users:
        user = u.to_dict()
        break
    if not user or not verify_password(login_data.senha, user.get('senha')):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token({"uid": u.id, "email": user.get('email')})
    return {"message": "Login realizado com sucesso", "uid": u.id, "access_token": token}

@router.get('/me')
def me(user=Depends(get_current_user)):
    return {"user": user}
