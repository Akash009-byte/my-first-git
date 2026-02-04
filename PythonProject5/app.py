from flask import Flask, render_template, request
import os
from parser_logic import extract_text_from_pdf, calculate_similarity

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create an 'uploads' folder if it doesn't exist to store resumes temporarily
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'resume' not in request.files:
        return "No file part"

    file = request.files['resume']
    jd = request.form['job_description']

    if file.filename == '':
        return "No selected file"

    if file:
        # Save the uploaded PDF
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Extract text using your Step 2 logic
        resume_text = extract_text_from_pdf(file_path)

        # Calculate the score
        score = calculate_similarity(resume_text, jd)

        # Remove the file after processing to keep your project clean
        os.remove(file_path)

        return f"""
        <h1>Analysis Complete</h1>
        <p>Your Resume Match Score is: <strong>{score}%</strong></p>
        <a href='/'>Try another resume</a>
        """


if __name__ == '__main__':
    app.run(debug=True)