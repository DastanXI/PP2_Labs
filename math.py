#1 degree to radian
import math

deg = float(input("Input degree: "))
rad = deg * (math.pi / 180)
print("Output radian:", round(rad, 6))

#2 area of trapezoid
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
area_trapezoid = 0.5 * (a + b) * h
print("Expected Output:", area_trapezoid)

#3 area of regular polygon
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area_polygon = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area_polygon, 2))

#4 area of parallelogram
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area_para = base * height
print("Expected Output:", area_para)
