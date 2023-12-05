def CompExtPrice(qty, up):
  ep = qty * up
  
  if ep > 10000.00:
    discamt = ep * (.1)
  else:
    discamt = 0.0

  nep = ep - discamt
  return nep

tep = 0.0
r = input("Do you want to compute extended price? (y/n) ")

while r == "y":
  qty = float(input("Enter quantity: "))
  up = float(input("Enter unit price: $"))
  nep = CompExtPrice(qty, up)
  tep = tep + nep
  print("Extended price is: $", nep)
  r = input("Do you want to compute extended price? (y/n) ")

print("Total extended price is: $" , tep)