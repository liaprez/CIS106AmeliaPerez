response = input("Do you want to compute the annual interest? (Yes or No) ")

while response == "Yes":
  p = float(input("Enter principle: "))
  r = float(input("Enter interest rate: "))
  t = 0.0
  for count in range (1,6, ):
    a = p * r
    eb = p + a
    print(count, "  ", p, "  ", eb)
    p = eb
    t = t + a
    
  response = input("Do you want to compute the annual interest? (Yes or No) ")
print("Total interest earned", t)