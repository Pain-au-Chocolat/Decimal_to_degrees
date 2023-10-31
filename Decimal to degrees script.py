# Decimal to Degrees Converter
# TODO: Make GUI compatible with functions
# TODO: Make final angle... if its 700°, it shows 340°. or if its 700.50, it shows 340,50.
from tkinter import *


def decimal_to_degrees():
    user_input = (input("Input your angle in decimal form: "))
    user_input = user_input.replace(",", ".")
    separator = "."
    if separator not in user_input:
        user_input = user_input + ".0"

    result_angle = user_input.split(separator, 1)[0]

    minutes_decimal_part = user_input.split(separator, 1)[-1]
    minutes_decimal_part = ("0." + str(minutes_decimal_part))
    minutes_decimal_part = float(minutes_decimal_part)
    minutes = minutes_decimal_part * 60
    result_minutes = str(minutes).split(separator, 1)[0]

    seconds_decimal_part = str(minutes).split(separator, 1)[-1]
    seconds_decimal_part = ("0." + str(seconds_decimal_part))
    seconds_decimal_part = float(seconds_decimal_part)
    seconds = seconds_decimal_part * 60
    result_seconds = str(seconds).split(separator, 1)[0]

    print(result_angle + "°" + result_minutes + "'" + result_seconds + '"')

def degrees_to_decimal():
    user_input_degrees = input("Input your degrees: ")
    user_input_minutes = input("Input your minutes: ")
    user_input_seconds = input("Input your seconds: ")

    result_decimal = float(user_input_degrees) + (float(user_input_minutes)/60) + (float(user_input_seconds)/3600)
    print(result_decimal)

window = Tk()
window.title("Made for KMS <3")
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



window.mainloop()
