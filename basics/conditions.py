# age = 20

# Basic if condition

# if(age >= 18):
#     print("You are an adult.")

# if-else condition

# marks = 75

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 40:
#     print("Grade: D")
# else:
#     print("Grade: F")

# Conditional statements with input
 
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else: 
#     print("You are a minor.")

# Nested if-else condition

age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ").lower()

if age >= 18:
    if has_license == "yes":
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")
else:
    print("You are not old enough to drive.")