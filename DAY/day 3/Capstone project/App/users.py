from datetime import datetime
from typing import List
from uuid import uuid4
from fastapi import APIRouter,Depends,HTTPException,status
from pymongo.collection import collection
from App.dependencies import get_users_collection
from App.schemas.user import UserCreate,UserUpdate,UsersResponse

router = APIRouter(prefix ="/users",tags=["Users"])
@router.post("/",response_model=UserCreate,status_code=status.HTTP_201_CREATED)
def create_user(payload:UserCreate, users_collections: Colection = Depends(get_users_collection)):
    if users_collections.find_one({"email":payload.email}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with this email already exists")

    user_doc = { "id": str(uuid4()), "name": payload.name, "email": payload.email, "role": payload.role, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow() }
    users_collections.insert_one(user_doc)
    return user_doc