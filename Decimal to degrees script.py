# Decimal to Degrees Converter
# Made by Speed3DBall a.k.a. Pain-au-Chocolat
# https://github.com/Pain-au-Chocolat/Decimal_to_degrees

import tkinter
from tkinter import *
import threading
import time
from math import pi

def decimal_to_degrees():
    try:
        global decimal_switch, result_minutes, result_seconds
        decimal_switch = True
        while True:
            user_input_decimal = str(decimal_entry_box.get())
            user_input_decimal = user_input_decimal.replace(",", ".")
            separator = "."
            if separator not in user_input_decimal:
                user_input_decimal = user_input_decimal + ".0"

            result_angle = user_input_decimal.split(separator, 1)[0]

            try:
                minutes_decimal_part = user_input_decimal.split(separator, 1)[-1]
                minutes_decimal_part = ("0." + str(minutes_decimal_part))
                minutes_decimal_part = float(minutes_decimal_part)
                minutes = minutes_decimal_part * 60
                result_minutes = str(minutes).split(separator, 1)[0]

                seconds_decimal_part = str(minutes).split(separator, 1)[-1]
                seconds_decimal_part = ("0." + str(seconds_decimal_part))
                seconds_decimal_part = float(seconds_decimal_part)
                seconds = seconds_decimal_part * 60
                result_seconds = str(seconds).split(separator, 1)[0]
            except ValueError:
                decimal_entry_box.delete(0, tkinter.END)
                degrees_entry_box.delete(0, tkinter.END)
                minutes_entry_box.delete(0, tkinter.END)
                seconds_entry_box.delete(0, tkinter.END)

            if decimal_switch:
                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, str(result_angle))
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, str(result_minutes))
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, str(result_seconds))
            time.sleep(0.1)
    except ValueError:
        decimal_entry_box.delete(0, tkinter.END)
        decimal_entry_box.insert(0, "0")
        degrees_entry_box.delete(0, tkinter.END)
        degrees_entry_box.insert(0, "0")
        minutes_entry_box.delete(0, tkinter.END)
        minutes_entry_box.insert(0, "0")
        seconds_entry_box.delete(0, tkinter.END)
        seconds_entry_box.insert(0, "0")


def degrees_to_decimal():
    global decimal_switch, result_decimal
    while True:
        user_input_degrees = str(degrees_entry_box.get())
        user_input_minutes = str(minutes_entry_box.get())
        user_input_seconds = str(seconds_entry_box.get())
        try:
            result_decimal = (float(user_input_degrees) if user_input_degrees != "" else 0.0) + \
                            ((float(user_input_minutes)/60) if user_input_minutes != "" else 0.0) + \
                            ((float(user_input_seconds)/3600) if user_input_seconds != "" else 0.0)
        except ValueError:
            decimal_entry_box.delete(0, tkinter.END)
            decimal_entry_box.insert(0, "0")
            degrees_entry_box.delete(0, tkinter.END)
            degrees_entry_box.insert(0, "0")
            minutes_entry_box.delete(0, tkinter.END)
            minutes_entry_box.insert(0, "0")
            seconds_entry_box.delete(0, tkinter.END)
            seconds_entry_box.insert(0, "0")

        if not decimal_switch:
            decimal_entry_box.delete(0, tkinter.END)
            decimal_entry_box.insert(0, str(result_decimal))
        time.sleep(0.1)


def rads_to_decimal():
    #TODO
    pass



def grads_to_decimal():
    #TODO
    pass


def no_revolutions():
    while True:
        user_input_degrees = str(degrees_entry_box.get())
        try:
            while 360 < int(user_input_degrees) < 10000000:
                user_input_degrees = int(user_input_degrees) - 360
            if int(user_input_degrees) == 360:
                no_revolutions_angle.configure(text="[ 0° ]")
            elif int(user_input_degrees) == 0:
                no_revolutions_angle.configure(text="[ 0° ]")
            elif int(user_input_degrees) < 360:
                no_revolutions_angle.configure(text="[ " + str(user_input_degrees) + "° ] / -" + str(360 - int(user_input_degrees)))
            else:
                no_revolutions_angle.configure(text="Chyba pri výpočte")
            time.sleep(0.1)
        except:
            no_revolutions_angle.configure(text="Chyba pri výpočte")

