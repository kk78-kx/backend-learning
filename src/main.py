from fastapi import FastAPI
from src.models.user import User
from src.routers.user import router as user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend Learning Day 4"}

app.include_router(user_router)
