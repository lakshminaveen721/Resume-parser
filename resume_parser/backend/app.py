from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import pdfminer
import docx2txt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db:5432/resume_parser_db'
db = SQLAlchemy(app)
api = Api(app)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    contact_info = db.Column(db.Text)
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    skills = db.Column(db.Text)

    def __init__(self, name, contact_info, education, experience, skills):
        self.name = name
        self.contact_info = contact_info
        self.education = education
        self.experience = experience
        self.skills = skills

def extract_from_pdf(file):
    # Placeholder for PDF extraction logic
    return {
        "name": "John Doe",
        "contact_info": "john.doe@example.com",
        "education": "Bachelor's in Computer Science",
        "experience": "5 years as a software developer",
        "skills": "Python, JavaScript, Docker"
    }

def extract_from_docx(file):
    # Placeholder for DOCX extraction logic
    return {
        "name": "Jane Doe",
        "contact_info": "jane.doe@example.com",
        "education": "Master's in Data Science",
        "experience": "3 years as a data scientist",
        "skills": "Python, R, SQL"
    }

class ResumeUpload(Resource):
    def post(self):
        file = request.files['file']
        if file.filename.endswith('.pdf'):
            extracted_data = extract_from_pdf(file)
        elif file.filename.endswith('.docx'):
            extracted_data = extract_from_docx(file)
        else:
            return jsonify({"error": "Unsupported file type"}), 400

        resume = Resume(**extracted_data)
        db.session.add(resume)
        db.session.commit()
        return jsonify({"message": "Resume parsed and stored successfully"}), 201

api.add_resource(ResumeUpload, '/upload')

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
