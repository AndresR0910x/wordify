from fastapi import FastAPI
from routes.word_routes import router as word_router


app = FastAPI()

app.include_router(word_router)


@app.get('/home/')
def get_items():
    return {"Message" : "U are on HOME!"}


