# Declare the functions beforehand to be called in later on 
def add_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num1, num2):
    return num1 - num2
def multiply_numbers(num1, num2):
    return num1 * num2
def divide_numbers(num1, num2):
    return num1 / num2

# Ask the user to input the value of two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

# Makes the user select an operation
print ("Choose an operation:")
print ("1 - Addition")
print ("2 - Subtraction")
print ("3 - Multiplication")
print ("4 - Division")
operation = int(input("Enter chosen operation:"))

# Specific fucntion gets called on depending on the chosen operation
if operation == 1:
    print (f"The sum is {add_numbers(num1, num2)}")
elif operation == 2:
    print (f"The difference is {subtract_numbers(num1, num2)}")
elif operation == 3:
    print (f"The product is {multiply_numbers(num1, num2)}")
elif operation == 4:
    if num2 == 0:
        print ("Cannot divide with 0")
    else:
        print (f"The quotient is {divide_numbers(num1, num2)}")
else:
    print ("Invalid operation")