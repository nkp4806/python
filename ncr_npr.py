import math

def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def npr(n, r):
    return math.factorial(n) // math.factorial(n - r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print(f"nCr: {ncr(n, r)}")
print(f"nPr: {npr(n, r)}")
