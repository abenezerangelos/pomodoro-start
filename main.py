from tkinter import *
from time import *
from threading import Thread

# Options
# TODO 0: Fix the tick label first, DONE
# TODO 1: DONE, Try and figure out why the recursion doesn't work properly when the window.update()-(use update_idle() which is a lot better) is included inside the work part i.e. why isn't the break part being expressed
# So to do this part my idea is to set the countdown using after method inside a start countdown method and in this method also starting the timer mechanism with the same button and even destroying and starting the whole UI using after methodand we can basically use the mainloop to continually check if the value of self.reset has changed. And so we will be able to update and therefore reset the whole window including the frame or any other widget.
# TODO 2: Use bind to get around this problem
# TODO 3: Use threading.event
# TODO 4: Use "with open as"
# TODO 5: Regardless try your best to solve this problem with only Todo 1.
# TODO Tip: Use a combination of TODO 2,3 and 6 to achieve a very seamless and perfectly functioning program.
# TODO 6: Try using the App class method and try sending from the main to the thread mainloop
# TODO 7: Add the pause functionality, when pressing the start button twice and if pressed again it would function like the play button. so if button is pressed i.e. button_pressed%2==0
# TODO 8: Don't let pressing start once the program has started have any effects, basically make it unfunctional except for when starting the program from the beginning or reset.
# TODO 9: Instead of using the after callback instead use the OS time to keep track of the countdown and also manage the transition between Work and Break because you don't want your time to be fast or slow depending on other processes, if we want a program that is efficient we want to tie it to the OS Kernel time.
# TODO 10: ADD SOUND, for notification puposes! if possible let it have its own administrative access for sound where it uses maximum volume to notify. This part might be a little too advanced but this is the beauty of programming, the hill, feel me!
# Improvement for "todo 9 if you can't another very specific os timer just use time.time() function and make it work and also make your application use sound
# TODO 11: ADD STOP/END feature when the app ends for a small amount of time, and on top of that try removing the last break and replace it with the end/stop feature.
# TODO 12: Make sure this program uses as minimum of resources as possible, make sure it doesn't heavily interfere with other apps and your os as much as possible. Either find a data sturcture that is more efficient than a list or update the strategy you are using to count. Maybe threading or binding might fix it all.
# TODO 13: Add a feature that reminds you maybe every 5 minutes or so how much time you still have left.
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60000
SHORT_BREAK_MIN = 5*60000
LONG_BREAK_MIN = 20*60000


class Reset:
    def __init__(self):
        self.click = False
        self.activation = False

    def button_command(self):
        self.click = True

    def timer_command(self):
        return self.click


# ---------------------------- TIMER RESET ------------------------------- #
timer_reset = Reset()
reset = timer_reset.click

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_mechanism():
    minute=0
    if counter[0]<60000:
      if counter[0] % 1000 == 0 and counter[0]/1000<10:
        canvas.itemconfig(clock_counter, text=(f"00:0{int(counter[0]/1000)}"))
        canvas.update_idletasks()
      elif counter[0]% 1000==0 and counter[0]/1000>=10:
          canvas.itemconfig(clock_counter, text=(f"00:{int(counter[0] / 1000)}"))
          canvas.update_idletasks()

    elif counter[0]>=60000:
        if counter[0]%1000==0:
            transition=int(counter[0]/1000)
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
    if not timer_reset.click and i[0] > 0:

        # keep listening to the function that receives from the button while doing an after for the 25 min and 10 min respectively.3
        timer.config(text="Work", fg=GREEN)
        window.update_idletasks()

        # the solution to this problem is to break up the after process instead of doing it all at the same time make use of small increments so that this after could finish withing a second or two and then go to another function that contains all the timer_reset.click values update and come everytime until we reach a limit somewhere probably an array value that will be updated until we get to the 25 minute mark so this insures as the signal from the button will be accepted.
        execute("Work")

        # start=time()
        # end=time()
        # while end-start<5:
        #     end=time()
        #     timer_reset.click=timer_reset.timer_command()

    else:
        window.destroy()
        timer_reset.click = False
        i[0] = 4
        beginning()


def rest():
    global start_time
    start_time=0
    timer_reset.activation = True
    if not timer_reset.click:

        timer.config(text="Break", fg=PINK)

        if i[0] == 4:
            global frame
            frame = Frame(window, width=20, height=20)
            frame.grid(row=3, column=1)

        tick = Label(frame, text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
        tick.pack(side=LEFT)


        if i[0] > 0:
            execute("Break")

            if timer_reset.click:

                timer_reset.click = False
                window.destroy()
                beginning()

        else:
            window.destroy()
            beginning()

    else:
        window.destroy()
        i[0] = 4
        timer_reset.click = False
        beginning()
    i[0] -= 1
counter=[WORK_MIN]
def execute(identifier):
    if identifier=="Work":
        window.after(1,mirror,WORK_MIN)

    if identifier=="Break":
        window.after(1,mirror,SHORT_BREAK_MIN)

def mirror(value):
    if timer_reset.click:
        window.destroy()
        i[0]=4
        timer_reset.click=False
        counter[0]=WORK_MIN
        beginning()
    elif counter[0]>-1000:

        timer_mechanism()
        print(counter)
        if value==SHORT_BREAK_MIN:
            execute("Break")

        if value==WORK_MIN:
            execute("Work")
# this is the most important part of my code i.e., to set the button_click lower after the first sequence is expressed that is 30:00 or 00:00 and so evreytime a new sequence is activated the first number will not be a decreased one or incase of a stopwatch timer it wouldn't be increased.
        counter[0] -= 1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^important!
    elif counter[0]==-1000:

        window.deiconify()
        window.attributes("-topmost",1)
        window.attributes("-topmost",0)
        if value==WORK_MIN:
            if i[0]==1:
                counter[0]=LONG_BREAK_MIN
            else:
                counter[0] = SHORT_BREAK_MIN
            rest()
        if value==SHORT_BREAK_MIN:
            counter[0] = WORK_MIN
            start_countdown()



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
    start = Button(text="Start", highlightthickness=0, borderwidth=0, command=start_countdown)
    start.grid(row=2, column=0)
    end = Button(text="Reset", highlightthickness=0, borderwidth=0, command=timer_reset.button_command)
    end.grid(row=2, column=2)
    window.deiconify()
    window.attributes("-topmost", 1)
    window.mainloop()

beginning()

