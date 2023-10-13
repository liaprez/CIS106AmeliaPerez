#input phase
numberofbooks = input("Enter the number of books ordered: ")
costperbook = input("Enter the cost per book: ")

#process phase
ordertotal = float(numberofbooks) * float(costperbook)
if ordertotal > 50.00:
  shipping = 0.00
else:
  shipping = 25.00
  
#output phase
print("Order total: $", ordertotal)
print("Shipping: $", shipping)