from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Some Question Text",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  command=self.check_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,
                                   command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            # print(q_text)
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="Congrats!\nYou have finished the quiz.",
                                   fill=THEME_COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.feedback(self.quiz.check_answer("True"))
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def check_false(self):
        self.feedback(self.quiz.check_answer("False"))
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def feedback(self, is_right):
        if is_right:
            bg_color = "green"
        else:
            bg_color = "red"
        self.canvas.itemconfig(self.question_text, fill="white")
        self.canvas.config(bg=bg_color)
        self.window.after(150, self.get_next_question)
