from sqlmodel import SQLModel, create_engine, Session  # type: ignore
import os
from typing import Any

connection_string: Any = os.getenv('DB_SECRET_STRING')

print(connection_string)

connection = create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(connection)
