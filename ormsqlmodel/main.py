from fastapi import FastAPI, HTTPException  # type: ignore
import uvicorn  # type: ignore
from dotenv import load_dotenv
from sqlmodel import select, Session  # type: ignore

# Load environment variables
load_dotenv()

from .config.db import create_tables, connection
from .models.todo import TodoDetail, UpdateTodoDetail

# Create the FastAPI instance
app = FastAPI()

# Initialize the database tables
create_tables()

@app.post("/create_todo")
def create_todo(todo: TodoDetail):
    with Session(connection) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"status": "Todo created successfully", "detail": todo}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/get_todos")
def get_todos():
    with Session(connection) as session:
        statement = select(TodoDetail)
        result = session.execute(statement)
        data = result.scalars().all()
        return data

@app.put("/update_todo/{id}")
def update_todo(id: int, todo: UpdateTodoDetail):
    with Session(connection) as session:
        db_todo = session.get(TodoDetail, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo_data = todo.dict(exclude_unset=True)
        for key, value in todo_data.items():
            setattr(db_todo, key, value)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return db_todo

# @app.delete("/delete_todo/{id}")
# def delete_todo(id: int):
#     with Session(connection) as session:
#         db_todo = session.get(TodoDetail, id)
#         if not db_todo:
#             raise HTTPException(status_code=404, detail="Todo not found")
#         session.delete(db_todo)
#         session.commit()
#         return {"status": 200, "message": "Todo deleted successfully"}

def start():
    uvicorn.run("ormsqlmodel.main:app", host="127.0.0.1", port=8000, reload=True)
