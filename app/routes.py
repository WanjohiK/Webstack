from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User, Quiz, Question, QuizResult
from app.forms import RegistrationForm, LoginForm
import random

# Define the auth blueprint for authentication routes
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.quiz'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.quiz'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.quiz'))  # Redirect to quiz page after successful login
        flash('Login failed. Check email and password.', 'danger')
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Define a new main blueprint for non-authentication routes (e.g., home and quizzes)
main = Blueprint('main', __name__)

@main.route('/')
def home():
    quizzes = Quiz.query.all()
    return render_template('home.html', quizzes=quizzes)

@main.route('/quiz')
@login_required
def quiz():
    # Fetch all quizzes for the logged-in user
    quizzes = Quiz.query.all()
    if quizzes:
        # Redirect to the first quiz if quizzes exist
        return redirect(url_for('main.start_quiz', quiz_id=quizzes[0].id))
    flash('No quizzes available!', 'warning')
    return render_template('no_quiz.html')

@main.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def start_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)  # Fetch the quiz by its ID
    questions = Question.query.filter_by(quiz_id=quiz.id).all()  # Fetch all questions for the quiz

    # Manage session state to track the current question and score
    if 'question_index' not in session:
        session['question_index'] = 0
        session['score'] = 0

    question_index = session['question_index']

    # Check if it's the last question
    is_last_question = question_index == len(questions) - 1

    # If all questions are answered, calculate the final score and percentage
    if question_index >= len(questions):  
        score = session['score']
        percentage = (score / len(questions)) * 100  # Calculate percentage

        # Save the quiz result
        result = QuizResult(
            user_id=current_user.id, 
            quiz_id=quiz.id, 
            score=score, 
            percentage=percentage  # Store the percentage
        )
        db.session.add(result)
        db.session.commit()

        # Clear session
        session.pop('question_index', None)
        session.pop('score', None)

        flash(f'You completed the quiz! Your score: {score}/{len(questions)} ({percentage:.2f}%)', 'success')
        return redirect(url_for('main.quiz_results', quiz_id=quiz.id))

    question = questions[question_index]

    # Handle POST request: Check answer and move to next question
    if request.method == 'POST':
        selected_answer = request.form.get('answer')

        # Debugging: Log the selected answer, correct answer, and current score
        print(f"Selected Answer: {selected_answer}, Correct Answer: {question.correct_answer}, Current Score: {session['score']}")

        # Only update the score if the selected answer is correct
        if selected_answer == question.correct_answer:
            session['score'] += 1  # Increment score only if the answer is correct
            print(f"Score incremented! New Score: {session['score']}")

        # Move to next question
        session['question_index'] += 1
        return redirect(url_for('main.start_quiz', quiz_id=quiz.id))

    # Render the quiz with the current question and quiz progress
    return render_template('quiz.html', 
                           quiz=quiz, 
                           question=question, 
                           question_number=question_index + 1, 
                           total_questions=len(questions),
                           is_last_question=is_last_question)



@main.route('/quiz/<int:quiz_id>/results', methods=['GET'])
@login_required
def quiz_results(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)  # Fetch the quiz by its ID
    
    # Query the most recent quiz result for the current user and quiz
    result = QuizResult.query.filter_by(user_id=current_user.id, quiz_id=quiz.id).order_by(QuizResult.completed_at.desc()).first_or_404()
    
    return render_template('quiz_results.html', quiz=quiz, score=result.score, percentage=result.percentage)


@main.route('/quiz/<int:quiz_id>/abandon', methods=['GET'])
@login_required
def abandon_quiz(quiz_id):
    # You can add logic to handle abandonment here.
    # For example, you can redirect to the home page or show a message.
    flash("You abandoned the quiz.", "info")
    return redirect(url_for('main.home'))  # Redirect to the home page or quiz list