from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas import word_schemas


# Database connection details
url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="wordifydb",
    port=5432
)


# Create engine
engine = create_engine(url)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables in the database


def create_tables():
    # Create all tables in the engine
    word_schemas.Word.metadata.create_all(engine)
    print("Table created successfully.")


if __name__ == "__main__":
    create_tables()
