# SOC Project Management Webpage

This is a web application for managing System-on-a-Chip (SOC) projects, with a focus on the verification process.

## Features
- Project Management
- Release Version Monitoring
- Test Plan Upload and Management
- Test Case Creation and Tracking
- Bug Management
- REST API for all resources

## Technology Stack
- **Backend:** Python, Django, Django REST Framework
- **Frontend:** JavaScript, React

## How to Run

### Backend (Django)
1.  Navigate to the `backend` directory: `cd backend`
2.  Install Python dependencies: `pip install -r requirements.txt`
3.  Apply database migrations: `python manage.py migrate`
4.  Run the development server: `python manage.py runserver`
5.  The backend API will be available at `http://localhost:8000/api/`.

### Frontend (React)
1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install Node.js dependencies: `npm install`
3.  Run the development server: `npm start`
4.  The frontend will be available at `http://localhost:3000`. It is pre-configured to proxy API requests to the backend on port 8000.
