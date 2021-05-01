
class Quiz:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
        self.question = {}

    def next_question(self):
        self.question = self.question_list[self.question_num]
        self.question_num += 1
        return f"{self.question.question}"

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, ans):
        correct_answer = self.question.answer
        if ans == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
