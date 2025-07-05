#task1
# for i in range(1, 11):
#     print(i)

#task2
# for i in range(2, 21, 2):
#     print(i)

#task3
# for i in range(1, 21, 2):
#     print(i)

#task4
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial:", factorial)

#task5
# total = 0
# for i in range(1, 101):
#     total += i
# print("Sum:", total)

#task6
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# average = total / len(numbers)
# print("Average:", average)

# #task7
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

#task8
# for i in range(1, 6):
#     print(i)

#task9
# for i in range(1, 11):
#     print(i)

#task10
# numbers = [10, 20, 30, 40, 10]

# if numbers[0] == numbers[-1]:
#     print(True)
# else:
#     print(False)

#task11
# numbers = [10, 15, 23, 45, 60, 78, 90]
# for num in numbers:
#     if num % 5 == 0:
#         print(num)

#task12
# char = input("Enter a character: ").lower()
# if char in 'aeiou':
#     print("Vowel")
# else:
#     print("Consonant")

#task13
# even_count = 0
# odd_count = 0
# for i in range(10, 56):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even count:", even_count)
# print("Odd count:", odd_count)

#task14
# for i in range(1, 26):
#     if i % 5 != 0:
#         print(i)
#task15
# numbers = [3, 4, 5]
# for num in numbers:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"Factorial of {num}: {factorial}")

#task16        
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# product = a * b
# if product > 500:
#     print("Sum:", a + b)
# else:
#     print("Product:", product)

#task17
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# if a > b:
#     print(f"{a} is greater.")
# elif b > a:
#     print(f"{b} is greater.")
# else:
#     print("Both numbers are equal.")

#task18
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# if a >= b and a >= c:
#     print(f"{a} is the greatest.")
# elif b >= a and b >= c:
#     print(f"{b} is the greatest.")
# else:
#     print(f"{c} is the greatest.")

#task19
x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
positives = []
negatives = []
for num in x:
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)
print("Positive numbers:", positives)
print("Negative numbers:", negatives)
    
