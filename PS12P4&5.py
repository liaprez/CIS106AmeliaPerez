def displaynames(ln, batavg):
  l = len(ln)
  print("Lastname and batting average:")
  for x in range(0,l,1):
    print(x, " " , ln[x], "batting average: " , batavg[x])

def seqsearch(ln, sname):
  l = len(ln)
  i = -1
  for y in range(0,l,1):
   if ln[y] == sname:
     i = y

  return i


f = open("datafilePS12P4.txt", "r")

#define arrays
ln = []
batavg = []

lastname = f.readline()

while lastname != "":
  ln.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  batavg.append(s)
  lastname = f.readline()
f.close()
displaynames(ln, batavg)

r = input("Do you want to search for a name? (Yes/No) ")

while r == "Yes":
  sname = input("Enter last name to search for: ")
  i = seqsearch(ln, sname)
  if i == -1:
    print(sname, "not found.")
  else:
    print (ln[i], " has a batting average of ", batavg[i])

  r = input("Do you want to search for another name? (Yes/No) ")