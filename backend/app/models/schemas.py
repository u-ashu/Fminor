from pydantic import BaseModel 
from pydantic import EmailStr
class ChatRequest(BaseModel):
    session_id:str
    question:str 


class LoginUser(BaseModel):
    email:EmailStr
    password:str