import csv

# with open("csv_files/2016_pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)

# population = []

# with open("csv_files/2016_pilbara.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         population.append(line)

# # print(population)

# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")

# with open("csv_files/population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')

#     for age_group in population:
#         csv_writer.writerow([age_group[1], age_group[0]])

# Program 1
# with open("csv_files/colours_20.csv", encoding="utf-8") as csv_file:
# reader = csv.reader(csv_file)
# for line in reader:
#     print(line[1], line[2], line[4])

# Program 2/3

# with open("csv_files/colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)

#     next(reader)

#     for line in reader:
#         print(f"{line[4]} , Hex: {line[2]} , RGB: {line[1]}")

# Program 4
# with open("csv_files/colours_213.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)

#     next(reader)

#     yellow = 0
#     green = 0
#     blue = 0
#     red = 0

#     for line in reader:
#         print(line[4])
#         if "yellow" in line[4]:
#             yellow += 1
#         if "blue" in line[4]:
#             blue += 1
#         if "green" in line[4]:
#             green += 1
#         if "red" in line[4]:
#             red += 1


# print(yellow)
# print(blue)
# print(green)
# print(red)

# Program 5
with open("csv_files/galaxies.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)

    next(reader)

    min_galaxy = reader[0][0]
    max_galaxy = reader[0][0]
    min_velocity = reader[0][1]
    max_velocity = reader[0][1]
    index = 1

    for line in reader:
        if min_velocity < reader[index]:
            index += 1
