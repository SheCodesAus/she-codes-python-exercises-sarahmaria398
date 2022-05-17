
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
from datetime import datetime
# d = datetime.strptime("2021-07-05T07:00:00+08:00", "%Y-%m-%dT%H:%M+%H:%M")
# print(d)

# datetime.strptime(
#     "2008-09-03T20:56:35.450686Z", "%Y-%m-%dT%H:%M:%S.%fZ")

# d = datetime.strftime("2008-09-03T20:56:35.450686Z", "%Y-%m-%d")
# print(d)

d = datetime.strptime('2019-01-04T16:41:24+0200', "%Y-%m-%dT%H:%M:%S%z")
print(d)
