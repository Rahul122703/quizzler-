
from tkinter import *
import html
THEME_COLOR = "#375362"

class QuizGUI:
    def __init__(self, question_bank):
        self.score = 0
        self.question_bank = question_bank
        self.qno = 0

        self.window = Tk()
        self.window.title("QUIZZLER")
        self.window.config(bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)

        self.score_label = Label(text=f"Score : {self.score}", bg=THEME_COLOR, fg="white", font=("arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.question_text = self.canvas.create_text(150, 125, width=280, text=f"", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        right_image = PhotoImage(file=r"Quizzler\true.png")
        self.true_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=self.right_pressed)
        self.true_button.grid(row=2, column=0, pady=30)

        wrong_image = PhotoImage(file=r"Quizzler\false.png")
        self.false_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=self.wrong_pressed)
        self.false_button.grid(row=2, column=1, pady=30)
        self.ask_question()
        self.window.mainloop()

    def right_pressed(self):
        self.check_answer("True")

    def wrong_pressed(self):
        self.check_answer("False")

    def change_canvas_color(self, answer):
        if answer == "True":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def check_answer(self, button):
        if self.question_bank[self.qno-1]['correct_answer'] == button:
            self.score += 1
            self.score_label.config(text=f"Score : {self.score}")
            self.change_canvas_color("True")
        else:
            self.change_canvas_color("False")
        self.window.after(1000, self.ask_question)

    def ask_question(self):
        if self.qno+1 <= len(self.question_bank):
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Q.{self.qno + 1}){html.unescape(self.question_bank[self.qno-1]['question'])}")
            self.qno += 1
        else:
            self.canvas.itemconfig(self.question_text, text="THE END")
































