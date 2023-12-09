fp = 0.0
def CompNMF(m, s):
  
  if m == "Jan" or "Feb" or "Mar":
    fp = .1
  elif m == "Apr" or "May" or "Jun":
    fp = .15
  elif m == "Jul" or "Aug" or "Sep":
    fp = .2
  elif m == "Oct" or "Nov" or "Dec":
    fp = .25
  else:
    print("Re-enter forecasting period in 'Mmm' format")
    
  nmf = s * (1 + fp)
  return nmf

r = input("Do you want to compute next month's forecast? (Yes/No) ")

while r == "Yes":
  ln = input("Enter last name: ")
  m = input("Enter forecasting month: ")
  s = float(input("Enter sales: "))
  nmf = CompNMF(m, s)
  print(ln, "calculated a monthly forecast of $", nmf, "for the month of ", m)
  r = input("Do you want to compute next month's forecast? (Yes/No)")

print(ln, "calculated a monthly forecast of $", nmf, "for the month of ", m)