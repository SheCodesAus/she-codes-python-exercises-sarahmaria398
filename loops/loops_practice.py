# Exercise : 1
# num = int(input("Enter a number"))
# for i in range(num+1):
#     print(f"{num} * {i} = {num*i}")


# my attempt
# num = int(input("Enter a number"))
# if int(num) == 0:
#     print(num)

# else:
#     for i in range(num+1):
#         result = int(num) * i
#         print(f"{num} * {i} = {result}")


# Exercise: 2
# total = 0
# num = int(input("Enter a number "))
# for i in range(num+1):
#     total += i
#     print(total)


# need to rejig to only print the remaining output, not all the middle digits too

# for loop each number counting up to that number
# and add easch one to the previous
# print the result

# Exercise: 3

# total = 0
# random_numbers = [3, 5, 9, 1]

# for num in random_numbers:
#     total += num
#     print(total)
# need to rejig to only print the remaining output, not all the middle digits too

# Exercise : 4

# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]

# for item in mailing_list:
#     print(f"{item[0]} : {item[1]}")

# success!


# WHILE LOOPS

# Exercise: 1

# total = 0
# num = input("Enter a number ")

# while num != "":
#     int_num = int(num)
#     print(num)
#     total = total + int_num
#     num = input("Enter a number ")

# else:
#     print(total)


# commenting out my attempts: such as this one below
# total = 0
# num = int(input("Enter a number "))

# while num != "":
#     print(num)
#     total = total + num

# else:
#     print(total)
# total = total + num

# print(total)

# commenting out my attempts: such as this one below
# if num == "":
#     print(total)

# else:
#     print(num)
#     total = total + num
#     break


# Exercise: 2

# num = int(input("Enter a number "))

# list = []
# for i in range(num+2):
#     list.append(i)
# print(list[1: -1: 2])

# I used a for loop not while loop here.
# enter a number
# assign all numbers from 0 to this number, inclusive, in to a list
# print from the list every odd number

# Exercise : 3
# selected_number = 9
# guess = int(input("Guess a number "))

# while guess != selected_number:

#     if guess > selected_number:
#         # If you don't put another next step here, the code will continue forever...
#         print("Too high!")
#         guess = int(input("Guess a number "))

#     elif guess < selected_number:
#         print("Too low!")
#         guess = int(input("Guess a number "))

# while guess == selected_number:
#     print("Correct!")
#     break


# Loops: Extension

# Exercise: 1
# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# number_units = []
# input = int(input("Enter the number of units you have bought of each item "))
# number_units.extend(input)
# print(number_units)

# for unit in number_units:
#     for cost in groceries[1]:
#         print(unit * cost)

# number_units = []
# spinach = float(input("How many? "))
# number_units.append(spinach)

# chocolate = float(input("How many? "))
# number_units.append(chocolate)
# number_units.append(input("How many? "))
# number_units.append(input("How many? "))
# number_units.append(input("How many? "))
# number_units.append(input("How many? "))
# number_units.append(input("How many? "))

# for unit in number_units:
#     for type in groceries:
#         for cost in range(type[1]):
#             total = unit*cost
# print(total)

# Failed

# Exercise: 2

# string = input("enter a word ")

# for letter in string:
#     print(f"{string.index(letter)} {(letter)}")

# boom chaka laka!

# Exercise: 3
# num = int(input("Enter a number"))

# for i in range(num+1):
#     print(f"*" * i)

# Exercise : 4
# num = int(input("Enter a number"))

# for i in range(num+1):
# print(f"" * num+1 + "*" * i)


# for i in range(num+1):
#     space = "" * (num+1) - 2
#     print(sapce)

# failed
