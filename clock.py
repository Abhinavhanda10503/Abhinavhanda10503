from time import sleep
import tkinter
import time
from pygame import mixer
import datetime
from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox

#main window 
root = tkinter.Tk()
root.title("clock")
root.configure(background="black")
root.geometry("800x300")
root.resizable(width=False, height=False)

running = False
hours, minutes, seconds = 0, 0, 0


now = datetime.now()


class show():
    def __init__(self):
        self.nx = tkinter.Tk()
        self.nx.title("stopwatch")
        self.nx.configure(background="black")
        self.nx.geometry("800x300")
        self.nx.resizable(width=False, height=False)
        self.pic=PhotoImage(file='icons8-clock-64.png')
        self.my_button = Button(self.nx, image=self.pic, command=lambda: [
                                self.nx.destroy(), clock()])
        self.my_button.grid(row=0, column=1, pady=50)

        self.my_button1 = Button(self.nx, text="STOPWATCH")
        self.my_button1.grid(row=0, column=2, pady=20)

        self.my_button2 = Button(self.nx, text="ALARM", command=lambda: [
                                 self.nx.destroy(), alarm()])
        self.my_button2.grid(row=0, column=3, pady=20)

        self.my_label2 = Label(self.nx, text="00:00:00", font=(
            "Helvetica", 70), fg="green", bg="black")
        self.my_label2.grid(row=4, columnspan=5, padx=70)

        self.my_button3 = Button(self.nx, text="START", command=self.start)
        self.my_button3.grid(row=6, column=1, pady=20)

        self.my_button4 = Button(self.nx, text="STOP", command=self.stop)
        self.my_button4.grid(row=6, column=2, pady=20)

        self.my_button5 = Button(self.nx, text="RESET", command=self.reset)
        self.my_button5.grid(row=6, column=3, pady=20)

    def start(self):
        global running
        if not running:
            global hours, minutes, seconds
            seconds += 1
            if seconds == 60:
                minutes += 1
                seconds = 0
            if minutes == 60:
                hours += 1
                minutes = 0
            hour_string = f'{hours}' if hours > 9 else f'0{hours}'
            minute_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
            second_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

            self.my_label2.config(text=hour_string + ":" +
                                  minute_string + ":" + second_string)
            global update_time
            update_time = self.my_label2.after(10, self.start)

    def stop(self):
        global running
        if not running:
            self.my_label2.after_cancel(update_time)

    def reset(self):
        global running
        if not running:
            global hours, minutes, seconds
            hours, minutes, seconds = 0, 0, 0
            self.my_label2.config(text='00:00:00')


class clock():
    def __init__(self):
        self.root1 = tkinter.Tk()
        self.root1.title("clock")
        self.root1.configure(background="black")
        self.root1.geometry("800x300")
        self.root1.resizable(width=False, height=False)
        self.pic=PhotoImage(file='icons8-clock-64.png')
        self.my_button = Button(self.root1, image=self.pic)
        self.my_button.grid(row=0, column=1, pady=50)

        self.my_button1 = Button(self.root1, text="STOPWATCH", command=lambda: [
                                 self.root1.destroy(), show()])
        self.my_button1.grid(row=0, column=2, pady=20)

        self.my_button2 = Button(self.root1, text="ALARM", command=lambda: [
                                 self.root1.destroy(), alarm()])
        self.my_button2.grid(row=0, column=3, pady=20)
        self.my_label = Label(self.root1, text="", font=(
            "Helvetica", 70), fg="green", bg="black")
        self.my_label.grid(row=4, columnspan=5, padx=70)
        self.my_label1 = Label(self.root1, text="", font=(
            "Helvetica", 15), fg="green", bg="black")
        self.my_label1.grid(row=5, column=2)
        self.clock1()

    def clock1(self):
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        sec = time.strftime("%S")
        ap = time.strftime("%p")
        self.my_label.config(text=hour + ":" + minute + ":" + sec + " " + ap)
        self.my_label.after(1, self.clock1)
        date = now.strftime("%d:%m:%y")
        self.my_label1.config(text="current:" + " " + date)


