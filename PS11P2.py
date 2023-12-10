def exam_avg(exam1, exam2, exam3):
  sum = exam1 + exam2 + exam3
  avg = (sum/3)
  points = exam1 + exam2 + exam3
  return avg, points

ln = input("Enter last name: ")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))

avg, points = exam_avg(exam1, exam2, exam3)
print("Last name: ", ln)
print("Exam score average: ", avg)
print("Points total: ", points)