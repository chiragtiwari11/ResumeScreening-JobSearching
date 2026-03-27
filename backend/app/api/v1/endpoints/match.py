from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from app.services.match_service import match_jobs

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def match(resume_text: str, db=Depends(get_db)):
    return match_jobs(resume_text, db)