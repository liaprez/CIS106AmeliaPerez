#input phase
appliancename = input("Enter the appliance name: ")
appliancecost = input("How much did the appliance cost? :")

#process phase
if float(appliancecost) > 1000.00:
  warrantycost = float(appliancecost) * (.10)
else:
  warrantycost = float(appliancecost) * (.05)

total = float(appliancecost) + float(warrantycost)

#output phase
print("Appliance: ", appliancename)
print("Cost of appliance: $", appliancecost)
print("Cost of warranty: $", warrantycost)
print("Total cost: $", total)