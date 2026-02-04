import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # Loop through every page and pull the text out
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

def calculate_similarity(resume_text, job_description):
    # This turns the text into numbers (vectors) to compare them
    content = [resume_text, job_description]
    cv = TfidfVectorizer()
    matrix = cv.fit_transform(content)
    similarity_matrix = cosine_similarity(matrix)
    # Returns the match as a percentage
    return round(similarity_matrix[0][1] * 100, 2)