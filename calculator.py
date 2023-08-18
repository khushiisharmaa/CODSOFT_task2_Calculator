def calc_unique(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        if b != 0:
            return a / b
        else:
            return "Infinity and beyond!"
    else:
        return "Unknown operation"

while True:
    print("Welcome to CalcUniquely!")
    print("Available operations:")
    print(" - 'add' for addition")
    print(" - 'subtract' for subtraction")
    print(" - 'multiply' for multiplication")
    print(" - 'divide' for division")
    print(" - 'exit' to quit")

    operation = input("Enter operation: ")

    if operation == 'exit':
        print("Goodbye!")
        break  # Exit the loop if the user chooses to quit

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = calc_unique(num1, num2, operation)
    print("Result:", result)
