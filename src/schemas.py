from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class Blog(BaseModel):
    id: Optional[UUID] = uuid4()
    published: bool
    title: str
    description: str
    # comments: list
