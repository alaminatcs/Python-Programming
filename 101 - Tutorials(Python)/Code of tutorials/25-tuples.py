# tuple: similar to list but ordered and unchangable.
# used to group together related data.
# syntax: tuple_name = (item1, item2, ...)
# ---------------------------------------------------

fruits = ('mango', 'jackfruit', 'lichi', 'apple', 'lichi')
# print(fruits)
# Output: ('mango', 'jackfruit', 'lichi', 'apple', 'lichi')


# count('item_name') show an item how many times remains
# -----------------------------------------------------
# print(fruits.count('lichi'))        # Output: 2


# index('item_name') show the index of a specific item
# -----------------------------------------------------
# print(fruits.index('apple'))       # Output: 3


# in used to show an item remains or not
# ----------------------------------------------------
if 'lichi' in fruits:
    # print('It remains in your tuple')
    pass

for item in fruits:
    # print(item)
    pass