
from re import L
from tkinter import PAGES


# class Book:
#     def __init__(self, title, author, pages, current_page):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = current_page
#         self.bookmark = 1

#     def bookmark_page(self):
#         self.bookmark = self.current_page

#     def turn_page(self):
#         self.current_page += 1

#     def turn_back_page(self):
#         self.current_page -= 1

#     def __str__(self):
#         return f"Title:{self.title}, Author:{self.author} Pages:{self.pages}"

#     def _len_(self):
#         return self.pages


# my_book = Book("A great book", "me", 198, 1)
# # print(my_book)

# my_book.bookmark_page()
# print(my_book.bookmark)

# my_book.turn_page()
# my_book.bookmark_page()
# print(my_book.bookmark)

# my_book.turn_back_page()
# my_book.bookmark_page()
# print(my_book.bookmark)


# Q2:
# import math

# class Rectangle:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width * 2) + (self.height * 2)

#     def diagonal(self):
#         result = math.sqrt((self.width * self.width) +
#                            (self.height * self.height))
#         return '{:.1f}'.format(result)

#     def square(self):
#         if self.width == self.height:
#             return("Square")
#         else:
#             return("Rectangle")

#     def __str__(self):
#         return f"Width: {self.width}, Height: {self.height}"


# my_rectangle = Rectangle(50, 60)
# print(my_rectangle)

# print(my_rectangle.area())
# print(my_rectangle.perimeter())
# print(my_rectangle.diagonal())
# print(my_rectangle.square())


# Q3 & Q4


# class Car:
#     def __init__(self, makemodel, colour, seating, speed):
#         self.makemodel = makemodel
#         self.colour = colour
#         self.seating = seating
#         self.speed = speed
#         self.fuel = 20

#     def __str__(self):
#         return f"Car Make: {self.makemodel}, Colour: {self.colour}, Seats: {self.seating}, Speed: {self. speed}"

#     def rev_engine(self):
#         print("VRMMMM!!!")

#     def driving(self):
#         self.fuel -= 5
#         if self.fuel < 10:
#             print("Warning: low Fuel")
#         print(f"Current fuel amount: {self.fuel}")

#     def fuel_up(self):
#         self.fuel += 20
#         if self.fuel >= 40:
#             print("Max Fuel is 40 litres buddy, hold off.")
#             self.fuel = 40
#         print(f"Current fuel amount: {self.fuel}")


# my_car = Car("Kia Rio", "Blue", 5, 120)
# # print(my_car)
# my_car.rev_engine()
# my_car.driving()
# my_car.driving()
# my_car.driving()
# my_car.fuel_up()
# my_car.fuel_up()
