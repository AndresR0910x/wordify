from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Session as get_db
from models.word_model import WordCreate, WordOut
from controllers.word_controller import create_word, get_words

router = APIRouter()


# Create a new word /Save words
@router.post('/CreateWords/', response_model=WordCreate)
def add_word(word: WordCreate):
    return create_word(word)


# Get all words
@router.get('/GetWords/', response_model=list[WordOut])
def get_all_words():
    return get_words()