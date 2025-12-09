print("Area of Shapes")
choice = int(input("Enter 1 for Circle, 2 for Rectangle, 3 for Square and 4 for Triangle "))
if(choice==1):
    r = float(input("Enter radius "))
    print("The area of circle for given dimension",r,"is ",3.14*(r**2))
elif(choice==2):
    l = int(input("Enter length "))
    b = int(input("Enter breadth "))
    print("The area of rectangle for given dimensions",l,"and",b,"is ",l*b)
elif(choice==3):
    s = int(input("Enter side "))
    print("The area of sqaure for given dimension",s,"is ",s**2)
elif(choice==4):
    b = int(input("Enter breadth "))
    h = int(input("Enter height "))
    print("The area of rectangle for given dimensions",b,"and",h,"and","is ",0.5*b*h)
else:
    print("Choice is wrong")
