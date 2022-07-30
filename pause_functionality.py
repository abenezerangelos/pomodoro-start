# Not the clean version still looking very nasty as of now.

# from tkinter import *
# from time import *
# # Python program killing
# # a thread using ._stop()
# # function
# #
# # import time
# # import threading
# #
# # class MyThread(threading.Thread):
# #
# # 	# Thread class with a _stop() method.
# # 	# The thread itself has to check
# # 	# regularly for the stopped() condition.
# #
# # 	def __init__(self, *args, **kwargs):
# # 		super(MyThread, self).__init__(*args, **kwargs)
# # 		self.stop = threading.Event()
# #
# #
# # 	# function using _stop function
# #
# #
# #
# #
# # 	def run(self):
# # 		while True:
# # 			if self.stop.is_set():
# # 				return
# # 			print("Hello, world!")
# # 			time.sleep(1)
# #
# # t1 = MyThread()
# #
# # t1.start()
# # time.sleep(7)
# # t1.stop.set()
# # t1.join()
#
# running = False  # Global flag
#
# def working():
#     if running:  # Only do this if the Stop button has not been clicked
#         print ("Work")
#
#     # After 1 second, call scanning again (create a recursive loop)
#     root.after(1000, working)
# def breaking():
# 	if running:
# 		print("Break")
#
# 	root.after(1000,breaking)
# def start():
#     """Enable scanning by setting the global flag to True."""
#     global running
#     running = True
#
# def stop():
#     """Stop scanning by setting the global flag to False."""
#     global running
#     running = False
#
# root = Tk()
# root.title("Title")
# root.geometry("500x500")
#
# app = Frame(root)
# app.grid()
#
# start = Button(app, text="Start Scan", command=start)
# stop = Button(app, text="Stop", command=stop)
#
# start.grid()
# stop.grid()
#
# root.after(1000, working)  # After 1 second, call scanning
# init=time()
# end=time()
# while end-init<10:
# 	end=time()
# 	print(end-init)#this is a simulation process showing that the working phase will last 25 minutes, then the breaking part will start right after.
# root.after(1000,breaking)
# init=time()
# end=time()
# while end-init<10:
# 	end=time()
# 	print(end-init)
#
#
# root.mainloop()

# import tkinter as tk
# import threading
#
# class App(threading.Thread):
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.start()
#
#     def callback(self):
#         self.root.quit()
#
#     def run(self):
#         self.root = tk.Tk()
#         self.root.protocol("WM_DELETE_WINDOW", self.callback)
#
#         label = tk.Label(self.root, text="Hello World",padx=100,pady=100)
#         label.pack()
#
#         self.root.mainloop()
#
#
# app = App()
# print('Now we can continue running code while mainloop runs!')
#
# for i in range(1000000):
#     print(i)

# import tkinter as tk
#
# def handle_focus(event):
#     if event.widget == root:
#         print("I have gained the focus")
#
# root = tk.Tk()
# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)
#
# entry1.pack(padx=30,pady=50)
# entry2.pack(padx=50,pady=50)
#
# root.bind("<FocusIn>", handle_focus)
#
# root.mainloop()
#Import tkinter library
from tkinter import *

#Create an instance of tkinter frame
# win = Tk()
# #Set the geometry
# win.geometry("750x250")
# #Create a Text WIdget
# text= Text(win, width= 30, height= 10)
# text.insert(INSERT, "Hello World!")
# #Activate the focus
# text.focus_set()
# text.pack()
# #Create an Entry Widget
# entry=Entry(win,width= 30)
# entry.pack()
# win.mainloop()

