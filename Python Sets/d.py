#remove from set

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
thisset.discard("banana")

print(thisset)
x = thisset.pop()

print(x)

print(thisset)

thisset.clear()

print(thisset)


thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

