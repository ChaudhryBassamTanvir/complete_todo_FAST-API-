from sqlmodel import SQLModel, create_engine, select, Field, Session  # type: ignore
import os
 
from typing import Any

#E58rnAfdhRLmEXme
# Define the connection string
connection_string :Any = os.getenv('DB_SECRET_STRING')


connection = create_engine(connection_string)


def create_tables():
    # Create the tables in the database
    SQLModel.metadata.create_all(connection)