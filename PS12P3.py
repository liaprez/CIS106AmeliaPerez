def displaynames(ln, score):
  for i in ln, score:
    print(i)
    
  l = len(ln)
  print("Lastname and respective score")
  for x in range(0,l,1):
    print(x, " " , ln[x], "received a score of: " , score[x])

def hilow(ln, score):
  l = len(ln)
  hiscore = -1.0
  lowscore = 99999999.99
  for y in range (0,l,1):
    if float(score[y]) > float(hiscore):
      hiindex = y
      hiscore = score[y]

    if float(score[y]) < float(lowscore):
      loindex = y
      lowscore = score[y]

  print("Highest score:", ln[hiindex], score[hiindex])
  print("Lowest score:", ln[loindex], score[loindex]) 

f = open("datafilePS12P3.txt", "r")

#define arrays
ln = []
score = []

lastname = f.readline()

while lastname != "":
  ln.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  score.append(s)
  lastname = f.readline()
f.close()
displaynames(ln, score)
hilow(ln, score)