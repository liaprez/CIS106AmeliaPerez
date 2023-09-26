#input phase
fixedcosts = float(input("Enter fixed costs: $"))
unitprice = float(input("Enter price per unit: $"))
unitcost = float(input("Enter cost per unit: $"))

#process phase
breakevenpoint = (fixedcosts/(unitprice - unitcost))

#output phase
print("The break-even point is: ",breakevenpoint)