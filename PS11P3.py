def sales_rep(sales):
  if sales > 100000:
    com = sales * .10
  elif sales <= 100000:
    com = sales * .05
  nyt = sales * .05
  return com, nyt

ln = input("Enter salesperson's last name: ")
sales = float(input("Enter sales amount: "))
com, nyt = sales_rep(sales)
print(ln, "'s commission earned: $", com)
print("Next year's target: $", nyt)