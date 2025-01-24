# Interactive Quiz Application

This repository contains the code for the **Interactive Quiz Application**, a web-based platform that allows users to participate in interactive multiple-choice quizzes. The application includes features such as scoring, time limits, immediate feedback, and database-stored results under user accounts. Admins can manage quiz content via a dedicated panel, and a REST API is provided for integration.

---

## Project Overview

### Features:
- User authentication and session management.
- Interactive multiple-choice quizzes with scoring and feedback.
- Responsive design for all devices.
- Admin panel for managing quiz questions.
- REST API for exposing quiz questions for external integration.

### Technologies Used:
- **Backend:** Python (Flask/Django)
- **Frontend:** HTML, CSS
- **Database:** SQLite/PostgreSQL
- **Deployment:** Heroku
- **Tools:** GitHub, Trello, Postman

---

## Setup Instructions

### Prerequisites:
Ensure the following are installed on your system:
- Python 3.8+
- Git
- A PostgreSQL or SQLite database

### Steps to Set Up:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/interactive-quiz.git
   cd interactive-quiz
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Configure your database credentials in `settings.py` (Django) or `.env` (Flask).
   - Run migrations:
     ```bash
     python manage.py migrate  # For Django
     ```

5. Start the application:
   ```bash
   python manage.py runserver  # For Django
   flask run  # For Flask
   ```

6. Access the application at:
   ```
   http://127.0.0.1:8000/  # Default Django
   http://127.0.0.1:5000/  # Default Flask
   ```

---

## Usage Guidelines

### User Functions:
1. **Sign Up and Log In:**
   - Users must create an account to access quizzes.

2. **Take a Quiz:**
   - Select a quiz from the dashboard.
   - Answer multiple-choice questions within the time limit.
   - Submit answers to receive scores and feedback.

3. **View Results:**
   - Navigate to the Results Dashboard to view past scores and performance metrics.

### Admin Functions:
1. **Log In to the Admin Panel:**
   - Admin users can log in using their credentials.

2. **Manage Quiz Questions:**
   - Add, edit, or delete quiz questions.

3. **Access API:**
   - Use the REST API to expose quiz questions for external integration.

---

## Project Architecture

### Overview:
- **Backend:**
  - Handles business logic, authentication, session management, and API endpoints.
- **Frontend:**
  - Provides a responsive user interface for users and admins.
- **Database:**
  - Stores user data, quiz questions, and results.

### Architecture Diagram:
```
User <--> Frontend (HTML/CSS) <--> Backend (Flask/Django) <--> Database (SQLite/PostgreSQL)
                               ^
                               |
                        REST API (Integration)
```

### Folder Structure:
```
interactive-quiz/
├── app/
│   ├── templates/      # HTML templates
│   ├── static/         # CSS and JS files
│   ├── models.py       # Database models
│   ├── views.py        # Application logic
│   ├── api.py          # API endpoints
│   └── tests.py        # Unit tests
├── requirements.txt     # Dependencies
├── manage.py            # Entry point (Django)
├── app.py               # Entry point (Flask)
└── README.md            # Project documentation
```

---

## Next Steps

- Enhance quiz functionality with multimedia content (images/videos).
- Optimize API response time.
- Develop mobile applications for Android and iOS.

---

## Contributing

Feel free to contribute to this project by submitting pull requests. For major changes, please open an issue to discuss your ideas first.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
