

from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

questions = {
    "Python": [
        ("Which module is used in python for GUI?", ['Scilearn', 'Pandas', 'Tkinter', 'NumPy'], "Tkinter"),
        ("Is python an Object Oriented Language?", ["Yes","No"], "Yes"),
        ("Python was first introduced in", ['1997', '1991', '2024', '1800'], "1991"),
        ("Which of the following character \n is used to give single-line comments in Python",["//", "#", "!", "/*"],"#"),
        ("Who developed Python Programming Language", ["Wick van Rossum" ,"Rasmus Lerdorf","Guido van Rossum","Niene Stom"],"Guido van Rossum"),
        ("Which of the following functions can \n help us to find the version of python \n that we are currently working on",[ "sys.version(1)", "sys.version(0)" ,"sys.version()" ,"sys.version"],"sys.version"),
    ],
    "Physics": [
        ("What is the chemical symbol for water?", ["H2O", "CO2", "NaCl", "O2"], "H2O"),
        ("Who proposed the theory of relativity?", ["Newton", "Einstein", "Bohr", "Curie"], "Einstein"),
        ("What is the speed of light?", ["299792 km/s", "500000 km/s", "1000000 km/s", "2000000 km/s"], "299792 km/s"),
    ],
    """_summary_
    """        "Cricket": [
        ("Name International body that manages cricket mathches\n around the globe :", ["ICC", "BCCI", "PCB", "ACB"], "ICC"),
        ("Name the last indian bowler to take wicket in t20\n internationl semifinals:", ["Virat kohli", "Jasprit", "Nehra", "Curie"], "Virat kohli"),
        ("Who is the only cricketer to score 50 ODI centuries?", ["KOHLI", "DHONI", "ROHIT","SACHIN TENDULKAR",], "KOHLI"),
    ],
}

question_number = 0
correct_answers = 0

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

def check_answer():
    global correct_answers
    subject = menu.get()
    subject_questions = questions[subject]
    _, _, correct_answer = subject_questions[question_number]
    if v.get() == correct_answer:
        correct_answers += 1

def next_question():
    global question_number
    check_answer()
    question_number += 1
    start_quiz()

def start_quiz():
    clear_frame()

    subject = menu.get()
    subject_questions = questions[subject]

    if question_number < len(subject_questions):
        question, options, correct_answer = subject_questions[question_number]

        question_label = ctk.CTkLabel(f1, text=question,font=("times new roman",22))
        question_label.grid()

        v.set(None)
        for option in options:
            rb = ctk.CTkRadioButton(f1, text=option, variable=v, value=option,font=("times new roman",20),hover_color="#004d00")
            rb.grid()

        next_button.grid(row=7,column=1)
    else:
        total_questions = len(subject_questions)
        result_label = ctk.CTkLabel(f1,font=("times new roman",20), text=f"You have answered {correct_answers} questions correctly out of {total_questions} questions.\n Thank you for participating!")
        result_label.place(relx=0.5, rely=0.5, anchor='center')
        next_button.grid_remove()

root=ctk.CTk()
root.title("Intellect Arena:Battle of the Brains")
root.geometry('900x550')

ctk.CTkLabel(root, text="Intellect Arena", padx=10, pady=9, font=("times new roman",25)).grid(row=0,column=0)

f1 = ctk.CTkFrame(root, bg_color="black", width=650, height=450)
f1.grid(row=1,column=1)
f1.grid_propagate(0)

subjects=["Python","Physics","Cricket"]

menu=ctk.CTkSegmentedButton(f1, values=subjects,width=100,height=40)
menu.place(relx=0.5, rely=0.5, anchor='center')

startbutton=ctk.CTkButton(f1, text="Start", command=start_quiz)
startbutton.place(relx=0.5, rely=0.6, anchor='center')

v = StringVar()
next_button = ctk.CTkButton(root, text="Next Question", command=next_question)

switch_var=ctk.IntVar(value=0)

def lightmode():
    if switch_var.get()==1:
        ctk.set_appearance_mode("light")
    elif switch_var.get()==0:
        ctk.set_appearance_mode("dark")

ctk.CTkSwitch(root, onvalue=1, offvalue=0, text="Switch to light mode", command=lightmode, variable=switch_var).place(relx=0.75,rely=0.03)

root.mainloop()
