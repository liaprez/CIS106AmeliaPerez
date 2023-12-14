class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@company.com"

  def br(self, rate):
    b = float(rate) * float(self.pay)
    return b

  def fullname(self):
    return "{} {}".format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

                 
emp_1.fullname()
print(Employee.fullname(emp_1))

print("Email: ", emp_1.email)
print("Pay: ", emp_1.pay)
print("10% bonus: ", emp_1.br(.10))
print("20% bonus: ", emp_1.br(.20))