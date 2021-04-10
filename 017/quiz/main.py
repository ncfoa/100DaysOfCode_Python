from question_model import Question
# from data import question_data
from quiz_brain import Quiz
import random
import json
import requests

question_bank = []
num = random.randint(10, 20)  # Generate random number between 10 and 20 for questions received from API.
# Retreiving data from opentdb.com API
question_data = json.loads(requests.get(f"https://opentdb.com/api.php?amount={num}&difficulty=easy&type=boolean")
                           .text)["results"]
for item in question_data:
    q = item["question"]
    q = q.replace("&quot;", "'")
    q = q.replace("&#039;", "'")
    a = item["correct_answer"]
    newq = Question(q, a)
    question_bank.append(newq)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"You got {quiz.score} out of a possible {quiz.question_num} questions correct.")
