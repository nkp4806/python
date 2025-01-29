def count_alphabets_and_digits(string):
    alphabets = digits = 0
    for char in string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
    return alphabets, digits

string = input("Enter a string: ")
alphabets, digits = count_alphabets_and_digits(string)
print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
