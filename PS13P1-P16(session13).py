def dl1 (list1):
  n = int(input("How many items in your list? "))
  for n in range(0,n,1):
    s = int(input("Enter an integer: "))
    list1.append(s)
  return list1
def displaylist(list1):
  for item in list1:
      print(item)

#main
list1 = []   # defining an empty list
list1 =  dl1(list1)  
#displaylist(list1) # display each item in the list
print(" ")
print("Original list: ")
print(list1)
print(" ")

#Problem 2 (Insert 99 at position 1)
list1.insert(0,99)
print("New list once 99 is inserted at position 1: ")
print(list1)
print(" ")

#Problem 3 (Replace 99 with 100)
list1[0] = 100
print("New list once 99 is replaced with 100: ")
print(list1)
print(" ")

#Problem 4 (Second list is appended to the first list)
#(Problem 4 part 1)
list2 = ["500", "600", "700", "800", "900"]
print("Second list: ")
print(list2)
print(" ")
#(Problem 4 part 2 - first list is extended with second list and first list is displayed)
list1.extend(list2)
print("List one extended with list two: ")
print(list1)
print(" ")

#Problem 5 (Remove '800' from the list and display)
list1.remove("800")
print("List 1 with '800' removed: ")
print(list1)
print(" ")

#Problem 6 (Remove 3rd item from list and display)
list1.remove(2)
print("List 1 with 3rd item removed: ")
print(list1)
print(" ")

#Problem 7 (Create a list of grades)
list3 = ["A", "B", "C", "A", "A", "C"]

#Problem 8 (Display a count of the number of A grades)
print("Number of A grades in the list: ", list3.count("A"))
print(" ")

#Problem 9 (Display the index (position) of the first B grade)
print("Index of the first B grade: ", list3.index("B"))
print(" ")

#Problem 10 (Search for grade "F" in grades list)
def seqsearch(list3, grade):
  l = len(list3)
  sindex = -1
  for i in range(0, l, 1):
    if list3[i] == grade:
      sindex = i

  return sindex

r = input("Do you want to search for a grade? (Yes/No) ")
while r == "Yes":
  grade = input("Enter the grade to search for: ")
  i = seqsearch(list3, grade)
  if i == -1:
    print(grade, "was not found")
  else:
    print(grade, "was found in the list.")
  r = input("Do you want to search for another grade? (Yes/No) ")

#Problem 11 (Clear second list & display list)
list2.clear()
print(" ")
print("List two after being cleared: ")
print(list2)
print(" ")

#Problem 12 (Delete second list and display list)
#del will delete the list and display an error when trying to display 
#***(THIS IS HIDDEN TO RUN REST OF CODE PROPERLY)***
#del list2
#print("List two after being deleted: ")
#print(list2)
#print(" ")

#Problem 13 (Create a list of players)
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

#Problem 14 (Sort the list of players)
players.sort()
print("List of players sorted: ")
print(players)
print(" ")

#Problem 15 (Make a copy of the list of players)
players2 = players.copy()
print("Copy of list of players: ")
print(players2)
print(" ")

#Problem 16 (Reverse the list of players, display players, then display players2)
players.reverse()
print("Original list of players: ")
print(players)
print(" ")
print("reversed, sorted, copy of list of players: ")
print(players2)
