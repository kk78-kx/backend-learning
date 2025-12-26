from fastapi import APIRouter
from src.models.user import User, UserCreate
from src.services.user_service import get_all_users, create_user



router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[User])
def get_users():
    return get_all_users()

@router.post("/", response_model=User)
def create(user: UserCreate):
    return create_user(user)
