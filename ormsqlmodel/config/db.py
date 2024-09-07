from sqlmodel import SQLModel, create_engine, Session  # type: ignore
import os
from typing import Any

# Load the connection string from environment variables
connection_string: Any = os.getenv('DB_SECRET_STRING')

print(connection_string)

# Create the database connection
connection = create_engine(connection_string)

def create_tables():
    # Create the tables in the database
    SQLModel.metadata.create_all(connection)
