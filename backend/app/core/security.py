from jose import jwt ,JWTError
from datetime import datetime
from datetime import timedelta

SECRET_KEY = "serpent"
ALGORITHM = "HS256"


def verify_token(token:str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    
    except JWTError:
        return None 
    



    



def create_access_token(data):
    payload = data.copy()

    expire = datetime.utcnow()+timedelta(
        hours=24
    )

    payload.update (
        {"exp":expire}
    )

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token 