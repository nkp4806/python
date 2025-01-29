x1, y1 = map(int, input("Enter point 1 (x1 y1): ").split())
x2, y2 = map(int, input("Enter point 2 (x2 y2): ").split())
x3, y3 = map(int, input("Enter point 3 (x3 y3): ").split())

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points are collinear")
else:
    print("The points are not collinear")
