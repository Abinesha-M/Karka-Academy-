#task1
# num = float(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

#task2
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# #task3
# base = float(input("Enter the base number: "))
# exponent = float(input("Enter the exponent: "))
# result = base ** exponent
# print(f"{base} raised to the power of {exponent} is {result}")

#task4
# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:
#     print(f"{b} is greater than {a}")
# else:
#     print("Both numbers are equal.")

#task5
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#task6
# score = int(input("Enter the student's score: "))
# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score <= 89:
#     grade = 'B'
# elif 70 <= score <= 79:
#     grade = 'C'
# elif 60 <= score <= 69:
#     grade = 'D'
# else:
#     grade = 'F'
# print(f"Grade: {grade}")

#task7
# age = int(input("Enter your age: "))
# if age < 16:
#     print("You can't drive.")
# elif age < 18:
#     print("You can drive but not vote.")
# elif age < 25:
#     print("You can vote but not rent a car.")
# else:
#     print("You can do pretty much anything.")

# #task8
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

#task9
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

