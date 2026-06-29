from sqlalchemy import Column
from sqlalchemy import Integer 
from sqlalchemy import String 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.database.db import Base 

class User(Base):
    __tablename__="users"

    id = Column(
        Integer,
        primary_key =True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    hashed_password = Column(
        String,
        nullable=False
    )



class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(
        String,
        primary_key=True
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )
    title = Column(
        String,
        nullable = True 
    )


class Message(Base):
    __tablename__ = "messages"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    session_id= Column(
        String,
        ForeignKey("chat_sessions.id")

    )
    role = Column(
        String 
    )

    content = Column(
        String 
    )


    

