counter = 0

response = input("Do you want to compute your average score? (Yes or No) ")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter student last name: ")
  score1 = float(input("Enter exam score 1: "))
  score2 = float(input("Enter exam score 2: "))
  average = (score1 + score2)/2
  print(lastname, " has average of ", average)
  response = input("Do you want to compute another average score? (Yes or No) ")
  
print("Number of students", counter)