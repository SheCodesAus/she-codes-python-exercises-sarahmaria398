import csv
from datetime import datetime
from email import header
from operator import indexOf


# Functions
# Exercise 1: Write a function that takes a temperature in fahrenheitand returns the temperature in celsius.

# def temp_in_f(num):
#     total = (num * 1.8) + 32
#     return total


# print(temp_in_f(5))

# Exercise 2:
# Writeafunctionthatacceptsoneparameter(aninteger)andreturnsTruewhenthatparameterisoddandFalse when that parameter is even.

# num = int(input("enter a number "))

# if num % 2 == 0:
#     print("False")

# else:
#     print("True")


# def odd_even(num):
#     if num/2 ==

#Exercise: 3
# Write a function that returns the mean of a listof numbers

# numbers = [10, 5, 6]


# def mean(list):
#     total = 0
#     for i in list:
#         total += i
#     return total/(len(list))


# print(mean(numbers))

# Exercise : 4
# Writeafunctionthattakestwoparameters;theunitpriceofanitem,andhowmanyunitswerepurchased.Return the total cost as a string

# def total(price_per_unit, num_units):
#     result = price_per_unit * num_units
#     return result


# print(f"${total(4.25, 3)}")


# from datetime import datetime


# def convert_date(iso_string):
#     dt = datetime.datetime('%Y %m %d')
#     return dt

#     # d = datetime.fromisoformat(iso_string[:-1]).astimezone(timezone.utc)
#     # d.strftime('%Y-%m-%d %H:%M:%S')
#     # # date = datetime.strptime(iso_string, '%Y-%m-%dT%X+%X')
#     # return(date.strftime('%Y %m %d'))


# print(convert_date("2021-07-05T07:00:00+08:00"))


# numbers = [1, 2, -5, 3]

# min_value = numbers[0]
# min_location = 0
# index = 0

# for num in numbers:

#     if num < min_value:
#         min_value = num
#         min_location = index
#     index += 1

# print(min_value, min_location)


# def bonus_time(salary, bonus):
#     return "${}".format(salary * (10 if bonus else 1))
# # not mine


# print(int(3))
# print(int('3'))

# arr = ['5', '0', 9, 3, 2, 1, '9', 6, 7]


# def sum_mix(arr):
#     # list = []
#     num = arr[0]
#     int(num)
#     return print(type(num))
# result = 0
# for i in arr:
#     if type(i) != int:
#         int(i)
#     print(type(i))

# result += i
# list.append(i)
# print(i)
# list.append(i)
#     return result


# sum_mix(arr)


bob = [5, 10, 36, 9, 10]


def sum_two_smallest_numbers(numbers):
    list = []
    lowest_num = 0

    for i in numbers:
        if i < lowest_num:
            lowest_num = i
            list.append(i)
            numbers.remove(i)
        else:
            list.append(lowest_num)

    return list


print(sum_two_smallest_numbers(bob))
