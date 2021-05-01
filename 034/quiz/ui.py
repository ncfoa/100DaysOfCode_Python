from tkinter import *
from quiz_brain import Quiz
THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        self.w = Tk()
        self.w.title("Do You Know?")
        self.w.config(bg=THEME_COLOR, padx=20, pady=20)
        self.c = Canvas(width=300, height=250, bg="white")
        self.question_text = self.c.create_text(150, 125, width=250, text="", fill=THEME_COLOR,
                                                font=("Ariel", 20, "italic"))
        self.c.grid(column=0, row=1, columnspan=2, sticky="WE", pady=30)
        f_img = PhotoImage(file="../images/false.png")
        t_img = PhotoImage(file="../images/true.png")
        self.true = Button(image=t_img, bd=0, bg=THEME_COLOR, highlightthickness=0, command=self.answer_true)
        self.true.grid(column=0, row=2)
        self.false = Button(image=f_img, bd=0, bg=THEME_COLOR, highlightthickness=0, command=self.answer_false)
        self.false.grid(column=1, row=2)
        self.text = Label(bg=THEME_COLOR, fg="white", font=("Ariel", 15, "normal"), text=f"Score: {self.quiz.score}\n")
        self.text.grid(column=1, row=0)
        self.get_next_question()

        self.w.mainloop()

    def get_next_question(self):
        self.c.config(bg="white")
        if self.quiz.still_has_questions():
            qt = self.quiz.next_question()
            self.c.itemconfigure(self.question_text, text=qt)
        else:
            self.true.config(state=DISABLED)
            self.false.config(state=DISABLED)
            self.c.itemconfigure(self.question_text, text=f"You got {self.quiz.score} right out of"
                                                          f" {len(self.quiz.question_list)}")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.c.config(bg="green")
            self.text.config(text=f"Score: {self.quiz.score}\n")
        else:
            self.c.config(bg="red")

        self.c.after(1000, func=self.get_next_question)
