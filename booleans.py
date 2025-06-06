#1(true or ralse return)

print(10 > 9)
print(10 == 9)
print(10 < 9)

#2(based on condition)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
#3 the boolean function bool()

print(bool("Hello")) #true
print(bool(15)) #true

#3.1 in variable boolean 

print(bool("Hello"))
print(bool(15))

#strings and numbers are true except for empty strings and 0

#3.2

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#4(they return false)

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#5 function that returns false

class myclass():
      def __len__(self):
       return 0

myobj = myclass()
print(bool(myobj))

#6(prints YES if the value is true)

def myFunction() :
      return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#7(checks using the built in function isinstance)

x = 200
print(isinstance(x, int))
