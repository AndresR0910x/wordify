from pydantic import BaseModel

# Modelo de entrada para la creacion de palabras 
class WordCreate(BaseModel):
    word: str
    translate: str
    
# Modelo de salida para las respuesas de la API 

class WordOut(BaseModel):
    id: int
    word: str
    translate: str
    
    class Config: orm_mode = True
    
    

