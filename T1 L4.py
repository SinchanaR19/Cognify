def basic_calculator():
    print("Basic Calculator")
    
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Error: Invalid operator.")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numeric values.")
basic_calculator()