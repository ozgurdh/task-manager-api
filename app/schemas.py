from typing import Optional
from sqlmodel import SQLModel

class TaskCreate(SQLModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskRead(SQLModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None