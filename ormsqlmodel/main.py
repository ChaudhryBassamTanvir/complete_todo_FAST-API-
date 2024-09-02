from fastapi import FastAPI, Body, Query, Path  # type: ignore
import uvicorn  # type: ignore
from dotenv import load_dotenv
from sqlmodel import  select, Session  # type: ignore
from .config.db import create_tables , create_engine # . mean find in local folder
from .models.todo import Todo





 #python.env
# Create the FastAPI instance

load_dotenv()
app = FastAPI()






#
# Add a simple route for testing
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}




@app.get("/getTodos")
def get_todo():
    with Session( create_engine ) as session:
        statement = select(Todo)
        result = session.execute(statement)
        data = result.scalars().all()  # .all() fetches all records as a list
        return data
    
    
# @app.get("/getSingleStudents")
# def get_single_students():
#     with Session( create_engine ) as session:
#         statement = select(Todo).where(Todo.title=="Bassam")
#         result = session.execute(statement)
#         data = result.scalars().all()  # .all() fetches all records as a list
#         return data

# a start function to run the application
def start():
    uvicorn.run("ormsqlmodel.main:app", host="127.0.0.1", port=8000, reload=True)


