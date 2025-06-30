try:
    while True:
        def celsius_fahrenheit(celsius):
            fahrenheit = (celsius * 9/5) + 32
            return f"{fahrenheit:.2f} °F"

        def fahrenheit_celsius(fahrenheit):
            celsius = (fahrenheit - 32) * 5/9
            return f"{celsius:.2f} °C"

        def kelvin_celsius(kelvin):
            celsius = kelvin - 273.15
            return f"{celsius:.2f} °C"

        def celsius_kelvin(celsius):
            kelvin = celsius + 273.15
            return f"{kelvin:.2f} K"

        def kelvin_fahrenheit(kelvin):
            fahrenheit = (kelvin - 273.15) * 9/5 + 32
            return f"{fahrenheit:.2f} °F"

        def fahrenheit_kelvin(fahrenheit):
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
            return f"{kelvin:.2f} K"

        def converter_selection(select):
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
                    exit()
                case _:
                    return "Invalid input"

        select = int(input("""Please choose a converter:
        [1] Celsius to Fahrenheit
        [2] Fahrenheit to Celsius
        [3] Kelvin to Celsius
        [4] Celsius to Kelvin
        [5] Kelvin to Fahrenheit
        [6] Fahrenheit to Kelvin
        [7] Exit
        Input: """))

        result = converter_selection(select)
        print("Result:", result)

except ValueError as e:
    print("Invalid input, ensure that only numerical values are entered:", e)