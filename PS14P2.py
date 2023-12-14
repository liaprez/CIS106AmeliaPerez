class Student:
  def __init__(self, fn, ln,
               dc, enrolledcredits):
    self.fn = fn
    self.ln = ln
    self.districtcode = dc
    self.enrolledcredits = enrolledcredits

  def tuitionowed(self, dc, enrolledcredits):
    if dc == "I":
     to = enrolledcredits * 250.00
    else:
      to = enrolledcredits * 500.00
    return to

  def fullname(self):
    return "{} {}".format(self.fn, self.ln)

stu_1 = Student("John", "Doe", "I", 9)
stu_2 = Student("Jane", "Doe", "O", 9)

stu_1.fullname()
print(Student.fullname(stu_1))
print("Enrolled credits: ", stu_1.enrolledcredits)
print("District code: ", stu_1.districtcode)
print("Tuition owed: $", stu_1.tuitionowed(stu_1.districtcode, stu_1.enrolledcredits))
print(" ")
stu_2.fullname()
print(Student.fullname(stu_2))
print("Enrolled credits: ", stu_2.enrolledcredits)
print("District code: ", stu_2.districtcode)
print("Tuition owed: $", stu_2.tuitionowed(stu_2.districtcode, stu_2.enrolledcredits))