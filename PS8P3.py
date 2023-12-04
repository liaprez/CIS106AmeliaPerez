d = open("d3.txt", "r")

#initialize sums to 0
tb = 0.0

#get first data line
ln = str(d.readline().rstrip('\n'))

while ln !="":
  salary = float(d.readline())
  
  if salary >= 100000.00:
    b = salary * .2
  elif salary == 50000.00:
    b = salary * .15
  else:
    b = salary * .1

  tb = tb + b

  print("Employee last name: ", ln)
  print("Employee salary: $", salary)
  print(ln, "'s bonus: $", b)
  print("")

  
  ln = str(d.readline().rstrip('\n'))

d.close()

print("Total bonus paid out: $", tb)