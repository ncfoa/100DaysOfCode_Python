
class Quiz:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        ans = input(f"Q.{self.question_num }: {question.question} True or False?: ")
        self.check_answer(ans, question.answer)

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, ans, answer):
        if ans.lower() != "true" and ans.lower() != "false":
            print("Invalid Answer. You must type 'True' or 'False' Ending Quiz.")
            exit(1)
        if ans.lower() == answer.lower():
            self.score += 1
            print("Your answer is correct!")
        else:
            print("Sorry, incorrect answer.")
            print(f"The correct answer was: {answer}")
        print(f"Your current score is {self.score}/{self.question_num}\n")
