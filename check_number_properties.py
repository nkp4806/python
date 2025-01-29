def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_automorphic(num):
    return str(num ** 2).endswith(str(num))

num = int(input("Enter a number: "))
print("Prime:", is_prime(num))
print("Perfect:", is_perfect(num))
print("Armstrong:", is_armstrong(num))
print("Palindrome:", is_palindrome(num))
print("Automorphic:", is_automorphic(num))
