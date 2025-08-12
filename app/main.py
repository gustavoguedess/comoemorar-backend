from fastapi import FastAPI
from app.routes import auth, openai, user, map

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(openai.router, prefix="/openai")
app.include_router(user.router, prefix="/user")
app.include_router(map.router, prefix="/map")

@app.get("/")
def read_root():
    return {"message": "API do ComoEmorar Backend"}
