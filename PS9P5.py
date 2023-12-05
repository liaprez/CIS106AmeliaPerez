def CompTuOw(ch, dc, cpc):
  
  if dc == "I":
    cpc = 250.00
  else:
    cpc = 550.00

  tuow = ch * cpc
    
  return tuow
    
ttui = 0.0
r = input("Do you want to calculate tuition owed? (y/n): ")

while r == "y":
  ln = input("Enter student's last name: ")
  ch = int(input("Enter number of credit hours: "))
  dc = input("Enter student's district code: ")
  cpc = 0.0
  tuow = CompTuOw(ch, dc, cpc)
  print(ln, " tuition owed: $", tuow)
  ttui = ttui + tuow

  r = input("Do you want to calculate tuition owed? (y/n): ")

print("Total tuition owed: $", ttui) 