# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# # print(chilli_wishlist[0:4:2])
# # print(chilli_wishlist[1])
# # chilli_wishlist.append("dig mat")
# chilli_wishlist[2] = "ball"
# print(chilli_wishlist)

# sarah = [[3, 5], ["blue", "pink"]]
# print(sarah[1])
# print(sarah[0])
# print(sarah[1][1])

# print(len(chilli_wishlist))
# Prints the length of items in the list

# print(chilli_wishlist[4])
# Prints the 4th index item in the list

# print(chilli_wishlist[-1])
# prints the last item in the list

# print(chilli_wishlist[0:2])
# prints a split: prints each item from index value one to index value 2, excluding the index value 2

# print(chilli_wishlist[0:4:2])
# prints a split: prints each item from the index value one to index value 4, excluding value 4, also skipping every 2nd index value

# Adding and Removing Items

# chilli_wishlist.append("dig mat")
# adds one item to the list

# chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"])
# adds multiple items to the end of the list

# chilli_wishlist.insert(1, "peanut butter")
# adds the specified item to the list, at the location and before the index specified

# chilli_wishlist.pop()
# removes the last item from the list

# chilli_wishlist.pop(2)
# remove the item at index location 2

# chilli_wishlist.remove("donut toy")
# removes the specified item from the list

# Sublists
# chilli_wishlist = [
#     ["igloo"],  # bed
#     ["donut toy", "tennis ball", "crocodile toy"],  # toys
#     ["chicken", "peanut butter"],  # treats
#     ["cardboard box", "kong", "dig mat"]  # activity based toys
# ]

# prints items at index listing 2, then at that index, it prints items of index 1
# print(chilli_wishlist[2][1])
