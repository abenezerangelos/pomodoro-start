#This is the clean finished version of the pause_function implementation.

from tkinter import *
from time import *

from threading import Thread

# Options
# TODO 0: Fix the tick label first, DONE
# TODO 1: DONE, Try and figure out why the recursion doesn't work properly when the window.update()-(use update_idle() which is a lot better) is included inside the work part i.e. why isn't the break part being expressed
# So to do this part my idea is to set the countdown using after method inside a start countdown method and in this method also starting the timer mechanism with the same button and even destroying and starting the whole UI using after methodand we can basically use the mainloop to continually check if the value of self.reset has changed. And so we will be able to update and therefore reset the whole window including the frame or any other widget.
# TODO 2: Use bind to get around this problem
# TODO 3: Use threading.event
# TODO 4: DONE, Use "with open as"
# TODO 5: DONE, Regardless try your best to solve this problem with only Todo 1.
# TODO Tip: Use a combination of TODO 2,3 and 6 to achieve a very seamless and perfectly functioning program.
# TODO 6: Try using the App class method and try sending from the main to the thread mainloop
# TODO 7: Add the pause functionality, when pressing the start button twice and if pressed again it would function like the play button. so if button is pressed i.e. button_pressed%2==0
# TODO 8: Don't let pressing start once the program has started have any effects, basically make it unfunctional except for when starting the program from the beginning or reset.
# TODO 9: DONE, Instead of using the after callback instead use the OS time to keep track of the countdown and also manage the transition between Work and Break because you don't want your time to be fast or slow depending on other processes, if we want a program that is efficient we want to tie it to the OS Kernel time.
# TODO 10: ADD SOUND, for notification puposes! if possible let it have its own administrative access for sound where it uses maximum volume to notify. This part might be a little too advanced but this is the beauty of programming, the hill, feel me!
# Improvement for "todo 9, kinda done, not the sound part, if you can't another very specific os timer just use time.time() function and make it work and also make your application use sound
# TODO 11:(Will do almost already done, ez, I don't see the applicability- actually instead ask the user if they want to stop or start another round of the timer) ADD STOP/END feature when the app ends for a small amount of time, and on top of that try removing the last break and replace it with the end/stop feature.
# TODO 12:(Tried my best, except for the fact that I haven't tried any of the threading, event or binding strategies just yet) Make sure this program uses as minimum of resources as possible, make sure it doesn't heavily interfere with other apps and your os as much as possible. Either find a data sturcture that is more efficient than a list or update the strategy you are using to count. Maybe threading or binding might fix it all.
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60


# class Reset:
#     def __init__(self):
#         self.click = False
#         self.activation = False
#
#     def button_command(self):
#         self.click = True
#
#     def timer_command(self):
#         return self.click


# ---------------------------- TIMER RESET ------------------------------- #
# timer_reset = Reset()
# reset = timer_reset.click
start_work=[time()]
with open("button_click",mode="w") as reset:
    reset.write("Not Clicked")
def button_click():
    with open("button_click",mode="w")as reset:
        reset.write("Clicked")


# ---------------------------- TIMER MECHANISM ------------------------------- #
from winsound import *
# ichecker = False # should be deprecated, not necessarily useful given the fact that you can just use the time to check if it was the start and then activate based on that.

