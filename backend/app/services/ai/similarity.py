from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume, job):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, job])
    return cosine_similarity(vectors[0], vectors[1])[0][0]