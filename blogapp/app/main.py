from fastapi import FastAPI 
from .models import blog_model, user_model
from .utils.database import get_engine
from .routers import user, blog

app = FastAPI()

blog_model.Base.metadata.create_all(get_engine())
user_model.Base.metadata.create_all(get_engine())

app.include_router(user.router)
app.include_router(blog.router)
