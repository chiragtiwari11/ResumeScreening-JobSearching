from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from app.services.job_service import create_job, get_jobs
from app.schemas.job_schema import JobCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_job(job: JobCreate, db=Depends(get_db)):
    return create_job(db, job)

@router.get("/")
def jobs(db=Depends(get_db)):
    return get_jobs(db)