# Decimal to Degrees Converter
# TODO: Make GUI
# TODO: Make final angle... if its 700°, it shows 340°. or if its 700.50, it shows 340,50.

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
