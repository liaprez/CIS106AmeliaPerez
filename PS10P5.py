def CompAV(c, mv):
  if c == "Cook":
    av = mv * .9
  elif c == "DuPage":
    av = mv * .8
  elif c == "McHenry":
     av = mv * .75
  elif c == "Kane":
    av = mv * .6
  else:
    av = mv * .7
  return av


r = input("Do you want to calculate the assessed value of a home? (Yes/No)")
totv = 0.0

while r == "Yes":
  c = input("What is the county? ")
  mv = float(input("What is the home's market value?: $"))
  av = CompAV(c, mv)
  print("The assessed value of the home is: $", av)
  r = input("Do you want to calculate the assessed value of a home? (Yes/No)")
  totv = totv +av
print("The final assessed value of the homes is: $", totv)