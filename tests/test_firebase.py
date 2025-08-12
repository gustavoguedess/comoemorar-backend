from app.services.firebase_service import create_user, get_user, update_user, delete_user

uid = "test_uid"
data = {"nome": "Teste", "email": "teste@exemplo.com"}

# Testa criação
def test_create_user():
    create_user(uid, data)
    user = get_user(uid)
    print("Usuário criado:", user)
    assert user is not None and user["nome"] == "Teste"

def test_update_user():
    update_user(uid, {"nome": "Novo Nome"})
    user = get_user(uid)
    print("Usuário atualizado:", user)
    assert user is not None and user["nome"] == "Novo Nome"

def test_delete_user():
    delete_user(uid)
    user = get_user(uid)
    print("Usuário removido:", user)
    assert user is None

if __name__ == "__main__":
    test_create_user()
    test_update_user()
    test_delete_user()
