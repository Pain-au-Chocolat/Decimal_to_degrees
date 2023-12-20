# Decimal to Degrees Converter
# Made by Speed3DBall a.k.a. Pain-au-Chocolat
# https://github.com/Pain-au-Chocolat/Decimal_to_degrees
import math
import tkinter
from tkinter import *
import threading
import time
from math import pi

focus_switch = "Degrees_Focus"

def window_focus():
    while True:
        global focus_switch
        widget = window.focus_get()

        if str(widget) == ".!labelframe2.!entry" or ".!labelframe2.!entry2" or ".!labelframe2.!entry3":
            focus_switch = "Degrees_Focus"
        if str(widget) == ".!labelframe3.!entry2":
            focus_switch = "Rads_Focus"
        if str(widget) == ".!labelframe3.!entry":
            focus_switch = "Grads_Focus"
        if str(widget) == ".!labelframe4.!entry":
            focus_switch = "Decimal_Focus"
        time.sleep(0.1)


def calculations():
    while True:
        global focus_switch,result_decimal, result_degrees, result_minutes, result_seconds, result_rads, result_grads

        user_input_decimal = str(decimal_entry_box.get())
        user_input_degrees = str(degrees_entry_box.get())
        user_input_minutes = str(minutes_entry_box.get())
        user_input_seconds = str(seconds_entry_box.get())
        user_input_rads = str(rads_entry_box.get())
        user_input_grads = str(grads_entry_box.get())

        user_input_decimal = user_input_decimal.replace(",", ".")
        user_input_degrees = user_input_degrees.replace(",", ".")
        user_input_minutes = user_input_minutes.replace(",", ".")
        user_input_seconds = user_input_seconds.replace(",", ".")
        user_input_rads = user_input_rads.replace(",", ".")
        user_input_grads = user_input_grads.replace(",", ".")

        if focus_switch == "Decimal_Focus":
            try:
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
                    result_rads = float(user_input_decimal) * (math.pi / 180)
                    result_grads = float(user_input_decimal) * (200 / 180)
                except ValueError:
                    decimal_entry_box.delete(0, tkinter.END)
                    degrees_entry_box.delete(0, tkinter.END)
                    minutes_entry_box.delete(0, tkinter.END)
                    seconds_entry_box.delete(0, tkinter.END)

                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, str(result_angle))
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, str(result_minutes))
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, str(result_seconds))
                rads_entry_box.delete(0, tkinter.END)
                rads_entry_box.insert(0, str(f'{result_rads:.15f}'))
                grads_entry_box.delete(0, tkinter.END)
                grads_entry_box.insert(0, str(f'{result_grads:.15f}'))
                time.sleep(0.1)
            except ValueError:
                decimal_entry_box.delete(0, tkinter.END)
                decimal_entry_box.insert(0, "")
                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, "")
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, "")
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, "")


        if focus_switch == "Degrees_Focus":
            try:
                result_decimal = (float(user_input_degrees) if user_input_degrees != "" else 0.0) + \
                                ((float(user_input_minutes)/60) if user_input_minutes != "" else 0.0) + \
                                ((float(user_input_seconds)/3600) if user_input_seconds != "" else 0.0)
                result_rads = result_decimal * (math.pi/180)
                result_grads = result_decimal * (200/180)

            except ValueError:
                decimal_entry_box.delete(0, tkinter.END)
                decimal_entry_box.insert(0, "")
                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, "")
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, "")
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, "")


            decimal_entry_box.delete(0, tkinter.END)
            decimal_entry_box.insert(0, str(result_decimal))
            rads_entry_box.delete(0, tkinter.END)
            rads_entry_box.insert(0, str(f'{result_rads:.15f}'))
            grads_entry_box.delete(0, tkinter.END)
            grads_entry_box.insert(0, str(f'{result_grads:.15f}'))
            time.sleep(0.1)


        if focus_switch == "Rads_Focus":
            try:
                result_decimal = float(user_input_rads) * (180/pi)
                result_grads = result_decimal * (200/180)
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

                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, str(result_angle))
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, str(result_minutes))
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, str(result_seconds))

            except ValueError:
                decimal_entry_box.delete(0, tkinter.END)
                decimal_entry_box.insert(0, "")
                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, "")
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, "")
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, "")
                grads_entry_box.delete(0, tkinter.END)
                grads_entry_box.insert(0, "")
                rads_entry_box.delete(0, tkinter.END)
                rads_entry_box.insert(0, "")


            decimal_entry_box.delete(0, tkinter.END)
            decimal_entry_box.insert(0, str(result_decimal))
            grads_entry_box.delete(0, tkinter.END)
            grads_entry_box.insert(0, str(f'{result_grads:.15f}'))
            time.sleep(0.1)

        if focus_switch == "Grads_Focus":
            try:
                result_decimal = float(user_input_grads) * (180/200)
                result_rads = result_decimal * (pi/180)
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

                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, str(result_angle))
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, str(result_minutes))
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, str(result_seconds))

            except ValueError:
                decimal_entry_box.delete(0, tkinter.END)
                decimal_entry_box.insert(0, "")
                degrees_entry_box.delete(0, tkinter.END)
                degrees_entry_box.insert(0, "")
                minutes_entry_box.delete(0, tkinter.END)
                minutes_entry_box.insert(0, "")
                seconds_entry_box.delete(0, tkinter.END)
                seconds_entry_box.insert(0, "")
                grads_entry_box.delete(0, tkinter.END)
                grads_entry_box.insert(0, "")
                rads_entry_box.delete(0, tkinter.END)
                rads_entry_box.insert(0, "")


            decimal_entry_box.delete(0, tkinter.END)
            decimal_entry_box.insert(0, str(result_decimal))
            rads_entry_box.delete(0, tkinter.END)
            rads_entry_box.insert(0, str(f'{result_rads:.15f}'))
            time.sleep(0.1)

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


window = Tk()
window.title("Vyrobené pre KMS <3")
window.geometry("553x315")
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

frame7 = LabelFrame(window, bg="green", bd=0)
frame7.place(x=220, y=300)

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
grads_entry_box = Entry(frame3, bd=3, width=20, font=('Arial', 10, 'bold'))
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

rads_entry_box = Entry(frame3, bd=3, width=20, font=('Arial', 10, 'bold'))
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

addition = Label(frame7,
              text="Radiany a gradiany pridane na poziadavku R. Dubravickeho.",
              font=('Arial',8,'bold'),
              fg='black',
              bg='gray',
              bd=0,
              padx=0,
              pady=0,
              )
addition.grid(row=0, column=0)


f = threading.Thread(name='focus', target=window_focus)
f.daemon = True
f.start()

t = threading.Thread(name='calculations', target=calculations)
t.daemon = True
t.start()

n = threading.Thread(name='noRevolutions', target=no_revolutions)
n.daemon = True
n.start()

window.mainloop()
