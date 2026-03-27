from app.services.ai.similarity import calculate_similarity
from app.services.job_service import get_jobs

def match_jobs(resume_text, db):
    jobs = get_jobs(db)

    results = []
    for job in jobs:
        score = calculate_similarity(resume_text, job.skills)
        results.append({
            "job": job.title,
            "score": round(score * 100, 2)
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)