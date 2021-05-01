from data import question_data
from quiz_brain import Quiz
from ui import QuizUI

question_bank = question_data

quiz = Quiz(question_bank)
quiz_ui = QuizUI(quiz)

