fruits = ["apple", "banana", "cherry"]
for x in "banana":
    print(x)

for x in fruits:
  print(x)
  
  #2
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  #3
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#4
for x in range(2, 30, 3):
  print(x)
  
  #5
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)