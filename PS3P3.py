#input phase
mealtotal = float(input("Enter meal total: "))

#process phase
tipat15 = mealtotal*(.15)
totaland15 = mealtotal + tipat15
tipat18 = mealtotal*(.18)
totaland18 = mealtotal + tipat18
tipat20 = mealtotal*(.2)
totaland20 = mealtotal + tipat20

#output phase
print("With 15% Tip: ")
print()
print("Meal total: $",mealtotal)
print()
print("Tip amount: $",tipat15)
print()
print("Total with Tip: $",totaland15)
print()
print()
print("With 18% Tip: ")
print()
print("Meal total: $",mealtotal)
print()
print("Tip amount: $",tipat18)
print()
print("Total with Tip: $",totaland18)
print()
print()
print("With 20% Tip: ")
print()
print("Meal total: $",mealtotal)
print()
print("Tip amount: $",tipat20)
print()
print("Total with Tip: $",totaland20)