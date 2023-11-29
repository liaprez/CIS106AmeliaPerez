counter = 0
sumgrosspay = 0.0

response = input("Do you want to compute your gross pay? (Yes or No)")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter last name: ")
  hours = int(input("Enter hours worked: "))
  rate = float(input("Enter hourly rate: "))
  if hours >= 40:
    grosspay = (40 * rate) + ((hours - 40) * (rate * 1.5))
  else:
    grosspay = rate * hours
  print(lastname, " gross pay is: $", grosspay)
  sumgrosspay = sumgrosspay + grosspay
  response = input("Do you want to compute your gross pay? (Yes or No)")

print("Sum of pay roll: $", sumgrosspay)
print("Number of employees: ", counter)
avggrosspay = sumgrosspay / counter
print("Average gross pay is: $", avggrosspay)