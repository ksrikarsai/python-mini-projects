def km_to_miles(km):
    return km * 0.621371
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def kg_to_pounds(kg):
    return kg * 2.20462
print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")
choice = int(input("Enter your choice 1,2,3: "))
if choice == 1:
    km = float(input("Enter distance in kilometers: "))
    print(f"Miles: {km_to_miles(km)}")
elif choice == 2:
    c = float(input("Enter temperature in Celsius: "))
    print(f"Fahrenheit: {celsius_to_fahrenheit(c)}")
elif choice == 3:
    kg = float(input("Enter weight in kilograms: "))
    print(f"Pounds: {kg_to_pounds(kg)}")
else:
    print("Invalid Choice")
