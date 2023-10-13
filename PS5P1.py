#input process
qty = float(input("Enter a quantity of the item: "))

#process phase
if qty >= 1000:
  unitprice = 3.00
else:
  unitprice = 5.00

extprice = qty * unitprice

tax = extprice*(.07)

total = extprice+tax

#output phase
print("Quantity of items: ",qty)
print("Price per unit: $", unitprice)
print("Extended price: $", extprice)
print("Tax: $", tax)
print("Total price: $", total)