d = open("p4d.txt", "r")

#initialize counters and sums to 0
c = 0.0
tot_ep = 0.0

#get first data line
item = str(d.readline().rstrip('\n'))

while item !="":
  qty = float(d.readline())
  price = float(d.readline())
  
  ep = qty * price
  #sum and count - in the loop
  tot_ep = tot_ep + ep
  c = c + 1
  
  #diplay a line of data
  print("Item is:           ", item)
  print("Quantity is:       ", qty)
  print("Price is:          ", price)
  print("Extended price is: ", ep)
  
  #get next data
  item = str(d.readline().rstrip('\n'))

#after the loop
#final calc
#display item and sums and counts
print("Total extended prices: ", tot_ep)
print("Number of orders:      ", c)
avg = tot_ep/c
print("Average order:         ", avg)
  
