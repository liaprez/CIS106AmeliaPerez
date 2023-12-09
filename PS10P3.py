np = 0.0
msrp = 0.0
def CompOTD(msrp, make, model):
  if make == "Honda" and model == "Accord":
   np = msrp - (.1 * msrp)
  elif make == "Toyota" and model == "RAV4":
   np = msrp - (.15 * msrp)
  elif model == "Electric":
    np = msrp - (.3 * msrp)
  else:
   np = msrp - (.05 * msrp)
  return np

def CompTP(np, msrp):
  tp = np + (np * .07)
  return tp

r = input("Do you want to calculate the car's price? (Yes/No) ")

while r == "Yes":
  msrp = float(input("What is the MSRP? "))
  make = input("What is the make of the car? ")
  model = input("What is the model of the car? ")
  np = CompOTD(msrp, make, model)
  print("The new price is: $", np)
  r = input("Do you want to calculate the car's price? (Yes/No) ")

tp = CompTP(np, msrp)
print("The total, final price is: $ ", tp)