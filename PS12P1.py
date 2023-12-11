def displayarrays(ln):
  for i in range(0, 10, 1):
    print(ln[i])

def rdisplay(ln):
  for i in range (9, -1, -1):
    print(ln[i])

ln = ["Adams", "Baker", "Clark", "Davis", "Evans", 
        "Jones", "Gordon", "Henry","Smith", "Thomas"]

print("List of names: ")
displayarrays(ln)
print("List of names in reverse order: ")
rdisplay(ln)