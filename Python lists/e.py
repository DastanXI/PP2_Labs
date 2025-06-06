#Remove list items

#1 remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#2 pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
#if index is not specified in the function then removes the last element
print(thislist)

#3 delete
thislist = ["apple", "banana", "cherry"]
del thislist[0] 
#without [] deletes the entire list
print(thislist)

#4 clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
#clears the list but does not delete it
print(thislist)