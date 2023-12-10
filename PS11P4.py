def bow_avg(score1, score2, score3, hc):
  sum = score1 + score2 + score3
  avg = sum / 3
  havg = (sum + hc) / 3
  return avg, havg

ln = input("Enter bowler's last name: ")
score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))
hc = float(input("Enter handicap: "))
avg, havg = bow_avg(score1, score2, score3, hc)
print("Bowler: ", ln)
print("Average: ", format(float(avg), '10,.2f'))
print("Handicap: ", format(float(havg), '10,.2f'))