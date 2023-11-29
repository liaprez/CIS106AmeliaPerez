counter = 0
sumdisc = 0.0

response = input("Do you want to compute order total? (Yes or No) ")

while response == "Yes":
  counter = counter + 1
  qty = int(input("Enter quantity: "))
  price = float(input("Enter price: "))
  extprice = qty * price
  if extprice > 10000.00:
    discamt = extprice * .25
  else: discamt = extprice * .1
  total = extprice - discamt
  sumdisc = sumdisc + discamt
  print("Extended price: $", extprice)
  print("Discount amount: $", discamt)
  print("Total order amount: $", total)
  response = input("Do you want to compute order total? (Yes or No) ")

print("Total discounts: $", sumdisc)