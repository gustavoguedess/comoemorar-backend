from app.services.auth_service import create_access_token, decode_access_token
from datetime import timedelta

def test_jwt():
    # Dados simulados do usuário
    payload = {"uid": "test_uid", "email": "teste@exemplo.com"}
    token = create_access_token(payload, expires_delta=timedelta(minutes=1))
    print("Token JWT gerado:", token)
    decoded = decode_access_token(token)
    print("Payload decodificado:", decoded)
    assert decoded["uid"] == payload["uid"]
    assert decoded["email"] == payload["email"]

if __name__ == "__main__":
    test_jwt()
