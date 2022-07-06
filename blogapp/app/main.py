import email
from fastapi import FastAPI, Depends, Response, status
from .models import blog_model, user_model
from .schemas import blog_schema, user_schema
from .utils.database import get_engine, get_db
from sqlalchemy.orm import Session
from .utils.helper import (
    password_context,
    Hash
)

app = FastAPI()

blog_model.Base.metadata.create_all(get_engine())
user_model.Base.metadata.create_all(get_engine())


@app.get("/api/v1/blogs/unpublished")
def unpublished():
    return {
        "status": 200,
        "details": "OK",
        "data": "all unpublished blogs"
    }


@app.get("/api/v1/blogs", status_code = status.HTTP_200_OK)
def blogs(response: Response, db: Session = Depends(get_db)):
    try:
        blogs = db.query(blog_model.Blog).all()

        if blogs is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status": response.status_code,
                "details": "OK",
                "message": "Data not found!"
            }
    
        return {
            "status": response.status_code,
            "details": "OK",
            "data": blogs
        }

    except Exception as ex:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": response.status_code,
            "detail": "Something went wrong!",
            "message": ex
        }


@app.get("/api/v1/blogs/{id}", status_code = status.HTTP_200_OK)
def blog(response: Response, id: int, db: Session = Depends(get_db)):

    try:
        blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()

        if blog is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status": response.status_code,
                "details": "OK",
                "message": "Data not found!"
            }

        return {
            "status": 200,
            "details": "OK",
            "data": blog
        }

    except Exception as ex:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": response.status_code,
            "details": "Something went wrong!",
            "message": ex
        }


@app.post("/api/v1/blog", status_code = status.HTTP_201_CREATED)
def create_blog(response: Response, blog: blog_schema.Blog, db: Session = Depends(get_db)):

    new_blog = blog_model.Blog(title = blog.title, body=blog.body)

    try:
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)

        return {
            "status": 201,
            "details": "Created",
            "message": "Blog is created! Blog name is {title}".format(title=new_blog.title)
        }

    except Exception as ex:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": response.status_code,
            "details": "Something went wrong!",
            "message": ex
        }


@app.delete('/api/v1/blogs/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id:int, db: Session = Depends(get_db)):
    try:
        blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()

        if blog is None:
            return {
                'status': 404,
                'details': "Data not found!",
                'data': []
            }
        
        db.query(blog_model.Blog).filter(blog_model.Blog.id == id).delete(synchronize_session=False)
        db.commit() 

        return {
            'status': 204,
            'details': "Done",
            'data': []
        }

    except Exception as ex:
        return {
            'status': 500,
            'details': "Something went wrong!",
            'message': ex 
        }


@app.put("/api/v1/blogs/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: blog_schema.Blog, db: Session = Depends(get_db)):
    try:
        blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()

        if blog is None:
            return{
                'status': 404,
                'details': "Data not found!",
                'data': []
            }

        db.query(blog_model.Blog).filter(blog_model.Blog.id == id).update(request.dict(), synchronize_session=False)
        db.commit()

        return {
            'status': 200,
            'details': "OK",
            'data': [] 
        }
    
    except Exception as ex:
        return {
            'status': 500,
            'details': "Something went wrong!",
            'message': ex 
        }


@app.post("/api/v1/register")
def create_user(request: user_schema.User, db: Session = Depends(get_db)):
    try:
        new_user = user_model.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return{
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


@app.get("/api/v1/blogs/{id}/comments")
def blog_comments(id: int):
    return {
        "status": 200,
        "details": "OK",
        "data": f"comments for blog {id}"
    }