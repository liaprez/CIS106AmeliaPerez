#input phase
widgetqty = int(input("Enter the quantity of widgets:  "))

#process phase
if widgetqty > 10000:
  price = 10.00
elif widgetqty >= 5000 and widgetqty <= 10000:
  price = 20.00
else: 
  price = 30.00

extprice = price * widgetqty
tax = extprice * .07
total = extprice + tax

#output phase
print("The extended price is: $ ", extprice)
print("The tax is: $", tax)
print("The total price is: $ ", total)