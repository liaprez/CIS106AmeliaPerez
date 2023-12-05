def CompMpG(m, g):
  mpg = m/g
  return mpg

t = 0
r = input("Do you want to calculate MPG? (y/n) ")

while r == "y":
  dc = input("Enter the destination city: ")
  m = int(input("Enter the miles traveled: "))
  g = int(input("Enter the gallons used: "))
  mpg = CompMpG(m, g)
  print("You travelled ", m, " miles to ", dc)
  print("Miles per gallon: ", mpg)
  t = t + 1
  r = input("Do you want to calculate MPG? (y/n) ")

print("You calculated the mpg for", t, "trip(s)!")