from fastapi import APIRouter, Depends
from ..schemas import authentication_schema
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..models.user_model import User
from ..utils.hashing import Hash
from ..utils.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/api/v1/login")
def login(request: authentication_schema.Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        return ({'message': "User not found!"})

    if not Hash.verify(user.password, request.password):
        return ({'message': "Wrong password!"})

    # generate a jwt token and return the token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}