from app.services.firebase_service import create_user, get_user
from app.services.auth_service import hash_password

uid = "mrgustavoip"
data = {
    "nome": "Gustavo",
    "email": "mrgustavoip@exemplo.com",
    "senha": hash_password("guedes")
}

def test_create():
    create_user(uid, data)
    user = get_user(uid)
    print("Usuário criado:", user)
    assert user is not None and user["email"] == data["email"]

if __name__ == "__main__":
    test_create()
