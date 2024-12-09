from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Word(Base):
    __tablename__ = 'words'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String(100), nullable=False)
    translate = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    
    