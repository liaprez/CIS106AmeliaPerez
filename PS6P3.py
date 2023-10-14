#input phase
principle = float(input("Enter the principle amount: "))
maturity = int(input("Enter year to maturity of CD:  "))

#process phase
if principle > 100000 and maturity == 5:
  interestrate = .06
elif principle >= 50000 and principle <= 100000 and maturity == 10:
  interestrate = .05
elif principle >= 50000 and principle <= 100000 and maturity == 5:
  interestrate = .04
else:
  interestrate = .02

interestamount = principle * interestrate

#output phase
print("Principle amount: $ ", principle)
print("Interest rate: " , interestrate)
print("Interest amount for the first year: $ ", interestamount)