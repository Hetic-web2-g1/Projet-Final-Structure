from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from typing import List

from database.db_engine import engine
from schema.user import UserCreate, User
from manager import UserManager

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=List[User | None])
def get_all_users():
    with engine.begin() as conn:
        return list(UserManager.get_all_users(conn))


@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    with engine.begin() as conn:
        user =  UserManager.get_user_by_id(conn, user_id)
        if user is None:
            raise HTTPException(404, "User not found")
        else:
            return user


@router.post("", response_model=User | None)
def create_user(user: UserCreate):
    # A supp
    user = UserCreate(**{
        'is_admin': True,
        'pseudo': 'SQSQKJS',
        'password': 'Zeremie',
        'email': 'zeremie@zeremie.zeremie',
        'description': 'zeremie',
        'sport_level': 9999,
        'favorite': [3],
        'date_of_birth': 0,
        'location': [222, 333],
        'img_path': 'zeremie/zeremie/zeremie/zeremie.zeremie'
    })
    with engine.begin() as conn:
        return UserManager.create_user(conn, user)
