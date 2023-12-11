def displayarrays(ln, examscore):
  for i in range(0, 10, 1):
    print(ln[i], "received an exam score of ", examscore[i])


ln = ["Adams", "Baker", "Clark", "Davis", "Evans", 
        "Jones", "Gordon", "Henry","Smith", "Thomas"]
examscore = [90.0, 92.1, 91.2, 92.5, 94.5,97.5, 99.2, 97.3, 98.7, 96.4]
print("List of names with respective score: ")
displayarrays(ln, examscore)