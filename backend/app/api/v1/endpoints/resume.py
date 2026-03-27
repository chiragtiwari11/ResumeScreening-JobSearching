from fastapi import APIRouter, UploadFile
from app.services.ai.parser import extract_text

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    text = await extract_text(file)
    return {"resume_text": text}