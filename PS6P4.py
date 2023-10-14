#input phase
tickets =int(input("Enter the number of tickets: "))

#process phase
if tickets >=25:
  price = 50.00
elif tickets >=10 and tickets <= 24:
  price = 60.00
elif tickets >=5 and tickets <= 9:
  price = 70.00
else:
  price = 75.00

total = tickets * price

#output phase
print("The number of tickets: ", tickets)
print("The price per ticket: $ ", price)
print("The total price: $ ", total)