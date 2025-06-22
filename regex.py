# === regex_tasks.py ===
import re

# Task 1: 'a' followed by zero or more 'b's
def task1(text):
    return re.fullmatch(r'ab*', text)

# Task 2: 'a' followed by two to three 'b's
def task2(text):
    return re.fullmatch(r'ab{2,3}', text)

# Task 3: lowercase joined with underscore
def task3(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)

# Task 4: One uppercase followed by lowercase letters
def task4(text):
    return re.findall(r'[A-Z][a-z]+', text)

# Task 5: 'a' followed by anything, ending in 'b'
def task5(text):
    return re.fullmatch(r'a.*b', text)

# Task 6: Replace space, comma, or dot with colon
def task6(text):
    return re.sub(r'[ ,.]', ':', text)

# Task 7: Snake case to camel case
def task7(text):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)

# Task 8: Split at uppercase letters
def task8(text):
    return re.findall(r'[A-Z]?[a-z]+', text)

# Task 9: Insert spaces before capital letters
def task9(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# Task 10: CamelCase to snake_case
def task10(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

# Test section
if __name__ == "__main__":
    print("Task 1:", task1("abbb"))
    print("Task 2:", task2("abb"))
    print("Task 3:", task3("hello_world text_here"))
    print("Task 4:", task4("Hello World test"))
    print("Task 5:", task5("axyzb"))
    print("Task 6:", task6("Hello, world. Test"))
    print("Task 7:", task7("hello_world_test"))
    print("Task 8:", task8("SplitAtUpperCase"))
    print("Task 9:", task9("InsertSpacesHere"))
    print("Task 10:", task10("CamelCaseExample"))
