#input phase
firstname = input("Enter first name: ")
stepswalked = float(input("Enter number of steps walked in a day: "))

#process phase
caloriesburned = stepswalked*(.25)

#output phase
print(firstname, "burned ",caloriesburned, " calories.")