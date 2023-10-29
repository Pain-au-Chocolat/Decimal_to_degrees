# Decimal to Degrees Converter
# TODO: Make function to convert decimal to degrees and other way around
# TODO: Make GUI

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
    pass

decimal_to_degrees()
