from tkinter import *
from quiz_brain import QuizBrain

BG_COLOR = "#54BAB9"
CVS_COLOR = "#FBF8F1"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Dumb or Clever?")
        self.window.config(bg=BG_COLOR, padx=30, pady=30)

        # wynik
        self.score_lbl = Label(text=f"Score: 0", font=("Droid", 12, "bold"), bg=BG_COLOR)
        self.score_lbl.grid(row=0, column=1, sticky="NE", pady=(0, 15))

        # tekst na cnavas
        self.canvas = Canvas(width=300, height=400, bg=CVS_COLOR, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question = self.canvas.create_text(150, 200, text="Tutaj bedzie pytanie", width=300, font=("Droid", 20, "normal"))

        # Przyciski
        self.right_img = PhotoImage(file="./images/button_true-1.png")
        self.right_btn = Button(image=self.right_img, command=self.answer_true)
        self.right_btn.config(highlightthickness=0, bg=BG_COLOR, activebackground=BG_COLOR, bd=0, relief="flat")
        self.right_btn.grid(row=2, column=0, pady=(20, 0), padx=(0, 10))

        self.wrong_img = PhotoImage(file="./images/button_false.png")
        self.wrong_btn = Button(image=self.wrong_img, command=self.answer_false)
        self.wrong_btn.config(highlightthickness=0, bg=BG_COLOR, activebackground=BG_COLOR, bd=0, relief="flat")
        self.wrong_btn.grid(row=2, column=1, pady=(20, 0))

        self.ui_next_question()
        self.window.mainloop()

    def ui_next_question(self):
        self.canvas.config(bg=CVS_COLOR)
        if self.quiz.still_have_question():
            self.score_lbl.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You finished the quiz")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#2EB086")
        else:
            self.canvas.config(bg="#B33030")
        self.window.after(1000, self.ui_next_question)

