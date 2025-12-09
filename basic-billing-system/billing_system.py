itemname = input("Enter the item: ")
quantity = int(input("Enter Quantity "))
price = float(input("Enter Price per item "))
total = quantity*price
gst = total*0.8
final = total+gst
print("Billing System")
print("Total: ",total)
print("GST (18%): ",gst)
print("Final Amount: ",final)
