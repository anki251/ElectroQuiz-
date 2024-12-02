import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

# Load quiz data from Excel file
def load_quiz_data(file_path):
    df = pd.read_excel(file_path)
    questions = df[['Questions', 'Option A', 'Option B', 'Option C', 'Option D']].values.tolist()
    answers = df['Answers'].values.tolist()
    return questions, answers

# Load data from your Excel file
file_path = 'quiz_data 1.xlsx'
questions, answers = load_quiz_data(file_path)

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x600")

        # Display Welcome Screen
        self.show_welcome_screen()

    def show_welcome_screen(self):
        # Load welcome background image
        self.bg_image = Image.open("2.jpeg")
        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.welcome_label = tk.Label(self.root, text="Welcome to Basic Electrical Quiz!", font=("Comic Sans MS", 24), bg="#FFFFFF")
        self.canvas.create_window(400, 150, window=self.welcome_label)

        self.start_button = tk.Button(self.root, text="Start Quiz", font=("Comic Sans MS", 16), command=self.start_game)
        self.canvas.create_window(400, 400, window=self.start_button)

    def start_game(self):
        self.welcome_label.destroy()
        self.start_button.destroy()
        self.canvas.destroy()
        
        # Load game background image
        self.bg_image = Image.open("4.jpeg")
        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.question_index = 0
        self.correct_answers = 0

        # Change the background to a light color and adjust the text color
        self.question_label = tk.Label(self.root, text="", font=("Comic Sans MS", 16), bg="#F0F0F0", fg="#000000")
        self.canvas.create_window(400, 50, window=self.question_label)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Comic Sans MS", 14), command=lambda idx=i: self.check_answer(idx))
            self.option_buttons.append(btn)
            self.canvas.create_window(400, 150 + i * 50, window=btn)

        self.show_question()

    def show_question(self):
        if self.question_index < len(questions):
            question = questions[self.question_index]
            self.question_label.config(text=question[0])
            for i in range(4):
                self.option_buttons[i].config(text=f"{chr(65 + i)}. {question[i + 1]}", bg="SystemButtonFace")
        else:
            self.end_game()

    def check_answer(self, idx):
        correct_idx = ord(answers[self.question_index]) - 65
        if idx == correct_idx:
            self.option_buttons[idx].config(bg="green")
            self.correct_answers += 1
        else:
            self.option_buttons[idx].config(bg="red")
            self.option_buttons[correct_idx].config(bg="green")
        
        self.question_index += 1
        self.root.after(1000, self.show_question)  # Show next question after 1 second

    def end_game(self):
        self.canvas.destroy()
        
        # Create a new canvas for the result display
        self.result_canvas = tk.Canvas(self.root, width=800, height=600, bg="#FFD700")
        self.result_canvas.pack(fill="both", expand=True)
        self.result_canvas.create_text(400, 200, text=f"Your Score: {self.correct_answers} out of {len(questions)}", font=("Comic Sans MS", 36), fill="#000080")
        self.result_canvas.create_text(400, 300, text="Thank you for playing this game!", font=("Comic Sans MS", 28), fill="#000080")

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
