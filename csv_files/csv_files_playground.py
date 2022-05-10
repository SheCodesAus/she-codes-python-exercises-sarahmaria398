import csv
import os


# with open ("dogs.txt") as file:
#     file_reader = csv.reader(file, delimiter=" ") #how you want to separate things
#     for row in file_reader:
#         # print(row)
#         print(row[0]) #without being in a list

# cats = ["Cats are great.", "Nope"]

# # would default as read. mode to be set with write, if file does not exist.
# with open("cats.txt", mode="w") as file:
#     file_writer = csv.writer(file, delimiter="\n")
#     # delimiter again, this time adding newline. defining what to do with each element.
#     file_writer.writerow(cats)


# READING FROM CSV FILE
# population = []

# with open("csv_files/2016_pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         population.append(line)

# print(population)
# print()

# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")


# WRITING A CSV FILE


# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     for age_group in population:
#         csv_writer.writerow([age_group[1]], age_group[0])


# Q1)Write a program that reads in colours_20_simple.csvand output the colour data

# with open("csv_files/colours_20.csv") as csv_file:
#     file_reader = csv.reader(csv_file)

#     next(file_reader)

#     for line in file_reader:
#         print(f"{line[1]} {line[2]} {line[4]}")


# Q2)Write a program that reads in colours_20_simple.csv and outputs the colour data in order English,Hex then RGB.

# with open("csv_files/colours_20.csv") as csv_file:
#     file_reader = csv.reader(csv_file, delimiter=",")

#     next(file_reader)

#     for line in file_reader:
#         print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")


# Q4)Using the sam ecolour csvfiles, write a program that outputs the number of times each of the following colours appear in the English Name


# Red = 0
# Green = 0
# Blue = 0
# Yellow = 0

# with open("csv_files/colours_20.csv") as csv_file:
#     file_reader = csv.reader(csv_file, delimiter=",")

#     next(file_reader)

# # yellow = file_reader.count("yellow")

# for line in file_reader:

#     print(line)
# print(yellow)

#         word = csv.reader(line, delimiter=' ')
# if
# print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")
# print(line)
# print(word)

# fail

# 5)galaxies.py contains dataabout82differentgalaxiesandtheirvelocities(km/sec).Usingthisdata,outputthe galaxy with the slowest velocity, and the galaxy with the highest velocity.

# with open("csv_files/galaxies.csv") as csv_file:
#     file_reader = csv.reader(csv_file)

#     next(file_reader)

#     for line in file_reader:
#         line.sort()
#     # print(f"{line[0]} {line[1]}")

#     print(line)

# ----------------

# with open("csv_files/colours_20.csv") as csv_file:
#     file_reader = csv.reader(csv_file)

#     next(file_reader)

#     with open("colours101.csv", "w") as new_file:
#         csv_writer = csv.writer(new_file, delimiter=' ')

#         for line in file_reader:
#             csv_writer.writerow(line)