deiconifier=0
def timer_mechanism(identifier,value,dif):
    minute=0

    value=int(value)
    counter=int(value-dif)

    global rest_pause
    global only_once

    if identifier=="Work" and int(dif)==0 :

        timer.config(text="Work", fg=GREEN)
        global deiconifier
        if deiconifier>10:
            window.deiconify()
            window.attributes("-topmost", 1)
            window.attributes("-topmost", 0)
        deiconifier+=1
    elif (identifier=="Break" or identifier=="Long Break") and only_once==True:
        if identifier=="Break":
            timer.config(text="Break", fg=PINK)

        if identifier=="Long Break":
            timer.config(text="Break", fg=RED)
        if i[0]==3:
            global frame
            frame = Frame(window, width=20, height=20)
            frame.grid(row=3, column=1)
            keeper=[Frame]
        tick = Label(frame, text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
        MessageBeep(MB_ICONEXCLAMATION)
        tick.pack(side=LEFT)
        window.deiconify()
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        only_once=False
        # ichecker=False

    if counter<60 :
      if counter/1<10:
        canvas.itemconfig(clock_counter, text=(f"00:0{int(counter/1)}"))
        canvas.update_idletasks()
      elif counter/1>=10:
          canvas.itemconfig(clock_counter, text=(f"00:{int(counter / 1)}"))
          canvas.update_idletasks()


    elif counter>=60 :

            transition=int(counter/1)
            while transition>=60:
                minute+=1
                transition-=60


            second=transition
            if second<10 and minute<10:
                canvas.itemconfig(clock_counter,text=(f"0{minute}:0{second}"))
                canvas.update_idletasks()
            elif second>=10 and minute<10:
                canvas.itemconfig(clock_counter,text=(f"0{minute}:{second}"))
                canvas.update_idletasks()
            elif minute>=10 and second<10:
                canvas.itemconfig(clock_counter, text=(f"{minute}:0{second}"))
                canvas.update_idletasks()
            else:
                canvas.itemconfig(clock_counter,text=(f"{minute}:{second}"))
                canvas.update_idletasks()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# class Work(Thread):
#    def run(self):
#        for i in range(4):
#          print("!!!!")
#          timer.config(text="Work",fg=GREEN)
#          start=int(time())
#          window.update()
#          end=int(time())
#          while end-start<3:
#            end=time()
#
#          Break().run()
#
#
#          if i == 1:
#              return "exit"
#
#
#
# array=[1]
#
# class Break(Thread):
#    def run(self):
#
#       print("$$$$$$    ")
#       timer.config(text="Break",fg=PINK)
#       test=Frame(width = 100,height=50,bg=YELLOW)
#       test.grid(row=3,column=1)
#       Label(test,text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN,padx=3).pack(in_=test,side=LEFT)
#
#       start = int(time())
#       end = int(time())
#       while end - start < 1:
#         end = time()
#
#
#
#       array[0]+=1
#
#
# def start_countdown():
#
#     print("Ok")
#     work=Work()
#     work.start()
#     work.join()
#     #needs to wait until the iteration is done
#     beginning()


# def start_countdown():
#  global reset
#  reset = False
#
#  global frame
#  frame = Frame(window, width=20, height=20)
#  frame.grid(row=3, column=1)
#
#  for i in range(4):
#
#     print(i)
#     timer["text"] = "Work"
#     timer["fg"] = GREEN
#     window.update()
#     start=time()
#     end= time()
#     while end-start<=5:
#        end=time()
#        print(end - start)
#        if reset:
#            window.destroy()
#            beginning()
#        sleep(0.1)
#     timer["text"]="Break"
#     timer["fg"]=PINK
#
#
#     tick=Label(frame,text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
#     tick.pack(in_=frame,side=LEFT)
#     print(tick)
#     # print(tick)
#     # if i>0:
#     #    tick1=Label(frame,text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
#     #    tick1.pack(in_=frame, side=LEFT)
#     #    ticks.append(tick1)
#     # print(ticks)
#
#
#
#     window.update()
#     start=time()
#     end=time()
#     while end-start<=3:
#        end=time()
#        print(end-start)
#        if reset:
#            window.destroy()
#            beginning()
#        sleep(0.1)
#     if i ==3 or reset:
#        window.destroy()
#        beginning()
# -----------------------------New countdown mechanism----------------------------#
i = [4]


def start_countdown():
    with open("button_click") as reset:
        timer_reset=reset.read()
    global count_identifier

    global rest_pause
    if count_identifier==0 or (rest_pause==False and timer["text"]=="Break") :

        start_work[0]=time()
    else:
        global counter_dif
        try:
            start_work[0]=time()-counter_dif-1
        except:
            start_work[0]=time()


    if count_identifier%2==1:
        global after_object


        window.after_cancel(after_object)
    elif timer_reset!="Clicked" and i[0] >= 0 and count_identifier%2==0:

        # keep listening to the function that receives from the button while doing an after for the 25 min and 10 min respectively.3



        # the solution to this problem is to break up the after process instead of doing it all at the same time make use of small increments so that this after could finish withing a second or two and then go to another function that contains all the timer_reset.click values update and come everytime until we reach a limit somewhere probably an array value that will be updated until we get to the 25 minute mark so this insures as the signal from the button will be accepted.

        if rest_pause==True:
            rest()
        else:
            execute("Work")

        # start=time()
        # end=time()
        # while end-start<5:
        #     end=time()
        #     timer_reset.click=timer_reset.timer_command()

    else:
        reset_func()
    count_identifier += 1
def reset_func():

    i[0] = 4
    with open("button_click",mode="w") as reset:
         reset.write("Not Clicked")

    window.destroy()
    beginning()
    # counter[0]=WORK_MIN

def rest():
    global rest_pause
    global only_once
    with open("button_click") as reset:
        timer_reset=reset.read()
    if rest_pause!=True:
        i[0] -= 1
        only_once = True

    global count_identifier
    if count_identifier==1 or timer["text"]=="Work":

        start_work[0]=time()
    else:
        global counter_dif
        start_work[0]=time()-counter_dif-1

    if timer_reset=="Not Clicked" and i[0]>=0:
        #logic is a bit complicated not that simple, it is not easy to read but idk y i really like it but it shouldn't be this way, code usually shouldn't have a lot of global variables and logic shouldn't be tangled up
        #one thing that is costing us readability is using the adder variables at the end of the function actually bring it up it will be way easier that way giving us a clear distinction between functions.
        if i[0] >0 :

            execute("Break")

        # i feel like we can make this code look a lot cleaner than it is supposed to be, mainly by adding the self-referencing variables to the beginnning of the function

        elif i[0]==0:
            execute("Long Break")



        else:
            reset_func()

    else:

        reset_func()



    rest_pause=True


# counter=[WORK_MIN]
#create one function that keeps calling time and opening the button_click file every once in a while checking to see if the time.time() inside the function minus the initial outside the function equal to the amount and for the timer mechanism just substract the difference from the initial WORK_MIN or BREAK_MIN.
#given that we can actually use the with open as function right now as is with the "button_click" array. The with open as function is just substituting our Reset() class and nothing else.

def execute(identifier):
    global after_object
    global rest_pause
    if identifier=="Work":
        after_object=window.after(500,mirror,WORK_MIN,identifier)

    if identifier=="Break":

        after_object=window.after(500,mirror,SHORT_BREAK_MIN,identifier)

    if identifier=="Long Break":
        after_object=window.after(500,mirror,LONG_BREAK_MIN,identifier)


def mirror(value,identifier):

    value=int(value)
    global rest_pause
    with open("button_click") as reset:
        timer_reset=reset.read()

    end=time()
    global counter_dif
    counter_dif=int(end-start_work[0]-1)

    if timer_reset=="Clicked":
        reset_func()
    elif counter_dif<value:#elif counter[0]>=1:

        timer_mechanism(identifier=identifier,value=value,dif=counter_dif)

        # print(button_click)
        if identifier=="Break":
            execute("Break")
        if identifier=="Long Break":
            execute("Long Break")
        if identifier=="Work":
            execute("Work")
# this is the most important part of my code i.e., to set the button_click lower after the first sequence is expressed that is 30:00 or 00:00 and so evreytime a new sequence is activated the first number will not be a decreased one or incase of a stopwatch timer it wouldn't be increased.
#         counter[0] -= 1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^important!
    elif counter_dif>=value:# elif counter[0]<1:


        timer_mechanism(identifier=identifier, value=value, dif=counter_dif)
        if identifier=="Work":

            # if i[0]==1:
            #     counter[0]=LONG_BREAK_MIN
            # else:
            #     counter[0] = SHORT_BREAK_MIN
            rest_pause=False
            global count_identifier
            count_identifier=1



            counter_dif=0
            rest()
        if identifier=="Break" :
            # counter[0] = WORK_MIN

            count_identifier=0

            counter_dif = 0
            rest_pause=False
            start_countdown()
        if identifier=="Long Break":
            sleep(0.5)
            Beep(500,1500)
            reset_func()




# ---------------------------- UI SETUP ------------------------------- #
def beginning():
    global window
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
    clock_counter=canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)
    global rest_pause
    rest_pause=False
    global count_identifier
    count_identifier=0
    start = Button(text="Start", highlightthickness=0, borderwidth=0, command=start_countdown)
    start.grid(row=2, column=0)
    end = Button(text="Reset", highlightthickness=0, borderwidth=0, command=button_click)
    end.grid(row=2, column=2)
    window.attributes("-topmost", 1)

    window.mainloop()


beginning()


