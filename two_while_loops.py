# This file will be dedicated to using two while loops to run the whole program and see what becomes of it.
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

# This file will also be an attempt to not use any global or list values.
# you might try the technique of self-reference when implementing the after method but once you get done with the execute-mirror/bounce strategy.
# this is literally the same thing as extra-transition, while extra-transition is recursive we want to make this more of a loop which the two are basic two ways of doing the same thing, they are basically the same thing by the end of the day.

# this is literally the same thing AGHHHHHHHH!!!!!!! This is probably how Angela would have wanted me to do it.
beginning = True


end_window=False
while beginning==True:
    start_work = [time()]
    i=[4]
    identifier="Work"
    with open("button_click", mode="w") as reset:
        reset.write("Not Clicked")


    def button_click():
        with open("button_click", mode="w") as reset:
            reset.write("Clicked")


    def timer_mechanism(identifier, value, dif):
        minute = 0
        print(i)
        value = int(value)
        counter = int(value - dif)
        print(dif, "CLOCK DIFFERENCE BETWEEN START AND END")
        print(value)
        print(counter)

        if identifier == "Work" and int(dif) == 0:

            timer.config(text="Work", fg=GREEN)
            window.deiconify()
            window.attributes("-topmost", 1)
            window.attributes("-topmost", 0)

        elif (identifier == "Break" or identifier == "Long Break") and int(dif) == 0:
            print(dif, "IT AIN'T MFING ", 0, "SO SHUSH PLEASE!!!")
            timer.config(text="Break", fg=PINK)

            if i[0] == 4:
                global frame
                frame = Frame(window, width=20, height=20)
                frame.grid(row=3, column=1)

            tick = Label(frame, text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
            tick.pack(side=LEFT)
            window.deiconify()
            window.attributes("-topmost", 1)
            window.attributes("-topmost", 0)
        if counter < 60 :
            if counter / 1 < 10:
                canvas.itemconfig(clock_counter, text=(f"00:0{int(counter / 1)}"))
                canvas.update_idletasks()
            elif counter / 1 >= 10:
                canvas.itemconfig(clock_counter, text=(f"00:{int(counter / 1)}"))
                canvas.update_idletasks()
        elif counter >= 60 :

            transition = int(counter / 1)
            while transition >= 60:
                minute += 1
                transition -= 60

            second = transition
            if second < 10 and minute < 10:
                canvas.itemconfig(clock_counter, text=(f"0{minute}:0{second}"))
                canvas.update_idletasks()
            elif second >= 10 and minute < 10:
                canvas.itemconfig(clock_counter, text=(f"0{minute}:{second}"))
                canvas.update_idletasks()
            elif minute >= 10 and second < 10:
                canvas.itemconfig(clock_counter, text=(f"{minute}:0{second}"))
                canvas.update_idletasks()
            else:
                canvas.itemconfig(clock_counter, text=(f"{minute}:{second}"))
                canvas.update_idletasks()


    def start_countdown():
        with open("button_click") as reset:
            timer_reset = reset.read()
        start_work[0] = time()
        if timer_reset != "Clicked" and i[0] > 0:

            # keep listening to the function that receives from the button while doing an after for the 25 min and 10 min respectively.3

            # the solution to this problem is to break up the after process instead of doing it all at the same time make use of small increments so that this after could finish withing a second or two and then go to another function that contains all the timer_reset.click values update and come everytime until we reach a limit somewhere probably an array value that will be updated until we get to the 25 minute mark so this insures as the signal from the button will be accepted.
            execute(WORK_MIN,"Work")

            # start=time()
            # end=time()
            # while end-start<5:
            #     end=time()
            #     timer_reset.click=timer_reset.timer_command()

        else:
            window.destroy()


    def rest():

        with open("button_click") as reset:
            timer_reset = reset.read()
        print(timer_reset, "DEBUG")
        start_work[0] = time()
        if timer_reset == "Not Clicked":
            print(i[0])
            if i[0] > 1:

                execute(SHORT_BREAK_MIN,"Break")
            elif i[0] == 1:
                execute(LONG_BREAK_MIN,"Long Break")



            else:
                print("DESTRUCTION")
                window.destroy()


        else:
            print("DESTRUCTION!!!!!")
            window.destroy()

        i[0] -= 1
        print(i)
        print(start_work)


    def execute(value,identifier):
        print("WHATEVER, JUST PLEASE WORK!")
        value = int(value)
        with open("button_click") as reset:
            timer_reset = reset.read()
        print(timer_reset, "DEBUG2!!!")
        end = time()
        counter_dif = int(end - start_work[0])
        print(int(value), "EVERY STEP OF THE WAY!")
        if timer_reset == "Clicked":
            window.destroy()
        elif counter_dif <value+1:  # elif counter[0]>=1:
            print("this is working too")
            timer_mechanism(identifier=identifier, value=value, dif=counter_dif)
            # print(button_click)
            if identifier == "Work":

                window.after(1000, execute, WORK_MIN, identifier)

            if identifier == "Break":
                print("working at some point")
                print(i)
                print(start_work)
                window.after(1000, execute, SHORT_BREAK_MIN, identifier)
            if identifier == "Long Break":
                window.after(1000, execute, LONG_BREAK_MIN, identifier)
        elif counter_dif >= value+1:  # elif counter[0]<1:
            print(counter_dif, "=", int(value), "AT THIS POINT!")


            if identifier == "Work":
                # if i[0]==1:
                #     counter[0]=LONG_BREAK_MIN
                # else:
                #     counter[0] = SHORT_BREAK_MIN
                rest()
            if identifier == "Break" or identifier == "Long Break":
                # counter[0] = WORK_MIN
                start_countdown()





    def close():
        global beginning
        beginning = False
        window.destroy()

    print(beginning)
    print(end_window)
    window = Tk(className="Pomodoro")
    window.title("Pomodoro")
    window.config(pady=50, padx=100, bg=YELLOW)

    window.protocol("WM_DELETE_WINDOW",close)


    timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, foreground=GREEN)
    timer.grid(row=0, column=1)

    canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
    tomato = PhotoImage(file="tomato.png")
    canvas.create_image(100, 100, image=tomato)

    clock_counter = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)

    start = Button(text="Start", highlightthickness=0, borderwidth=0, command=start_countdown)
    start.grid(row=2, column=0)
    end = Button(text="Reset", highlightthickness=0, borderwidth=0, command=button_click)
    end.grid(row=2, column=2)
    window.deiconify()
    window.attributes("-topmost", 1)
    window.update()





    window.mainloop()

