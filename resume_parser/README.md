Resume Parser Application

Overview

This is a resume parsing application that extracts and processes information from resumes in various formats (PDF, DOCX). The application is containerized using Docker and can be deployed on any cloud service.

Features

- Resume Upload and Parsing
- Data Extraction (Name, Contact, Education, Experience, Skills)
- Database Storage (PostgreSQL)
- Simple React-based Frontend

Setup and Installation

Backend
1. Navigate to the `backend` directory.
2. Run `docker-compose up --build` to start the backend services.

 Frontend
1. Navigate to the `frontend` directory.
2. Run `npm install` to install dependencies.
3. Run `npm start` to start the React development server.

Deployment

To deploy the application on a cloud service like Paperspace:
1. Set up a machine with Docker installed.
2. Clone the repository.
3. Run `docker-compose up --build` to start the services.
