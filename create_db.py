from app import create_app, db
from app.models import User, Quiz, Question, QuizResult

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables created successfully!")
