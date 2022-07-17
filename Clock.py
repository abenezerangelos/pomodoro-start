from tkinter import *
from time import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25*60
SHORT_BREAK_MIN = 0.125*60
LONG_BREAK_MIN = 0.20*60
# if by any chance you want to change the counting method from a second to like 500 ms just decrease the time in the after method to a 500ms
class Clock():
    def __init__(self):
        with open("button_click",mode="w") as reset:
            reset.write("Not Clicked")




        self.start_time=time() #starts the timer, we need it to be a global variable
        self.window=Tk()
        self.window.title("Pomodoro")
        self.window.config(pady=50, padx=100, bg=YELLOW)
        self.i_counter=4
        self.identifier="Work"
        # // We will implement this later on, I hope we do implement this peacefully
        self.frame=Frame(self.window,width=20,height=20)
        self.start=Button(text="Start", highlightthickness=0, borderwidth=0, command=self.start_countdown)
        self.start.grid(row=2, column=0)
        self.reset=Button(text="Reset", highlightthickness=0, borderwidth=0, command=self.write_reset)
        self.reset.grid(row=2, column=2)

        self.canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
        self.tomato = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 100, image=self.tomato)
        self.clock_counter=self.canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(row=1, column=1)
        self.timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, foreground=GREEN)
        self.timer.grid(row=0, column=1)
        self.window.deiconify()
        self.window.attributes("-topmost", 1)
        self.end=time()
        self.dif = self.end-self.start_time
        self.window.mainloop()
    def timer_mechanism(self):
        minute=0
        print(self.dif,"BEFORE")
        counter=int((self.value-self.dif+1))
        print(counter,"AFTER")
        # print(value,"The Big V",1111111111)
        if self.identifier == "Work" and counter == self.value:

            self.timer.config(text="Work", fg=GREEN)
            self.window.deiconify()
            self.window.attributes("-topmost", 0)
            self.window.attributes("-topmost", 1)
            print(self.i_counter, "Counter")
        elif (self.identifier=="Break"or self.identifier=="Long Break") and counter==int(self.value) :
            print(int(counter), "IT AIN'T MFING ", 0, "SO SHUSH PLEASE!!!",int(self.value))
            self.timer.config(text="Break", fg=PINK)

            if self.i_counter == 3:

                self.frame.grid(row=3, column=1)

            tick = Label(self.frame, text="✔", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
            tick.pack(side=LEFT)
            self.window.deiconify()
            self.window.attributes("-topmost", 1)
            self.window.attributes("-topmost", 0)
            # ichecker=False

        if counter < 60:
            if counter / 1 < 10:
                self.canvas.itemconfig(self.clock_counter, text=(f"00:0{int(counter/1)}"))
                self.canvas.update_idletasks()
            elif counter / 1 >= 10:
                self.canvas.itemconfig(self.clock_counter, text=(f"00:{int(counter/1 )}"))
                self.canvas.update_idletasks()


        elif counter >= 60:

            transition = int(counter / 1)
            while transition >= 60:
                minute += 1
                transition -= 60

            second = transition
            if second < 10 and minute < 10:
                self.canvas.itemconfig(self.clock_counter, text=(f"0{minute}:0{second}"))
                self.canvas.update_idletasks()
            elif second >= 10 and minute < 10:
                self.canvas.itemconfig(self.clock_counter, text=(f"0{minute}:{second}"))
                self.canvas.update_idletasks()
            elif minute >= 10 and second < 10:
                self.canvas.itemconfig(self.clock_counter, text=(f"{minute}:0{second}"))
                self.canvas.update_idletasks()
            else:
                self.canvas.itemconfig(self.clock_counter, text=(f"{minute}:{second}"))
                self.canvas.update_idletasks()



    def execute(self):
        self.window.after(1000,self.bouncer)
    def bouncer(self):
        print(self.end,"!!!!!!!!!")
        self.end=time()
        print(self.i_counter, "Counter")
        print(self.end,"$$$$$$$")

        self.dif=(self.end-self.start_time-0.5)
        print("[[[[[[[[[",self.dif,"]]]]]]]]]]]")

        print(self.read())
        print(self.start_time,"$$$$$$$$$")
        if self.read() == "Clicked" or self.i_counter<0:
            self.restart()
            print("YOU're done because of the i_counter or the button got clicked but most probably self.i_counter")

        else :
            print(self.value, "VALUE")
            if self.dif < self.value:
                self.timer_mechanism()
                print(int(self.dif), "TFFFFFFF!!!!TFTFTFTF")
                self.execute()

            elif self.dif >= self.value:
                self.timer_mechanism()

                print(self.value, "2nd VALUE")
                print("GOOOOOOGOOOOOGAGAGAGAGAGAGA")
                if self.identifier=="Work" :
                    print("SO Whats the fucking deal, is it executing or nah")
                    self.rest()
                elif self.identifier=="Break" or self.identifier=="Long Break":
                    self.start_countdown()



    def start_countdown(self):
        if self.read()=="Not Clicked" and self.i_counter>0:
            self.start_time=time()
            print(self.start_time,"!!!!!!!!")
            print("When, How and Why is this being executed",time())
            self.identifier="Work"
            self.value=WORK_MIN
            self.execute()

        else:
            print("Apparently because self.i_counter is equal to 0")
            self.restart()

    def read(self):
        with open("button_click", mode="r") as reset:
            button=reset.read()
        return button
    def write_reset(self):
        with open("button_click",mode="w")as reset:
            reset.write("Clicked")
    def rest(self):
        print(self.value,"333333")
        self.i_counter -= 1
        if self.read()=="Not Clicked":
          self.start_time = time()
          print(self.i_counter,"Counter")

          if self.i_counter>0:
            self.identifier="Break"
            self.value=SHORT_BREAK_MIN
            print(self.value, 444444444444)
            self.execute()
          elif self.i_counter==0:
              self.identifier="Long Break"
              self.value=LONG_BREAK_MIN
              self.execute()
        else:
            self.restart()



    def restart(self):
        self.window.destroy()
        beginning_start()
def beginning_start():

# maybe if we want to we can put this in a conditionally set while loop and see what becomes of it although, I wouldn't suggest this

    pomodoro=Clock()
    return pomodoro

x=beginning_start()
print(x)



