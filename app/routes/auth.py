from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/signup")
async def signup(payload : UserCreate):
    return await AuthService.create_user(payload)

