#input phase
shareprice = float(input("Enter the purchase price per share: "))
stockprice = float(input("Enter the current stock price: "))
stockquantity = float(input("Enter the quantity of stock: "))

#process phase
stockvalue = (stockprice-shareprice)*stockquantity

#output phase
print("Stock value has changed by: ",stockvalue)