subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))

if subject1 <= 39 or subject2 <= 39 or subject3 <= 39:
    print("Fail")
else:
    print("Pass")

total = subject1 + subject2 + subject3
average = total / 3
print("Total:", total)
print("Average:", average)

def assign_grade(marks):
    if marks == -1:
        return "NA"
    elif marks <= 39:
        return "F"
    elif marks <= 44:
        return "P"
    elif marks <= 49:
        return "C"
    elif marks <= 54:
        return "B"
    elif marks <= 59:
        return "B+"
    elif marks <= 69:
        return "A"
    elif marks <= 79:
        return "A+"
    else:
        return "O"

print("Subject 1 Grade:", assign_grade(subject1))
print("Subject 2 Grade:", assign_grade(subject2))
print("Subject 3 Grade:", assign_grade(subject3))
