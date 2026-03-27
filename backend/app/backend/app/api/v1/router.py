from fastapi import APIRouter
from app.api.v1.endpoints import resume, job, match

api_router = APIRouter()

api_router.include_router(resume.router, prefix="/resume")
api_router.include_router(job.router, prefix="/job")
api_router.include_router(match.router, prefix="/match")