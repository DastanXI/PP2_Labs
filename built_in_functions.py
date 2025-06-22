#1 Multiply all the numbers in a list using builtin function
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Example usage:
nums = [2, 3, 4]
print("#1 Product of all numbers:", multiply_list(nums))


#2 Count uppercase and lowercase letters in a string using builtin functions
def count_case(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return upper_count, lower_count

# Example usage:
string = "Hello World!"
upper, lower = count_case(string)
print("#2 Uppercase letters:", upper)
print("Lowercase letters:", lower)


#3 Check if a string is a palindrome using builtin functions
def is_palindrome(s):
    return s == s[::-1]

# Example usage:
word = "madam"
print(f"#3 Is '{word}' a palindrome? {is_palindrome(word)}")


#4 Invoke square root function after specific milliseconds
import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"#4 Square root of {number} after {delay_ms} milliseconds is {result}")

# Example usage:
num = 25100
delay = 2123
delayed_sqrt(num, delay)


#5 Check if all elements in a tuple are true using builtin function
def all_true(elements):
    return all(elements)

# Example usage:
t = (True, 1, "Hello", 3.5)
print("#5 All elements are true:", all_true(t))