#^^^^^^This is such an ingenious beautiful piece of code and logic

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
# TODO 7: Thank God, finally successfully done,  Add the pause functionality, when pressing the start button twice and if pressed again it would function like the play button. so if button is pressed i.e. button_pressed%2==0
# TODO 8: Easily DONE, Don't let pressing start once the program has started have any effects, basically make it unfunctional except for when starting the program from the beginning or reset.
# TODO 9: DONE, kinda, i am still using the after callback but it is also depepnding on the time() method. One thing I want to try is the event and bind method without no help from the after callback.  Instead of using the after callback instead use the OS time to keep track of the countdown and also manage the transition between Work and Break because you don't want your time to be fast or slow depending on other processes, if we want a program that is efficient we want to tie it to the OS Kernel time.
# TODO 10:DONE, ADD SOUND, for notification puposes! if possible let it have its own administrative access for sound where it uses maximum volume to notify. This part might be a little too advanced but this is the beauty of programming, the hill, feel me!
# Improvement for "todo 9, kinda done, not the sound part, if you can't another very specific os timer just use time.time() function and make it work and also make your application use sound
# TODO 11:(Will do almost already done, ez, I don't see the applicability- actually instead ask the user if they want to stop or start another round of the timer) ADD STOP/END feature when the app ends for a small amount of time, and on top of that try removing the last break and replace it with the end/stop feature.
# TODO 12:(Tried my best, except for the fact that I haven't tried any of the threading, event or binding strategies just yet) Make sure this program uses as minimum of resources as possible, make sure it doesn't heavily interfere with other apps and your os as much as possible. Either find a data sturcture that is more efficient than a list or update the strategy you are using to count. Maybe threading or binding might fix it all.
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25*60
SHORT_BREAK_MIN = 0.125*60
LONG_BREAK_MIN = 0.25*60


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

