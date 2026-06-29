import os 
from fastapi import APIRouter,UploadFile,File ,Depends
from app.services.pdf_loader import extract_text
from app.services.chunker import chunk_text
from app.services.vectorstores import save_chunks
from app.services.dependencies import get_current_user
router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post("/upload")
async def upload_pdf(file:UploadFile=File(...),
                     current_user = Depends(get_current_user)):
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path,"wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)
    chunks = chunk_text(text)
    save_chunks(chunks,file.filename)
    
    return {
        "status":"Success",
        "chunks_stored":len(chunks) 
    }