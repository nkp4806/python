import math

x_center, y_center = map(int, input("Enter center of circle (x y): ").split())
radius = int(input("Enter radius of the circle: "))
x, y = map(int, input("Enter point (x y): ").split())

distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)

if distance < radius:
    print("The point is inside the circle")
elif distance == radius:
    print("The point is on the circle")
else:
    print("The point is outside the circle")
