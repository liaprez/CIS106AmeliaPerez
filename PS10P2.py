SF = 0.0
def CompSF(length, width, height):
  SF = (2 * (length * width) + 2 * (length * height) + 2 * (width * height))
  return SF

def CompNumGal(tsf):
  NumGal = tsf/50
  return NumGal

tsf = 0.0
r = input("Do you want to calculate square footage? (Yes/No) ")

while r == "Yes":
  length = int(input("Enter the length of the room: "))
  width = int(input("Enter the width of the room: "))
  height = int(input("Enter the height of the room: "))
  SF = CompSF(length, width, height)
  print("The square footage of the room is", SF)
  tsf = tsf + SF
  r = input("Do you want to calculate square footage? (Yes/No)")

NumGal = CompNumGal(tsf)
print("The number of gallons needed ", NumGal)