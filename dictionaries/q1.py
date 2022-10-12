# Program 1

# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
# }

# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
# }
# result = ""

# for item, price in groceries.items():
#     for item2, amount in quantity.items():
#         if item == item2:
#             total = "{:.2f}".format(price * amount)

#             result += f"{amount} "
#             result += f"{item} @ "
#             result += f"${price} = "
#             result += f"${total}\n"


# print(result)


# for item, price in groceries.items():
#     for item2, amount in quantity.items():
#         print(price, amount)
#         groceries[item] = price * amount

# print(groceries)

# quantity_list = list(quantity.values())
# print(quantity_list)

# groceries_list = list(groceries.values())
# print(groceries_list)

# total = []
# for i in range(0, len(quantity_list)):
#     total.append(quantity_list[i] * groceries_list[i])

# print(total)

# for i in total:
#     for item in groceries:
#         groceries[item] = i

# print(groceries)

# res = []
# for sub, val in zip(groceries, total):
#     res.append(sub)
# print(res)

# Program 2

colours = ["purple", "red", "yellow", "blue", "purple",
           "orange", "blue", "purple", "orange", "green"]

colour_counts = {"blue": 0, "green": 0, "yellow": 0,
                 "red": 0, "purple": 0, "orange": 0, }

purple = 0

# for key, val in colour_counts.items():
#     if key in colours:
#         colour_counts[key] = val + 1

for colour in colours:
    if colour_counts[colour] in colours:
        colour_counts[colour] = val + 1

print(colour_counts)

# if "purple" in colours:
#     purple += 1
#     colour_counts["purple"] = + purple

# print(colour_counts)
