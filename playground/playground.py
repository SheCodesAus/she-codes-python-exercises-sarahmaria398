# Inpogress : leetcode
# Palindrome

# something like  if less than 0
# abs() returns absolute value

# x = -121


# def isPalindrome(y):
#     string = str(y)
#     if "-" in string:
#         string = string.replace("-", "")

#     result = str(string)[::-1]
#     msg = "true" if int(result) == y else "false"
#     return msg


# print(isPalindrome(x))

# Twice as Old

# dad = 55
# son = 30


# def twice_as_old(dad_years_old, son_years_old):
#     son = son_years_old * 2
#     result = dad_years_old - son
#     if result < 0:
#         result = str(result)
#         result = result.replace("-", "")
#         result = int(result)

#     return(result)


# print(twice_as_old(dad, son))

# def twice_as_old(dad_years_old, son_years_old):
#     return abs(dad_years_old - 2*son_years_old)

# not my own solution, abs() returns absolute value
