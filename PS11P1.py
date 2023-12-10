def discounts(qty, price, discrate):
  total = qty * price
  discamt = discrate * total
  discprice = total - discamt
  
  return discamt, discprice

qty = float(input("Enter the quantity: "))
price = float(input("Enter the unit price: $"))
discrate = float(input("Enter the discount rate (%): "))
discamt, discprice = discounts(qty, price, discrate)

print("There was a quantity of", qty, "units at $", price, "each.")
print("Discounted amount: $", discamt)
print("Discounted price: $", discprice)