from schemas import word_schemas
from database import Session as DBSession
from models.word_model import WordCreate, WordOut



def create_word(word_data: WordCreate):
    session = DBSession()
    new_word = word_schemas.Word(word=word_data.word, translate=word_data.translate)
    session.add(new_word)
    session.commit()
    session.refresh(new_word)
    session.close()
    return new_word

#Get all words
def get_words():
    try:
        session = DBSession()
        words = session.query(word_schemas.Word).all()
        return words
    except Exception as e:
        print("Error al obtener palabras:", e)
        return []


# Get word by id 
def read_word(word_id: int):
    session = DBSession()
    word = session.query(word_schemas.Word).filter(word_schemas.Word.id == word_id).first()
    session.close()
    return word

#Update a word 
def update_word(word_id: id, new_word: str, new_translate: str):
    session = DBSession()
    word = session.query(word_schemas.Word).filter(word_schemas.word.id == word_id).first()
    if word:
        word.word = new_word
        word.translate = new_translate
        session.commit()
        session.refresh(word)
    session.close()
    return word


# Delete a word
def delete_word(word_id: int):
    session = DBSession()
    word = session.query(word_schemas).filter(word_schemas.Word.id == word_id).first()
    if word: 
        session.delete(word)
        session.commit()
    session.close()
    return word        
    
    