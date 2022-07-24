from fastapi import APIRouter, Depends
from ..models import user_model
from ..schemas import user_schema
from ..utils.database import get_db
from sqlalchemy.orm import Session
from ..utils.hashing import Hash

router = APIRouter(
    tags=["Users"]
)

@router.post("/api/v1/register")
def create_user(request: user_schema.User, db: Session = Depends(get_db)):
    try:
        new_user = user_model.User(name=request.name,
                                   email=request.email,
                                   password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            'status': 200,
            'details': "OK",
            'message': f"User created as name {new_user.name}"
        }

    except Exception as ex:
        return {
            'status': 500,
            'details': "Something went wrong!",
            'message': "User not created!"
        }


@router.get("/api/v1/users/{id}")
def user(id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(
            user_model.User).filter(user_model.User.id == id).first()

        if user is None:
            return {
                'status': 404,
                'details': "Not found!",
                'message': "User not found!"
            }

        response_user = user_schema.ShowUser.from_orm(user)

        return {
            'status': 200,
            'details': "OK",
            'message': "",
            'data': response_user
        }
    except Exception as ex:
        return {
            'status': 500,
            'details': "Something went wrong!",
            'message': "Error"
        }
