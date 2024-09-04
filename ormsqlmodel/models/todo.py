
from sqlmodel import SQLModel,  Field  # type: ignore

class Todo(SQLModel, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    is_complete: bool


