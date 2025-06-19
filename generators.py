#1 squares up to n
def square_generator(n):
    for i in range(n + 1):
        yield i * i

#2 even numbers from 0 to n (input from user)
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
evens = even_generator(n)
print(",".join(str(num) for num in evens))

#3 numbers divisible by 3 and 4 from 0 to n
def div_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

#4 squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

#5 countdown from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
