import csv
import os
# groceries = {"Baby Spinach": 2.78, "Hot Chocolate": 3.70,
#              "Crackers": 2.10, "Bacon": 9.00, "Carrots": 0.56, "Oranges": 3.08}

# quantity = {"Baby Spinach": 1, "Hot Chocolate": 3,
#             "Crackers": 2, "Bacon": 1, "Carrots": 4, "Oranges": 2}

# result = ""
# for item, cost in groceries.items():
#     for item2, item_qty in quantity.items():
#         if item == item2:
#             total = "{:.2f}".format(cost * item_qty)

#             result += f"{item_qty} "
#             result += f"{item} @ "
#             result += f"${cost} = "
#             result += f"${total}\n"

# print(result)

# Q2
# colours = ["purple", "red", "yellow", "blue", "purple",
#            "orange", "blue", "purple", "orange", "green"]

# colours = ["orange", "purple", "blue", "yellow", "green", "green", "purple", "purple", "green",
#            "blue", "green", "orange", "purple", "blue", "green", "orange", "orange", "red", "yellow", "yellow"]

# colour_counts = {"blue": 0, "green": 0,
#                  "yellow": 0, "red": 0, "purple": 0, "orange": 0}

# for i in colours:
#     for colour, value in colour_counts.items():
#         if colour == i:
#             colour_counts[colour] += 1
# print(colour_counts)

# Q3
# names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy", "Joy", "Katie", "Maddie", "Tash", "Nic", "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
#          "Viv", "Anna", "Catherine", "Catherine", "Debby", "Gab", "Megan", "Michelle", "Nic", "Roxy", "Samara", "Sasha", "Sophie", "Teagen", "Viv"]

# name_counts = {"Maddy": 0, "Bel": 0, "Elnaz": 0, "Gia": 0, "Izzy": 0, "Joy": 0, "Katie": 0, "Maddie": 0, "Tash": 0, "Nic": 0, "Rachael": 0, "Bec": 0,
#                "Tabitha": 0, "Teagen": 0, "Viv": 0, "Anna": 0, "Catherine": 0, "Debby": 0, "Gab": 0, "Megan": 0, "Michelle": 0, "Roxy": 0, "Samara": 0, "Sasha": 0, "Sophie": 0}

# for i in names:
#     for name, value in name_counts.items():
#         if name == i:
#             name_counts[name] += 1

# print(name_counts)

# Q4
# with open("csv_files\colours_20_simple.csv") as csv_file:
#     file_reader = csv.reader(csv_file)
#     next(file_reader)
#     colour_data = {}
#     for line in file_reader:
#         colour_data[line[1]] = line[2]

# print(colour_data)

# Q5
with open("csv_files\colours_20_simple.csv") as csv_file:
    file_reader = csv.reader(csv_file)
    next(file_reader)
    list = []
    colour_data = {}

    for line in file_reader:
        list.append(line[0:3:2])
        colour_data[line[1]] = line[2]

    for i in list:
        for key, value in colour_data.items():
            colour_data[key] = i
            # I'm close but not quite: its all traffic yellow

print(colour_data)
