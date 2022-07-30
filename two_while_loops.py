# This file will be dedicated to using two while loops to run the whole program and see what becomes of it.
from tkinter import *
from time import *
from threading import Thread
# Options
# TODO 0: Fix the tick label first, DONE
# TODO 1: DONE, Try and figure out why the recursion doesn't work properly when the window.update()-(use update_idle() which is a lot better) is included inside the work part i.e. why isn't the break part being expressed
# So to do this part my idea is to set the countdown using after method inside a start countdown method and in this method also starting the timer mechanism with the same button and even destroying and starting the whole UI using after methodand we can basically use the mainloop to continually check if the value of self.reset has changed. And so we will be able to update and therefore reset the whole window including the frame or any other widget.
# TODO 2:Hopefully done soon,  Use bind to get around this problem
# TODO 3:We will see,  Use threading.event
# TODO 4: DONE, Use "with open as"
# TODO 5: DONE, Regardless try your best to solve this problem with only Todo 1.
# TODO Tip: Will be done soon, possibly, hopefully, Use a combination of TODO 2,3 and 6 to achieve a very seamless and perfectly functioning program.
# TODO 6: This doesn't really work, sorry, Try using the App class method and try sending from the main to the thread mainloop
# TODO 7:Will take some time,  Add the pause functionality, when pressing the start button twice and if pressed again it would function like the play button. so if button is pressed i.e. button_pressed%2==0
# TODO 8: Easily DONE, Don't let pressing start once the program has started have any effects, basically make it unfunctional except for when starting the program from the beginning or reset.
# TODO 9: DONE, Instead of using the after callback instead use the OS time to keep track of the countdown and also manage the transition between Work and Break because you don't want your time to be fast or slow depending on other processes, if we want a program that is efficient we want to tie it to the OS Kernel time.
# TODO 10:DONE, ADD SOUND, for notification puposes! if possible let it have its own administrative access for sound where it uses maximum volume to notify. This part might be a little too advanced but this is the beauty of programming, the hill, feel me!
# Improvement for "todo 9, kinda done, not the sound part, if you can't another very specific os timer just use time.time() function and make it work and also make your application use sound
# TODO 11:(Will do almost already done, ez, I don't see the applicability- actually instead ask the user if they want to stop or start another round of the timer) ADD STOP/END feature when the app ends for a small amount of time, and on top of that try removing the last break and replace it with the end/stop feature.
# TODO 12:(Tried my best, except for the fact that I haven't tried any of the threading, event or binding strategies just yet) Make sure this program uses as minimum of resources as possible, make sure it doesn't heavily interfere with other apps and your os as much as possible. Either find a data sturcture that is more efficient than a list or update the strategy you are using to count. Maybe threading or binding might fix it all.


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60

# This file will also be an attempt to not use any global or list values.
# you might try the technique of self-reference when implementing the after method but once you get done with the execute-mirror/bounce strategy.
# this is literally the same thing as extra-transition, while extra-transition is recursive we want to make this more of a loop which the two are basic two ways of doing the same thing, they are basically the same thing by the end of the day.

# this is literally the same thing AGHHHHHHHH!!!!!!! This is probably how Angela would have wanted me to do it.
beginning = True


while beginning==True:
    start_work = [time()]
    i=[4]

    identifier="Work"
    with open("button_click", mode="w") as button:
        button.write("Not Clicked")


    def button_click():
        with open("button_click", mode="w") as writer:
            writer.write("Clicked")


    def timer_mechanism(identifier, value, dif):
        minute = 0
        print(i)
        value = int(value)
        counter = int(value - dif)
        print(dif, "CLOCK DIFFERENCE BETWEEN START AND END")
        print(value)
        print(counter)

        if identifier == "Work":
         if int(dif)==0:
            timer.config(text="Work", fg=GREEN)

         elif int(dif)==int(value):
             if i[0] == 4:
                 global frame
                 frame = Frame(window, width=20, height=20, bg=YELLOW)
                 frame.grid(row=3, column=1)
             tick = Label(frame, text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
             tick.bell()
             tick.pack(side=LEFT)
             window.deiconify()
             window.attributes("-topmost", 1)
             window.attributes("-topmost", 0)



        elif (identifier == "Break" or identifier == "Long Break") :
         if int(dif)==0:
            print(dif, "IT AIN'T MFING ", 0, "SO SHUSH PLEASE!!!")
            if identifier=="Break":
                timer.config(text="Break", fg=PINK)
            elif identifier=="Long Break":
                timer.config(text="Break",fg=RED)
         if int(dif)==int(value):
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
            execute(WORK_MIN, "Work")

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
                window.bell()
                start_countdown()





    def close():
        global beginning
        beginning = False
        window.destroy()

    print(beginning)

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

