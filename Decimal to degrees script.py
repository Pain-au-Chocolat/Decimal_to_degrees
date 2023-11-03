# Decimal to Degrees Converter

import tkinter
from tkinter import *
import threading
import time

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
            time.sleep(0.01)
    except ValueError:
        degrees_entry_box.delete(0, tkinter.END)
        minutes_entry_box.delete(0, tkinter.END)
        seconds_entry_box.delete(0, tkinter.END)
        decimal_entry_box.delete(0, tkinter.END)

e = threading.Thread(name='decimalToDegrees', target=decimal_to_degrees)
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
            degrees_entry_box.delete(0, tkinter.END)
            minutes_entry_box.delete(0, tkinter.END)
            seconds_entry_box.delete(0, tkinter.END)

        if not decimal_switch:
            decimal_entry_box.delete(0, tkinter.END)
            decimal_entry_box.insert(0, str(result_decimal))
        time.sleep(0.01)




t = threading.Thread(name='degreesToDecimal', target=degrees_to_decimal)

global decimal_switch

def window_focus():
    while True:
        global decimal_switch
        widget = window.focus_get()
        if str(widget) == ".!labelframe4.!entry":
            decimal_switch = True
        else:
            decimal_switch = False
        time.sleep(0.01)

f = threading.Thread(name='focus', target=window_focus)

window = Tk()
window.title("Vyrobené pre KMS <3")
window.geometry("553x270")
window.configure(bg='gray')



frame1 = LabelFrame(window, bg="green", bd=5)
frame1.grid(row=0, column=0)

frame2 = LabelFrame(window, bg="green")
frame2.grid(row=1, column=0, pady=20)

frame3 = LabelFrame(window, bg="green", bd=0)
frame3.grid(row=2, column=0, pady=0)

frame4 = LabelFrame(window, bg="green", bd=4)
frame4.grid(row=3, column=0, pady=20)


label = Label(frame1,
              text="Prevodník stupňov a desatinných uhlov",
              font=('Arial',20,'bold'),
              fg='black',
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

arrows = Label(frame3,
              text="⬆⬇",
              font=('Arial',20,'bold'),
              fg='black',
              bg='gray',
              bd=0,
              padx=10,
              pady=10,
              )
arrows.grid(row=0, column=0)


decimal_entry_box = Entry(frame4, bd=2,width=20, font=('Arial',10,'bold'))
decimal_entry_box.insert(0, "0")
decimal_entry_box.grid(row=0, column=0)

t.start()
e.start()
f.start()


window.mainloop()

