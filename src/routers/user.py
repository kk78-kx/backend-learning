from fastapi import APIRouter
from src.models.user import User
from src.services.user_service import get_all_users

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[User])
def get_users():
    return get_all_users()