from time import sleep

def celsius_fahrenheit(celsius):
    return f"{(celsius * 9/5) + 32:.2f} °F"

def fahrenheit_celsius(fahrenheit):
    return f"{(fahrenheit - 32) * 5/9:.2f} °C"

def kelvin_celsius(kelvin):
    return f"{kelvin - 273.15:.2f} °C"

def celsius_kelvin(celsius):
    return f"{celsius + 273.15:.2f} K"

def kelvin_fahrenheit(kelvin):
    return f"{(kelvin - 273.15) * 9/5 + 32:.2f} °F"

def fahrenheit_kelvin(fahrenheit):
    return f"{(fahrenheit - 32) * 5/9 + 273.15:.2f} K"

def converter_selection(select):
    try:
        match select:
            case 1:
                temp = float(input("Please input a temp in Celsius: "))
                return celsius_fahrenheit(temp)
            case 2:
                temp = float(input("Please input a temp in Fahrenheit: "))
                return fahrenheit_celsius(temp)
            case 3:
                temp = float(input("Please input a temp in Kelvin: "))
                return kelvin_celsius(temp)
            case 4:
                temp = float(input("Please input a temp in Celsius: "))
                return celsius_kelvin(temp)
            case 5:
                temp = float(input("Please input a temp in Kelvin: "))
                return kelvin_fahrenheit(temp)
            case 6:
                temp = float(input("Please input a temp in Fahrenheit: "))
                return fahrenheit_kelvin(temp)
            case 7:
                print("Exiting Program...")
                exit()
            case _:
                return "Invalid input"
    except ValueError as e:
        return f"Invalid input, ensure that only numerical values are entered: {e}"

while True:
    try:
        select = int(input("""\bPlease choose a converter:
[1] Celsius to Fahrenheit
[2] Fahrenheit to Celsius
[3] Kelvin to Celsius
[4] Celsius to Kelvin
[5] Kelvin to Fahrenheit
[6] Fahrenheit to Kelvin
[7] Exit
Input: """))
        result = converter_selection(select)
        sleep(1)
        print("Result:", result)
        sleep(1)

    except ValueError:
        print("Please enter a valid number between 1 and 7.")
