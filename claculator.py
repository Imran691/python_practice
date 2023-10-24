
# class Calculator:
#     def add(self, x, y):
#         return x + y
    
#     def subtract(self, x, y):                                  
#         return x - y
    
#     def multiply(self, x, y):
#         return x * y
    
#     def divide(self, x, y):
#         if y == 0:
#             return "Cannot divide by zero"
#         return x / y

# # Create an instance of the Calculator class
# my_calculator = Calculator()

# while True:
#     print("Options:")
#     print("Enter 'add' for addition")
#     print("Enter 'subtract' for subtraction")
#     print("Enter 'multiply' for multiplication")
#     print("Enter 'divide' for division")
#     print("Enter 'quit' to end the program")

#     user_input = input(": ")

#     if user_input == "quit":
#         break

#     if user_input in ["add", "subtract", "multiply", "divide"]:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if user_input == "add":
#             result = my_calculator.add(num1, num2)
#         elif user_input == "subtract":
#             result = my_calculator.subtract(num1, num2)
#         elif user_input == "multiply":
#             result = my_calculator.multiply(num1, num2)
#         elif user_input == "divide":
#             result = my_calculator.divide(num1, num2)

#         print("Result:", result)
#     else:
#         print("Invalid input")

