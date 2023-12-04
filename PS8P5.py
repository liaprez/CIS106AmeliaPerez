t = open("d5.txt", "r")

#initialize counters and sums to 0
totaltuition = 0.0
c = 0

#get first data line
ln = str(t.readline().rstrip('\n'))

while ln != "":
  dcode = str(t.readline().rstrip('\n'))
  credits = float(t.readline())
  
  if dcode == "I":
    cpc = 250.00
  else:
    cpc = 500.00

  tuition = credits * cpc
  c = c + 1
  totaltuition = totaltuition + tuition
  
  print("Student: ",ln)
  print("Credits taken: " ,credits)
  print("Tuition owed: ", tuition)
  print(" ")
  
  ln = str(t.readline().rstrip('\n'))

t.close()

print("Total tuition owed: ", totaltuition)
print("Number of students: ", c)