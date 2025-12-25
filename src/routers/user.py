from fastapi import APIRouter
from src.services.user_service import get_all_users

router = APIRouter()

@router.get("/users")
def get_users():
    return get_all_users()