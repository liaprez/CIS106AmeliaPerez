#input phase
partnumber = int(input("Enter the part number: "))
quantity = input("Enter the quantity of parts")

#process phase
if partnumber == 10 or partnumber == 55:
  unitprice = 1.00
elif partnumber == 99:
  unitprice = 2.00
elif partnumber == 80 or partnumber == 70:
  unitprice = 3.00
else:
  unitprice = 5.00

total = float(quantity) * unitprice

#process phase
print("Part number:  ", partnumber)
print("Quantity:     ", quantity)
print("Unit price: $ ", unitprice)
print("Total:      $ ", total)