import requests
import html
import tkinter as tk
from tkinter import ttk

# taking data from API, https://opentdb.com/
trivia_response = requests.get(url="https://opentdb.com/api.php?amount=15&category=22&type=boolean")
trivia_response.raise_for_status()

# game instances
in_list_question_number = 0
question_number = in_list_question_number + 1
answer = False
score = 0


# start the game
def start_game():
    global in_list_question_number
    q_text = html.unescape(trivia_response.json()['results'][in_list_question_number]['question'])
    question.config(text=q_text)


def next_question_true():
    global in_list_question_number
    global question_number
    global score

    q_answer = trivia_response.json()['results'][in_list_question_number]['correct_answer']
    if q_answer == "True":
        in_list_question_number += 1
        question_number += 1
        score += 1
        q_text = html.unescape(trivia_response.json()['results'][in_list_question_number]['question'])
        question.config(text=q_text)
        score_board.config(text=f"Score: {score}")
    else:
        question.config(text="Your answer was incorrect!!", fg="red")
        button_true.destroy()
        button_false.destroy()


def next_question_false():
    global in_list_question_number
    global question_number
    global score

    q_answer = trivia_response.json()['results'][in_list_question_number]['correct_answer']
    if q_answer == "False":
        in_list_question_number += 1
        question_number += 1
        score += 1
        q_text = html.unescape(trivia_response.json()['results'][in_list_question_number]['question'])
        question.config(text=q_text)
        score_board.config(text=f"Score: {score}")
    else:
        question.config(text="Your answer was incorrect!!", fg="red")
        button_true.destroy()
        button_false.destroy()


# GUI with tkinter
# Create the main window
root = tk.Tk()
root.title("Quiz Now!")
root.config(bg="#EAD9EB")
root.minsize(500, 500)

# Create a style object
style = ttk.Style()

# Configure the style for the buttons
style.configure("TButton", padding=2, relief="flat",
                background="#0078d7", foreground="purple",
                font=("Arial", 12, "bold"))

score_board = tk.Label(root, text=f"Score: {score}", font=("Arial", 18), fg="purple", bg="#EAD9EB")
score_board.grid(row=0, column=1, padx=50, pady=10)

question = tk.Label(root, text="", font=("Arial", 18), fg="purple", bg="#EAD9EB")
question.grid(row=1, column=1, padx=50, pady=100)
start_game()

# Create the first button
button_true = ttk.Button(root, text="True", command=next_question_true)
button_true.grid(row=2, column=0, padx=25, pady=50)

# Create the second button
button_false = ttk.Button(root, text="False", command=next_question_false)
button_false.grid(row=2, column=2, padx=25, pady=50)


# Start the main loop
root.mainloop()

