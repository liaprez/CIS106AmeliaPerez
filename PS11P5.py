total = 0.0
tax = 0.0
def CompTotal (qty, price):
  global total
  total = qty * price
  global tax
  tax = total * .07
  return

qty = float(input("Enter quantity of item: "))
price = float(input("Enter price per unit: "))
CompTotal(qty, price)
print("Total: ", format(float(total), '10,.2f'))
print("Tax: ", format(float(tax), '10,.2f'))