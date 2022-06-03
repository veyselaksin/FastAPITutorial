from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.database.database import Base

# class Blog(BaseModel):
#     id: Optional[UUID] = uuid4()
#     published: bool
#     title: str
#     description: str
#     comments: list

class Blog(Base):
    __tablename__ = "blogs"

    id =  Column(UUID(as_uuid=True), primary_key=True, index=True)
    published = Column(Boolean)
    title = Column(String)
    description = Column(String)
