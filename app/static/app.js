/* app.js */
const questions = [
    {
        question: "What is the capital of France?",
        options: ["Paris", "London", "Berlin", "Madrid"],
        correct: 0
    },
    {
        question: "Which planet is known as the Red Planet?",
        options: ["Earth", "Mars", "Jupiter", "Venus"],
        correct: 1
    },
    {
        question: "What is the largest ocean on Earth?",
        options: ["Atlantic", "Indian", "Arctic", "Pacific"],
        correct: 3
    }
];

let currentQuestionIndex = 0;
let score = 0;

const questionEl = document.getElementById("question");
const optionsEl = document.getElementById("options");
const nextButton = document.getElementById("next-button");
const feedbackEl = document.getElementById("feedback");
const scoreSection = document.getElementById("score-section");
const scoreEl = document.getElementById("score");
const restartButton = document.getElementById("restart-button");

function loadQuestion() {
    const question = questions[currentQuestionIndex];
    questionEl.textContent = question.question;
    optionsEl.innerHTML = "";

    question.options.forEach((option, index) => {
        const li = document.createElement("li");
        const button = document.createElement("button");
        button.textContent = option;
        button.onclick = () => checkAnswer(index);
        li.appendChild(button);
        optionsEl.appendChild(li);
    });

    feedbackEl.textContent = "";
    nextButton.disabled = true;
}

function checkAnswer(selected) {
    const correct = questions[currentQuestionIndex].correct;
    feedbackEl.textContent = selected === correct ? "Correct!" : "Wrong!";
    if (selected === correct) {
        score++;
    }
    nextButton.disabled = false;
}

function nextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        loadQuestion();
    } else {
        showScore();
    }
}

function showScore() {
    scoreSection.hidden = false;
    scoreEl.textContent = score;
    document.getElementById("quiz-section").hidden = true;
}

function restartQuiz() {
    score = 0;
    currentQuestionIndex = 0;
    scoreSection.hidden = true;
    document.getElementById("quiz-section").hidden = false;
    loadQuestion();
}

nextButton.addEventListener("click", nextQuestion);
restartButton.addEventListener("click", restartQuiz);

loadQuestion();
