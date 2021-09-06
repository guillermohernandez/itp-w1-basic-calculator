"""This is the entry point of the program."""


def basic_calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
        
    elif operation == "subtract":
        return num1 -num2
    
    elif operation == "multiply":
        return num1 * num2
        
    elif operation == "divide":
        return num1 / num2
    
    elif operation == "square1":
        return num1*num1
    
    elif operation == "square2":
        return num2*num2
        
    else:
        return "Invalid operation"
