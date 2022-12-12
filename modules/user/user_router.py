from fastapi import APIRouter
from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .user_schema import User, Token, UserCreate
from .user_service import authenticate_user, create_access_token, verify_user_permission, get_current_user
from .user_repository import fake_users_db


ACCESS_TOKEN_EXPIRE_MINUTES = 30


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/create", response_model=User)
async def create_user(user: UserCreate, current_user: User = Depends(verify_user_permission)):
    return User(
        **user.dict(),
        id="djfdgvidunhvdovmdf",
        role="team_user",
    )


@router.get("/current/", response_model=User)
async def read_users_current(current_user: User = Depends(get_current_user)):
    return current_user
