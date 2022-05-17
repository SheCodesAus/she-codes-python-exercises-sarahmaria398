# Exercise : 1 Ask the user for a number. Use a for loop to print the times tables for that number.

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


# Exercise: 2 Ask the user for a number. Use a for loop to sum from 0 to that numbe
# total = 0
# num = int(input("Enter a number "))
# for i in range(num+1):
#     total += i

# print(total)


# need to rejig to only print the remaining output, not all the middle digits too

# for loop each number counting up to that number
# and add easch one to the previous
# print the result

# Exercise: 3 Given a list, use a for loop to sum all the numbers in the list.


# here
# total = 0
# random_numbers = [3, 5, 9, 1]

# for num in random_numbers:
#     total += num
#     print(total)
# need to rejig to only print the remaining output, not all the middle digits too

# Exercise : 4  Use a for loop to format and print the following list:

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

# Exercise: 1 Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the
# numbers

# total = 0
# num = input("Enter a number ")

# while num != "":
#     int_num = int(num)
#     print(num)
#     total += int_num
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


# Exercise: 2 Ask the user to enter a number. Print all the odd numbers between 0 and that number (inclusive).

# originally started with a for loop
# num = int(input("Enter a number "))

# list = []
# for i in range(num+2):
#     list.append(i)
# print(list[1: -1: 2])

# and then i implemented it in to the while loop

# num = int(input("Enter a number "))

# while num % 2 == 0:
#     list = []
#     for i in range(num+2):
#         list.append(i)
#     print(list[1: -1: 2])
#     break

# else:
#     list = []
#     for i in range(num+2):
#         list.append(i)
#     print(list[1: -1: 2])


# Exercise : 3 Select a number. Ask the user to enter a number, output whether their number is less than or greater than
# the selected number. Repeat this process until the user guesses the correct numbe
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

# Exercise: 1 Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is provided in the same order as defined in the list above.

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# cost = []

# for item in range(len(groceries)):
#     units = input("Enter the number of units you have bought of each item ")
#     sub_total = groceries[item][1] * float(units)
#     cost.append(sub_total)
#     print(cost)

# total = sum(cost)

# print("====Izzy's Food Emporium====")

# for i in range(len(groceries)):
#     print(f"{groceries[i][0]}      ${cost[i]}")


# print("============================")
# print(f"${total}")


# Print groceries list with replaced item[1] from new list


# print(float(item[1]))
# print(float(units))
# cost = cost.append(float(units) * float(item[1]))
# print(cost)


# for item in groceries

# number_units = []

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

# Exercise: 2 Ask the user to enter a string. Output the string one character at a time, as well as it’s position in the string.

# string = input("enter a word ")

# for letter in string:
#     print(f"{string.index(letter)} {(letter)}")

# boom chaka laka!

# Exercise: 3 Ask the user for a number and use this to generate a pyramid of that height.
# num = int(input("Enter a number"))

# for i in range(num+1):
#     print(f"*" * i)

# Exercise : 4  Ask the user for a number and use this to generate a (different) pyramid of that height.
# num = int(input("Enter a number"))

# for i in range(num+1):
#     space = " " * i
#     star = "*" * i
#     print(f"{space} {star}")


# for i in range(num+1):
#     space = "" * (num+1) - 2
#     print(sapce)

# failed
