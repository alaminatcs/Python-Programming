# set: is an unordered, unindexed multiple value container.
# it's not contain any duplicate values.
# it's faster than list compared to check an element remains or not
# ---------------------------------------------------------

fruits = {'mango', 'jackfruit', 'lichi', 'apple', 'guava'}
# print(fruits)
# Output: {'jackfruit', 'lichi', 'guava', 'apple', 'mango'}     #unordered


# add a new element to the set
# --------------------------------------------------------- 
fruits.add('watermelon')
# print(fruits)
# Output: {'lichi', 'watermelon', 'guava', 'jackfruit', 'mango', 'apple'}


# remove an element from the set
# ---------------------------------------------------------
fruits.remove('watermelon')
# print(fruits)
# Output: {'lichi', 'apple', 'mango', 'guava', 'jackfruit'}


# clear the set
# ---------------------------------------------------------
# fruits.clear()
# print(fruits)
# Output: set()


# update a set by adding another set
# ---------------------------------------------------------
additonal_fruits = {'watermelon', 'date', 'apple'}
# fruits.update(additonal_fruits)   # additional_fruits.update(fruits)
# print(fruits)
# Output: {'date', 'lichi', 'apple', 'jackfruit', 'guava', 'mango', 'watermelon'}


# join two sets and create a new set by union
# ---------------------------------------------------------
total_fruits = fruits.union(additonal_fruits)
# print(total_fruits)
# Output: {'watermelon', 'lichi', 'guava', 'date', 'jackfruit', 'apple', 'mango'}


# identify the common element between two sets
# ---------------------------------------------------------
print(fruits.intersection(additonal_fruits))    # Output: {'apple'}


# identify the difference from one set to another
# ---------------------------------------------------------
print(fruits.difference(additonal_fruits))
# Output: {'guava', 'lichi', 'jackfruit', 'mango'}

print(additonal_fruits.difference(fruits))
# Output: {'watermelon', 'date'}