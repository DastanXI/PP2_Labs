#copy a dictionary 

#copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict1 = dict(thisdict)
print(mydict1)