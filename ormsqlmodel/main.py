from fastapi import FastAPI, Body, Query, Path  # type: ignore
import uvicorn  # type: ignore
from dotenv import load_dotenv
from sqlmodel import  select, Session , create_engine # type: ignore
from .config.db import create_tables,connection  # . mean find in local folder
from .models.todo import Todo

 
 #python.env
# Create the FastAPI instance

load_dotenv()
app = FastAPI()

@app.post("/create_todo")
def create_todo(todo:Todo):
    with Session(connection) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

    




@app.get("/")
def read_root():
    return {"message": "Hello, World!"}




@app.get("/get_todos")
def get_todo():
    with Session( create_engine ) as session:
        statement = select(Todo)
        result = session.execute(statement)
        data = result.scalars().all()  
        return data
    
    
@app.put("/updte_todo")    
def update_todo():
        

def start():
    uvicorn.run("ormsqlmodel.main:app", host="127.0.0.1", port=8000, reload=True)


