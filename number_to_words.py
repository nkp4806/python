num_to_word = ["zero", "one", "two", "three", "four", "five", "six", 
               "seven", "eight", "nine", "ten", "eleven", "twelve", 
               "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
               "eighteen", "nineteen"]

num = int(input("Enter a number between 0 and 19: "))

if 0 <= num <= 19:
    print(num, "in words is", num_to_word[num])
else:
    print("Number out of range")
