from pyexpat import model
from urllib import request, response
from fastapi import Depends, FastAPI, status, Response, HTTPException
from src.schemas import Blog
from src.models import blog_model

from src.database.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()

blog_model.Base.metadata.create_all(engine)


@app.post('/api/v1/blogs', status_code=status.HTTP_201_CREATED)
async def create_blog(blog:Blog, db: Session = Depends(get_db)):
    try:
        _new_blog = blog_model.Blog(id=blog.id, published=blog.published, title=blog.title, description=blog.description)
        db.add(_new_blog)
        db.commit()
        db.refresh(_new_blog)
    except Exception as e:
        raise e

    return _new_blog

@app.get("/api/v1/blogs")
async def show_blogs(db: Session = Depends(get_db)):
    blogs = db.query(blog_model.Blog).all()
    return blogs

@app.get("/api/v1/blogs/{id}", status_code=200)
async def show_blog(id, response:Response, db: Session = Depends(get_db)):
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()

    # Alternative usage
    # if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"status":response.status_code, "message": f"Blog with the id {id} is not found!"}

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found!")
    
    return blog


# @app.delete("/api/v1/blogs/{id}", status_code=204)
# async def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()

#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found!")
#     else:
#         db.query(blog_model.Blog).filter(blog_model.Blog.id == id).delete(synchronize_session=False)


#     db.commit()
#     return {"status": status.HTTP_204_NO_CONTENT, "message": "Selected blog deleted!"}


@app.put('/api/v1/blogs/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, blog:Blog, db: Session = Depends(get_db)):

    try:
        res = db.query(blog_model.Blog).filter(blog_model.Blog.id == id)
        
        if not res.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found!")
        else:
            db.query(blog_model.Blog).filter(blog_model.Blog.id == id).delete(synchronize_session=False)

        res.update(blog)
        db.commit()
        return res
    except Exception as ex:
        print(ex)
    
   