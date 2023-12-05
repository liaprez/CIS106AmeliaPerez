def CompBatAvg(h, b):
  batavg = h/b
  return batavg

c = 0
r = input("Do you want to calculate batting average? (y/n) ")

while r == "y":
  ln = input("Enter player's last name: ")
  h = int(input("Enter the number of hits: "))
  b = int(input("Enter the number of at bats: "))
  batavg = CompBatAvg(h, b)
  print(ln, "'s batting average is: ", batavg)
  c = c + 1
  r = input("Do you want to calculate batting average? (y/n) ")
  
print("You calculated batting average for ", c, " players!")