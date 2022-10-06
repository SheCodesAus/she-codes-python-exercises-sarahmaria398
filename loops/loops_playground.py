# for num in range(0, 5, 2):
#     print(num)

# list = [["sarah"], ["jeff"], ["joan"], ["star", "stellar"]]

# for item in range(len(list)):
#     print(list[item])

# for item in list:
#     print(item)

# for a in list:
#     for b in a:
#         print(b)


# For loops
# Program 1
# num = input("enter a number ")
# num = int(num)

# for i in range(1, num+1):
#     j = i * (num)
#     print(f"{num} * {i} = {j}")

# Program 2
# num = input("enter a num to sum to ")
# num = int(num)
# total = 0

# for i in range(0, num+1):
#     total = total + i

# print(total)

# Program 3
# random_numbers = [-3, -5, 9, 1]

# total = 0
# for i in random_numbers:
#     total = total + i

# print(total)

# Program 4
# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]

# for i in mailing_list:
#     print(f"{i[0]} : {i[1]}")

# while loops

# Program 1
# num = input("enter a num ")

# while num != "":
#     num = input("enter another num ")

# --------------

# nums = [1, 2, 1]


# class Solution(object):
#     def getConcatenation(self, nums):
#         new_list = []

#         for i in nums:
#             new_list.append(i)

#         new_list.reverse()
#         total = nums + new_list
#         print(total)

#     getConcatenation(nums)

# -----------
# Program 2
# num = input("enter num ")
# num = int(num)
# total = -1


# while total < num:
#     total += 2
#     print(total)


# Program 3
# num = input("ENTER A NUM")
# num = int(num)
# guess = 50

# while num < guess:
#     print("Too low!")
#     num = input("ENTER A NUM")
#     num = int(num)

# while num > guess:
#     print("Too high!")
#     num = input("ENTER A NUM")
#     num = int(num)


# while num == guess:
#     print("Correct!")
#     break

# Program 1
# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# list = []
# amounts = []
# complete = []
# index = 0

# for i in groceries:
#     list.append(float(input("How many of " + i[0] + " did you buy? ")))

# for i in groceries:
#     amounts.append(i[1])

# for i in list:
#     complete.append(list[index] * amounts[index])
#     index += 1

# total = sum(complete)

# jeff = 0

# print("====Izzy's Food Emporium====")

# for i in groceries:
#     my_float = complete[jeff]
#     format_float = "{:.2f}".format(my_float)
#     print(i[0], format_float)
#     jeff += 1

# print("============================")
# print("{:.2f}".format(total))

# Program 2
# word = "cats"
# index = 0
# for i in word:
#     print(index, i)
#     index += 1

# Program 3
# num = input("enter a number ")
# num = int(num)
# for i in range(0, num+1):
#     print("*" * i)

# Program 4
# num = input("enter a number ")
# num = int(num)
# for i in range(0, num+1):
