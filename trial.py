
from tkinter import *
from time import *
from threading import Thread


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25*60
SHORT_BREAK_MIN = 0.125*60
LONG_BREAK_MIN = 0.25*60

def start_it():
    print("started")
def button_click():
    print("reset")

window = Tk(className="Pomodoro")
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

global timer
timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, foreground=GREEN)
timer.grid(row=0, column=1)
global canvas
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato)
global clock_counter
clock_counter = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", highlightthickness=0, borderwidth=0, command=lambda: start_it())
start.grid(row=2, column=0)
end = Button(text="Reset", highlightthickness=0, borderwidth=0, command=button_click)
end.grid(row=2, column=2)
window.deiconify()
window.attributes("-topmost", 1)
window.mainloop()