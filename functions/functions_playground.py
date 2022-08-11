
# def hello():
#     print("hello world")
#     return 5

# # return is where the function ends


# result = hello()
# print(result)

# def add(number1, number2):
#     result = number1 + number2
#     return result


# print(add(1, 3))

# def multiply(num):
#     return num * 3


# # or save it in a variable, then print it
# print(multiply(3))

# def calculate_mean(x, y):
#     total = (x + y)/2
#     return total


# print(calculate_mean(5, 8))

list = [1, 12]


# def plusOne(digits):
#     num = digits[-1]
#     num += 1
#     digits.pop()
#     digits.append(num)

#     if digits[-1] >= 10:
#         str(digits[-1])

#     return digits


def plusOne(digits):
    list = []
    for i in digits:
        list.append(str(i))

    for i in list:
        list = list.join()
    # for i in list:
    #     for j in i:
    #         if j.length >= 2:
    #             j.split()
    #         list.append(j)
    # list.append(str(i))
    # list.join()

    return list


print(plusOne(list))
