def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation. Please choose add, subtract, multiply, or divide."

from arithmetic_operations import perform_operation

# Prompt the user for input
print("Welcome to the Arithmetic Operations Program!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose operation - add, subtract, multiply, divide: ").strip().lower()

# Call the function and print the result
result = perform_operation(num1, num2, operation)

print("Result:", result)

     