# ichecker = False # should be deprecated, not necessarily useful given the fact that you can just use the time to check if it was the start and then activate based on that.
def timer_mechanism(identifier,value,dif):
    minute=0
    print(i)
    value=int(value)
    counter=int(value-dif)
    print(dif,"CLOCK DIFFERENCE BETWEEN START AND END")
    print(value)
    print(counter)

    if identifier=="Work" and int(dif)==0 :

        timer.config(text="Work", fg=GREEN)
        if i[0]!=4:
            timer.bell(window)
            print("\n\TIMER\n\n time")
        print("Time has been displayed")
        window.deiconify()
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)

    elif (identifier=="Break" or identifier=="Long Break")and int(dif)==0:
        print(dif, "IT AIN'T MFING ",0, "SO SHUSH PLEASE!!!")
        timer.config(text="Break", fg=PINK)

        if i[0]==3:
            global frame
            frame = Frame(window, width=20, height=20)
            frame.grid(row=3, column=1)

        tick = Label(frame, text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
        tick.bell(window)
        tick.pack(side=LEFT)
        window.deiconify()
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        # ichecker=False

    if counter<60 :
      if counter/1<10:
        canvas.itemconfig(clock_counter, text=(f"00:0{int(counter/1)}"))
        canvas.update_idletasks()
      elif counter/1>=10:
          canvas.itemconfig(clock_counter, text=(f"00:{int(counter / 1)}"))
          canvas.update_idletasks()


    elif counter>=60 :

            print("Time has been displayed")
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
count_identifier=0



def start_countdown():
    with open("button_click") as reset:
        timer_reset=reset.read()

    global count_identifier
    print(count_identifier,11111111111)

    global counter_dif
    if count_identifier>0 and count_identifier%2==0:
        start_work[0]=time()-counter_dif-1
    elif count_identifier==0:
        start_work[0] = time()
    print(start_work[0],"Not that important")

    if count_identifier%2==1:
        global after_object
        window.after_cancel(after_object)
    print(start_work[0],"SHOULD BE THE SAME")
    global pause_identifiier
    if timer_reset!="Clicked" and i[0] >= 0 and count_identifier%2==0:
        print(start_work[0],"IMPORTANT<IMPORTANT>")

        # keep listening to the function that receives from the button while doing an after for the 25 min and 10 min respectively.3



        # the solution to this problem is to break up the after process instead of doing it all at the same time make use of small increments so that this after could finish withing a second or two and then go to another function that contains all the timer_reset.click values update and come everytime until we reach a limit somewhere probably an array value that will be updated until we get to the 25 minute mark so this insures as the signal from the button will be accepted.
        print("POOOPIE BUTTHOLE BABY")

        if pause_identifier=="Work":
            execute("Work")
        elif pause_identifier=="Break":
            execute("Break")
        elif pause_identifier=="Long Break":
            execute("Long Break")

        # start=time()
        # end=time()
        # while end-start<5:
        #     end=time()
        #     timer_reset.click=timer_reset.timer_command()

    elif timer_reset=="Clicked" or i[0]<0:
        window.destroy()
        reset_allvalues()
        beginning()
    count_identifier += 1
def reset_allvalues():

    i[0] = 4
    global count_identifier
    count_identifier=0
    with open("button_click",mode="w") as reset:
         reset.write("Not Clicked")
    # counter[0]=WORK_MIN
# counter=[WORK_MIN]
#create one function that keeps calling time and opening the button_click file every once in a while checking to see if the time.time() inside the function minus the initial outside the function equal to the amount and for the timer mechanism just substract the difference from the initial WORK_MIN or BREAK_MIN.
#given that we can actually use the with open as function right now as is with the "button_click" array. The with open as function is just substituting our Reset() class and nothing else.

def execute(identifier):

    global after_object
    if identifier=="Work":
        after_object=window.after(1000,mirror,WORK_MIN,identifier)

    if identifier=="Break":
        print("working at some point")
        print(i)
        print(start_work)
        after_object=window.after(1000,mirror,SHORT_BREAK_MIN,identifier)
    if identifier=="Long Break":
        after_object=window.after(1000,mirror,LONG_BREAK_MIN,identifier)

def mirror(value,identifier):
    global pause_identifier
    print("WHATEVER, JUST PLEASE WORK!")
    value=int(value)
    with open("button_click") as reset:
        timer_reset=reset.read()
    print(timer_reset,"DEBUG2!!!")
    end=time()
    global counter_dif
    counter_dif=int(end-start_work[0]-1)
    print(int(counter_dif),"EVERY STEP OF THE WAY!")
    if timer_reset=="Clicked":
        window.destroy()
        reset_allvalues()
        beginning()
    elif counter_dif<value:#elif counter[0]>=1:
        print("this is working too")
        timer_mechanism(identifier=identifier,value=value,dif=counter_dif)
        # print(button_click)
        if identifier=="Break":
            print("this is working three")
            execute("Break")
        if identifier=="Long Break":
            execute("Long Break")
        if identifier=="Work":
            execute("Work")
# this is the most important part of my code i.e., to set the button_click lower after the first sequence is expressed that is 30:00 or 00:00 and so evreytime a new sequence is activated the first number will not be a decreased one or incase of a stopwatch timer it wouldn't be increased.
#         counter[0] -= 1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^important!
    elif counter_dif>=value:# elif counter[0]<1:
        print(counter_dif, "=", int(value), "AT THIS POINT!")

        timer_mechanism(identifier=identifier, value=value, dif=counter_dif)
        if identifier=="Work":
            # if i[0]==1:
            #     counter[0]=LONG_BREAK_MIN
            # else:
            #     counter[0] = SHORT_BREAK_MIN
            print("\n\nWHAT ABOUT THIS, THIS HAS TO START EXECUTING AGHHHH\n\n")
            if timer_reset == "Not Clicked":
                print(i[0])
                if i[0] > 1:
                    print("\n\n EXECUTION!!!!!!!!!!!!\n\n")
                    pause_identifier="Break"
                    start_work[0]=time()
                    execute("Break")
                elif i[0] == 1:
                    start_work[0]=time()
                    pause_identifier="Long Break"
                    execute("Long Break")



                else:
                    print("DESTRUCTION")
                    window.destroy()
                    reset_allvalues()
                    beginning()

            else:
                print("DESTRUCTION!!!!!")
                window.destroy()
                reset_allvalues()
                beginning()
            i[0] -= 1
        if identifier=="Break" :
            # counter[0] = WORK_MIN
            global count_identifier
            count_identifier=1
            start_work[0]=time()
            pause_identifier="Work"
            execute("Work")
        elif identifier=="Long Break":
            window.bell()
            window.destroy()
            reset_allvalues()
            beginning()



# ---------------------------- UI SETUP ------------------------------- #
def beginning():
    global window
    window = Tk(className="Pomodoro")
    window.title("Pomodoro")
    window.config(pady=50, padx=100, bg=YELLOW)
    print("W")

    global timer
    timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, foreground=GREEN)
    timer.grid(row=0, column=1)
    print("H")
    global canvas
    canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
    tomato = PhotoImage(file="tomato.png")
    canvas.create_image(100, 100, image=tomato)
    global clock_counter
    print("Y")
    clock_counter=canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)
    global counter_dif
    counter_dif=0
    global pause_identifier
    pause_identifier="Work"
    print("I")
    start = Button(text="Start", highlightthickness=0, borderwidth=0, command=start_countdown)
    start.grid(row=2, column=0)
    end = Button(text="Reset", highlightthickness=0, borderwidth=0, command=button_click)
    end.grid(row=2, column=2)
    print("S")
    window.deiconify()

    window.attributes("-topmost", 1)
    print("it taking so long")
    window.mainloop()


beginning()

