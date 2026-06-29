from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.models import User 
from app.services.auth import hash_password,verify_password
from app.models.schemas import LoginUser
from app.core.security import create_access_token
from app.services.dependencies import get_current_user
router = APIRouter(
    prefix="/auth",
    tags = ["Authentication"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@router.get("/me")
def me(
    current_user=Depends(get_current_user)
):
    return current_user

    


@router.post("/register")
def register(
    user:LoginUser,
    db:Session = Depends(get_db)
):
    existing_user = db.query(user).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return {
            "message":"Email already registered"
        }

    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hash_password(
            user.password 
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message":"User registered successfully"
    }

@router.post("/login")

def login(
    user:LoginUser,
    db:Session=Depends(get_db)
):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return {
            "message":"Invalid Email"
        }
    
    if not verify_password(
        user.password,
        db_user.hashed_password 
    ):
        return {
            "message":"Invalid Password"
        }
    
    token = create_access_token(
        {
            "sub":db_user.email,
            "user_id":db_user.id 
        }
    )

    return {
        "access_token":token,
        "token_type":"bearer"
    }
