def add(x,y):
    """Addition
    Give two numbers as argument It will add
    """
    return x+y

def subtract(x,y):
    """Subtraction
    Give two numbers as argument It will subtract the numbers and give answers
    """
    if(x>y):
        return x-y
    else:
        return y-x

def multiply(x,y):
    """Multiplication
    Give two numbers as argument It will multiply the numbers and provide result"""
    return x*y

def divide(x,y):
    """Division
    Give two numbers as argument It will give division number
    """
    if y==0:
        print("Division by zero error")
    else:
        return x/y


def percentage(x,y):
    """Modulo
    Give two numbers as argument It will produce reminder
    """
    return x/100*y