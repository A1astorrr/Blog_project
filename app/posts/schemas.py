from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    
class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostInDB(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True