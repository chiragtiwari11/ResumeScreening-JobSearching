from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    skills: str