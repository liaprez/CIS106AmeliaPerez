#input phase
lastname = input("Enter last name: ")
depnum = input("Enter number of dependants: ")
grossincome = float(input("Enter gross income: $"))

#process phase
adjgrossincome = grossincome - 12000.00 * float(depnum)

if adjgrossincome > 50000.00:
  tax = adjgrossincome * .2
else:
  tax = adjgrossincome * .1

if tax < 0.00:
  tax = 100

#output phase
print("Last name: ",lastname)
print("Gross income: $", grossincome)
print("Number of dependants: ", depnum)
print("Adjusted gross income: $", adjgrossincome)
print("Income tax: $", tax)
