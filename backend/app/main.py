from fastapi import FastAPI 
from app.routes.upload import router as upload_router
from app.routes.chat import  router as chat_router 
from app.database.db import engine ,Base
from app.routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine) 

app = FastAPI(
    title="Custom QA Chatbot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {"message":"Hello I am going to do best "}