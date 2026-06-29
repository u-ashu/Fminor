from fastapi import APIRouter,Depends 
from pydantic import BaseModel 
from app.services.memory import chat_history
from app.services.rag import ask_questions
from app.services.dependencies import get_current_user
import uuid
from sqlalchemy.orm import Session 
from fastapi import Depends 

from app.database.db import SessionLocal
from app.database.models import ChatSession

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

    

router = APIRouter()

class ChatRequest(BaseModel):
    question:str 


@router.post("/session")
async def create_session(
    current_user = Depends(get_current_user),
    db:Session = Depends(get_db)
):
    session_id = str(uuid.uuid4())

    session = ChatSession(
        id = session_id,
        user_id = current_user["user_id"],
        title="new chat"
    )

    db.add(session)
    db.commit()
    

    return {
        "session_id":session_id
    }

@router.post("/chat")
async def chat(data:ChatRequest,current_user = Depends(get_current_user)):
    result = ask_questions(data.session_id,data.question)
    return {
        "answer":result["answer"],
        "sources":result["sources"],
        "user":current_user["sub"]
    }


@router.delete("/history")
async def clear_history():
    chat_history.clear()

    return {
        "message":"History Cleared"
    }

@router.get("/sessions")
async def get_sessions():
    return list(chat_history.keys())

@router.delete("/session/{session_id}")
async def delete_session(session_id:str):
    chat_history.pop(session_id,None)
    return {"message":"Session deleted"}