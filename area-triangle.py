# Find the area of a triangle
a = float(input("Enter first side:"))
b = float(input("Enter second side:"))
c = float(input("Enter third side:"))
d = (a + b + c) / 2
area = (d*(d-a)*(d-b)*(d-c)) ** 0.5
print("The Area of the triangle is : ", area)

input("Press any key to continue")