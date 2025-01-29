import math

def calculate_sin(x, terms=10):
    sin_x = 0
    for n in range(terms):
        sign = (-1) ** n
        sin_x += sign * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return sin_x

degrees = float(input("Enter angle in degrees: "))
radians = degrees * (math.pi / 180)
print(f"Sin({degrees}) ≈ {calculate_sin(radians)}")