global decimal_switch
def window_focus():
    while True:
        global decimal_switch
        widget = window.focus_get()
        if str(widget) == ".!labelframe4.!entry":
            decimal_switch = True
        else:
            decimal_switch = False
        time.sleep(0.1)


window = Tk()
window.title("Vyrobené pre KMS <3")
window.geometry("553x290")
window.configure(bg='gray')

frame1 = LabelFrame(window, bg="green", bd=5)
frame1.grid(row=0, column=0)

frame2 = LabelFrame(window, bg="green")
frame2.grid(row=1, column=0, pady=20)

frame3 = LabelFrame(window, bg="gray", bd=0)
frame3.grid(row=2, column=0, pady=0)

frame4 = LabelFrame(window, bg="green", bd=4)
frame4.grid(row=3, column=0, pady=20)

frame5 = LabelFrame(window, bg="green", bd=0)
frame5.grid(row=4, column=0, pady=0)

frame6 = LabelFrame(window, bg="green", bd=0)
frame6.place(x=220, y=55)

label = Label(frame1,
              text="Prevodník stupňov a desatinných uhlov",
              font=('Arial',20,'bold'),
              fg='white',
              bg='gray',
              bd=10,
              padx=1,
              pady=1,
              )
label.grid(row=0, column=0)

degrees_entry_box = Entry(frame2, bd=2,width=5, font=('Arial',10,'bold'))
degrees_entry_box.insert(0, "0")
degrees_entry_box.grid(row=0, column=0)
degrees_symbol = Label(frame2, text="°", fg='black', bg='gray', font=('Arial',16,'bold'))
degrees_symbol.grid(row=0, column=1)

minutes_entry_box = Entry(frame2, bd=2,width=5, font=('Arial',10,'bold'))
minutes_entry_box.insert(0, "0")
minutes_entry_box.grid(row=0, column=2)
minutes_symbol = Label(frame2, text="'", fg='black', bg='gray', font=('Arial',16,'bold'))
minutes_symbol.grid(row=0, column=3, padx=1.5)

seconds_entry_box = Entry(frame2, bd=2,width=5, font=('Arial',10,'bold'))
seconds_entry_box.insert(0, "0")
seconds_entry_box.grid(row=0, column=4)
seconds_symbol = Label(frame2, text='"', fg='black', bg='gray', font=('Arial',16,'bold'))
seconds_symbol.grid(row=0, column=5)


grads_text = Label(frame3, text='Grads', fg='black', bg='gray', font=('Arial',10,'bold'))
grads_text.grid(row=0, column=0)
grads_entry_box = Entry(frame3, bd=3, width=15, font=('Arial', 10, 'bold'))
grads_entry_box.insert(0, "0")
grads_entry_box.grid(row=0, column=1)


arrows = Label(frame3,
              text="⬆⬇",
              font=('Arial',20,'bold'),
              fg='black',
              bg='gray',
              bd=0,
              padx=10,
              pady=10,
              )
arrows.grid(row=0, column=2)

rads_entry_box = Entry(frame3, bd=3, width=15, font=('Arial', 10, 'bold'))
rads_entry_box.insert(0, "0")
rads_entry_box.grid(row=0, column=3)
rads_text = Label(frame3, text='Rads', fg='black', bg='gray', font=('Arial',10,'bold'))
rads_text.grid(row=0, column=4)


decimal_entry_box = Entry(frame4, bd=2,width=20, font=('Arial',10,'bold'))
decimal_entry_box.insert(0, "0")
decimal_entry_box.grid(row=0, column=0)

no_revolutions_angle = Label(frame5,
              text="INITIALISATION OF SCRIPT",
              font=('Arial',10,'bold'),
              fg='black',
              bg='gray',
              bd=0,
              padx=0,
              pady=0,
              )
no_revolutions_angle.grid(row=0, column=0)

made_by = Label(frame6,
              text="Made by Speed3DBall",
              font=('Arial',8,'bold'),
              fg='black',
              bg='gray',
              bd=0,
              padx=0,
              pady=0,
              )
made_by.grid(row=0, column=0)


e = threading.Thread(name='decimalToDegrees', target=decimal_to_degrees)
t = threading.Thread(name='degreesToDecimal', target=degrees_to_decimal)
f = threading.Thread(name='focus', target=window_focus)
n = threading.Thread(name='noRevolutions', target=no_revolutions)

e.daemon = True
t.daemon = True
f.daemon = True
n.daemon = True

t.start()
e.start()
f.start()
n.start()

window.mainloop()
