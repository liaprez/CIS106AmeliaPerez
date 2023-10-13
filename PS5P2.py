#input phase
item = input ("Enter item (as a capital letter): ")
itemquantity = input("Enter item amount: ")

#process phase
if item == "A":
  unitprice = 10
else:
  unitprice = 20

extprice = float(itemquantity) * float(unitprice)

#output phase
print ("Item: ", item)
print ("Unit price: $", unitprice)
print ("Extended price: $", extprice)