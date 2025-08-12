import os
import firebase_admin
from firebase_admin import credentials, firestore

from dotenv import load_dotenv

load_dotenv()

# Inicialização do Firebase
cred_path = os.getenv("FIREBASE_CREDENTIALS")
if not firebase_admin._apps:
	cred = credentials.Certificate(cred_path)
	firebase_admin.initialize_app(cred)

db = firestore.client()

def get_user(uid: str):
	"""Busca um usuário pelo UID na coleção 'users'"""
	doc_ref = db.collection('users').document(uid)
	doc = doc_ref.get()
	if doc.exists:
		return doc.to_dict()
	return None

def create_user(uid: str, data: dict):
	"""Cria ou atualiza um usuário na coleção 'users'"""
	db.collection('users').document(uid).set(data)
	return True

def update_user(uid: str, data: dict):
	"""Atualiza campos de um usuário na coleção 'users'"""
	db.collection('users').document(uid).update(data)
	return True

def delete_user(uid: str):
	"""Remove um usuário da coleção 'users'"""
	db.collection('users').document(uid).delete()
	return True
