def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
a = float(input("Enter First Number "))
b = float(input("Enter Second Number "))
choice = int(input("Enter 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division "))
if choice==1:
    print("The Addition of Two Numbers is ",add(a,b))
elif choice==2:
    print("The Subtraction of Two Numbers is ",subtract(a,b))
elif choice==3:
    print("The Multiplication of Two Numbers is ",multiply(a,b))
elif choice==4:
    print("The Division of Two Numbers is ",divide(a,b))
else:
    print("Invalid Choice")
