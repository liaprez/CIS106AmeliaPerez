def CompGP(h, jc, rate):
  
  if jc == "L":
    rate = 25
  elif jc == "A":
    rate = 30
  elif jc == "J":
    rate = 50

  if h> 40:
    gp = (40 * rate ) + ((h - 40) * rate * 1.5)
  else:
    gp = h * rate
    
  return gp

tgp = 0
r = input("Do you want to compute gross pay? (y/n) ")

while r == "y":
  rate = float
  ln = input("Enter Last Name: ")
  h = int(input("Enter hours worked: "))
  jc = input("Enter job code: ")
  gp = CompGP(h, jc, rate)
  print("Employee: ", ln)
  print("Gross pay: ", gp)
  tgp = tgp + gp
  
  r = input("Do you want to compute gross pay? (y/n) ")

print("You calculated a total gross pay amount of $", tgp)