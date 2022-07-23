from fastapi import APIRouter
from fastapi import Depends, Response, status
from ..models import blog_model
from ..schemas import blog_schema
from ..utils.database import get_db
from sqlalchemy.orm import Session
from ..utils.helper import delete_dict_item

router = APIRouter()

@router.get("/api/v1/blogs/unpublished")
def unpublished():
    return {
        "status": 200,
        "details": "OK",
        "data": "all unpublished blogs"
    }


@router.get("/api/v1/blogs", status_code = status.HTTP_200_OK, tags=["blogs"])
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

@router.get("/api/v1/blogs/{id}", status_code = status.HTTP_200_OK, tags=["blogs"])
def blog(response: Response, id: int, db: Session = Depends(get_db)):

    try:
        blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()
        # user_schema.ShowUser.from_orm(blog)
        blog_schema.ShowBlog.from_orm(blog)

        blog = delete_dict_item(blog.__dict__, keys=["id", "user_id", "password", "_sa_instance_state"], is_sub_dict=True, sub_dict="creator")

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
        print(ex)
        return {
            "status": response.status_code,
            "details": "Something went wrong!",
            "message": ex
        }


@router.post("/api/v1/blog", status_code = status.HTTP_201_CREATED, tags=["blogs"])
def create_blog(response: Response, blog: blog_schema.Blog, db: Session = Depends(get_db)):

    new_blog = blog_model.Blog(title = blog.title, body=blog.body, user_id=18)

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
        print(ex)
        return {
            "status": response.status_code,
            "details": "Something went wrong!",
            "message": ex
        }


@router.delete('/api/v1/blogs/{id}', status_code=status.HTTP_200_OK, tags=["blogs"])
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


@router.put("/api/v1/blogs/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
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

@router.get("/api/v1/blogs/{id}/comments", tags=["blogs"])
def blog_comments(id: int):
    return {"status": 200, "details": "OK", "data": f"comments for blog {id}"}
