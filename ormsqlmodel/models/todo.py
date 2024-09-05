from sqlmodel import SQLModel, Field  # type: ignore

class TodoDetail(SQLModel, table=True):  # This will create the "todos_detail" table
    id: int = Field(default=None, primary_key=True)
    title: str | None
    description: str
    is_completed: bool  # Changed from 'is_active' to 'is_completed'

class UpdateTodoDetail(SQLModel):  # Model for updating the todo item
    title: str | None
    description: str | None
    is_completed: bool | None  # Updated field
