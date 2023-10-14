#input phase
lastname = input("Enter last name: ")
salary = float(input("Enter salary: $ "))
joblevel = int(input("Enter job level: "))

#process phase
if joblevel >= 10:
  bonusrate = .25
elif joblevel >= 5 and joblevel <= 9:
  bonusrate = .20
else:
  bonusrate = .10

bonus = salary * bonusrate

#output phase
print("Employee last name: ", lastname)
print("Bonus: $ ", bonus)