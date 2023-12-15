class Car:
  def __init__(self, make, model, year, stickerprice):
     self.make = make
     self.model = model
     self.year = year
     self.stickerprice = stickerprice
     self.discountprice = stickerprice * .9
     self.updatedprice = 0
    
  def longname(self):
    return "{} {} {}".format(self.year, self.make, self.model)


class Sport(Car):
  def __init__(self, make, model, year, stickerprice, sportwheels, sportengine, sportinterior):
     self.make = make
     self.model = model
     self.year = year
     self.stickerprice = stickerprice
     self.discountprice = stickerprice * .9
     self.sportwheels = sportwheels
     self.sportinterior = sportinterior
     self.sportengine = sportengine
     self.updatedprice = 0

  def pricewithoptions(self, sportwheels, sportengine, sportinterior, discountprice):
    if sportwheels == "y":
      updatedprice = discountprice + 1000.00
    else:
      updatedprice = discountprice
    if sportengine == "y":
      updatedprice = updatedprice + 3000.00
    else:
      updatedprice = updatedprice
    if sportinterior == "y":
      updatedprice = updatedprice + 2000.00
    else:
      updatedprice = updatedprice
    return updatedprice
    


car_1 = Sport('Dodge', 'Charger GT', 2020, 26000.00,'n', 'y', 'y',)
car_2 = Sport('Subaru', 'Impreza', 2013, 10000.00,'n', 'y', 'n',)
car_3 = Sport('Toyota', 'Supra', 1995, 30000.00,'y', 'y', 'y',)
print( "Car: ", car_1.longname())
print("Sticker price: $", car_1.stickerprice)
print("Discounted price: $", car_1.discountprice)

print("Price with added options: $", car_1.pricewithoptions(car_1.sportwheels, car_1.sportengine, 
                                                           car_1.sportinterior, car_1.discountprice))
print("")
print( "Car: ", car_2.longname())
print("Sticker price: $", car_2.stickerprice)
print("Discounted price: $", car_2.discountprice)

print("Price with added options: $", car_2.pricewithoptions(car_2.sportwheels, car_2.sportengine, 
                                                           car_2.sportinterior, car_2.discountprice))
print("")
print( "Car: ", car_3.longname())
print("Sticker price: $", car_3.stickerprice)
print("Discounted price: $", car_3.discountprice)
print("Price with added options: $", car_3.pricewithoptions(car_3.sportwheels, car_3.sportengine, 
                                                             car_3.sportinterior, car_3.discountprice))
print("")