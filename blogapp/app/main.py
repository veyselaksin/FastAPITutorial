from os import stat
from fastapi import FastAPI, Depends, Response, status
from .models import blog_model
from .schemas import blog_schema
from .utils.database import get_engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()

blog_model.Base.metadata.create_all(get_engine())

@app.get("/api/v1/blog/unpublished")
def unpublished():
    return {
        "status": 200,
        "details": "OK",
        "data": "all unpublished blogs"
    }

@app.get("/api/v1/blogs", status_code = 200)
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


@app.get("/api/v1/blog/{id}", status_code = 200)
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

@app.post("/api/v1/blog", status_code = 201)
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

@app.get("/api/v1/blog/{id}/comments")
def blog_comments(id: int):
    return {
        "status": 200,
        "details": "OK",
        "data": f"comments for blog {id}"
    }