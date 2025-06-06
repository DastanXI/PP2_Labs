#change the list items

thislist = ["apple","banana","grapes"]
thislist[1] = "blackcurrant"
thislist.insert(2, "watermelon")
print(thislist)

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)

list2 = ["apple", "banana", "cherry"]
list2[1:3] = ["watermelon"]
print(list2)