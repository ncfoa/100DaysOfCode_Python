# Question Class for quiz app
from html import unescape


class Question:

    def __init__(self, q_text, q_answer):
        self.question = unescape(q_text)
        self.answer = q_answer


