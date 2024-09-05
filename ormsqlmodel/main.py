from fastapi import FastAPI, HTTPException # type: ignore
import uvicorn  # type: ignore
from dotenv import load_dotenv
from sqlmodel import  select, Session , create_engine # type: ignore
from .config.db import create_tables,connection  # . mean find in local folder
from .models.todo import Todo ,UpdateTodo

 
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
    
    
@app.put("/updte_todo/{id}")    
def update_todo(id,todo:Todo):
    with Session(create_engine) as session:
        db_todo=session.get(Todo,id)
        if not db_todo:
            raise HTTPException(status_code=404)
        hero_data = todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(hero_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return db_todo
        
        

@app.delete("delete_todo/{id}")
def delete_todo():
    with Session(connection) as session:
        db_todo=session.get(Todo,id)
        if not db_todo:
            raise HTTPException(status_code=404)
        session.delete(db_todo)
        session.commit()
        session.refresh()
        return {"status":200,"message":"Todos deleted successfully"} 

def start():
    uvicorn.run("ormsqlmodel.main:app", host="127.0.0.1", port=8000, reload=True)


