def convert_temperature():
    user_input = input("Enter temperature with unit : ").strip().upper()

    try:
        temp_value, unit = user_input[:-1].strip(), user_input[-1]
        temp = float(temp_value)

        if unit == 'C':
            converted = (temp * 9/5) + 32
            print(f"{temp}°C is equal to {converted:.2f}°F")
        elif unit == 'F':
            converted = (temp - 32) * 5/9
            print(f"{temp}°F is equal to {converted:.2f}°C")
        else:
            print("Invalid unit. Please end with 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid input. Format must be like: 100 C or 212 F")

convert_temperature()