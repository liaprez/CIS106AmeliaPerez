def CompTP(dtc):
  if dtc >= 30:
    tp = 12.00
  elif dtc >= 20 and dtc <=29:
    tp = 10.00
  elif dtc >= 10 and dtc <=19:
    tp = 8.00
  else:
    tp = 5.00
  return tp


r = input("Do you want to calculate ticket price? (Yes/No) ")
totp = 0.0
tp = 0.0

while r == "Yes":
  dtc = int(input("Enter distance from downtown Chicago: "))
  tp = CompTP(dtc)
  print("The ticket price is: $", tp)
  r = input("Do you want to calculate ticket price? (Yes/No) ")
  totp = totp + tp
print ("The total for all calculated tickets is: $", totp)