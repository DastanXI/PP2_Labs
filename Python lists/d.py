#add list items

#append()

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist.insert(1,"grapes")
print(thislist)

#extend() adds one list to another

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#you can add tuple to a list
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)