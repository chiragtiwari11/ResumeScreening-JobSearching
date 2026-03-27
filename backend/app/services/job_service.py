from sqlalchemy.orm import Session
from app.models.job_model import Job

def create_job(db: Session, job):
    db_job = Job(title=job.title, skills=job.skills)
    db.add(db_job)
    db.commit()
    return db_job

def get_jobs(db: Session):
    return db.query(Job).all()