class alarm():
    def __init__(self):
        self.root2 = tkinter.Tk()
        self.root2.title("Alarm clock")
        self.root2.configure(background="black")
        self.root2.geometry("800x300")
        self.root2.resizable(width=False, height=False)
        self.pic=PhotoImage(file='icons8-clock-32.png')
        self.my_button = Button(self.root2, image=self.pic, command=lambda: [
                                 self.root2.destroy(), clock()],borderwidth=0)
        self.my_button.grid(row=0, column=3, pady=50, padx=50)

        self.my_button1 = Button(self.root2, text="STOPWATCH", command=lambda: [
                                 self.root2.destroy(), show()])
        self.my_button1.grid(row=0, column=4, pady=20, padx=20)

        self.my_button2 = Button(self.root2, text="ALARM")
        self.my_button2.grid(row=0, column=5, pady=20, padx=20)

        
        self.hour = Label(self.root2, text="Hour", height=1,
                          font=('Ivy 18 bold'), bg="black", fg="green")
        self.hour.grid(row=4, column=3, padx=50)
        self.c_hour = Combobox(self.root2, width=3, font=('arial 15'))
        self.c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")
        self.c_hour.current(0)
        self.c_hour.grid(row=5, column=3, padx=50)

        self.min = Label(self.root2, text="Minute", height=1,
                         font=('Ivy 18 bold'), bg="black", fg="green")
        self.min.grid(row=4, column=4, padx=30)

        self.c_min = Combobox(self.root2, width=3, font=('arial 15'))
        self.c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
                                "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
        self.c_min.current(0)
        self.c_min.grid(row=5, column=4, padx=30)

        self.sec = Label(self.root2, text="Second", height=1,
                         font=('Ivy 18 bold'), bg="black", fg="green")
        self.sec.grid(row=4, column=5, padx=30)
        self.c_sec = Combobox(self.root2, width=3, font=('arial 15'))
        self.c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
                                "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
        self.c_sec.current(0)
        self.c_sec.grid(row=5, column=5, padx=30)

        self.period = Label(self.root2, text="Period", height=1, font=(
            'Ivy 18 bold'), bg="black", fg="green")
        self.period.grid(row=4, column=6, padx=30)
        self.c_period = Combobox(self.root2, width=3, font=('arial 15'))
        self.c_period['values'] = ("AM", "PM")
        self.c_period.current(0)
        self.c_period.grid(row=5, column=6, padx=30)

        self.my_button = Button(self.root2, font=(
            "arial 10 bold"), text="Activate", command=self.alarm)
        self.my_button.grid(row=11, column=4, padx=80, pady=20)

    def alarm(self):
        while True:
            control = 1
            #print(control)

            alarm_hour = self.c_hour.get()
            alarm_min = self.c_min.get()
            alarm_sec = self.c_sec.get()
            alarm_period = self.c_period.get().upper()
            now = datetime.now()

            hr = now.strftime("%H")
            mn = now.strftime("%M")
            sc = now.strftime("%S")
            ap = now.strftime("%p").upper()
            if control == 1:
                if alarm_period == ap:
                    if alarm_hour == hr:
                        if alarm_min == mn:
                            if alarm_sec == sc:
                                self.sound_alarm()
            sleep(1)

    def sound_alarm(self):
        mixer.music.load('relaxing-music-vol1-124477.mp3')
        mixer.music.play()

    mixer.init()


my_label = Label(root, text="welcome to clock", font=(
    "Helvetica", 70), bg="black", fg="white")
my_label.grid(row=0, column=1, columnspan=5, padx=20)

my_button = Button(root, text="click here", command=lambda: [
                   root.destroy(), alarm()], font=("Helvetica", 15))
my_button.grid(row=1, column=3)


root.mainloop()
