# List used to store multiple elements of any type in a single variable
# syntax: list_name = [element1, element2, ...]
# ----------------------------------------------------------------------
nums = ['zero', 'one', 'two', 'three', 'four']
# print(nums)                     # ['zero', 'one', 'two', 'three', 'four']


# --------------------
# Accessing Elements #
# --------------------

# Syntax: list_name[index_number]
# ----------------------------------------------------------------------
second_nums = nums[1]           # one
fourth_nums = nums[3]           # three

# Slicing- Extract a portion of a list using slicing.
# Syntax: list_name[start : stop : step]
# -----------------------------------------------------------------------
nums[1:3]                       # ['one', 'two']
nums[1:]                        # ['one', 'two', 'three', 'four']


# -----------------
# Modifying Lists #
# -----------------

# Change elements using index
# list_name[index_number] = new_value_want_to_modify
# -----------------------------------------------------------------------
nums[1] = 'seven'               # ['zero', 'seven', 'two', 'three', 'four']

# Add elements using append() or insert().
# Syntax: list_name.append(item_name)
# ------------------------------------------------------------------------
nums.append('five')             # ['zero', 'seven', 'two', 'three', 'four', 'five']

# Add elements using insert().
# Syntax: list_name.insert(index_number, item_name)
# -----------------------------------------------------------------------
nums.insert(1, 'one')           # ['zero', 'one', 'seven', 'two', 'three', 'four', 'five']

# add multiple elements(new_list) into the last.
# Syntax:list_name.extend(new_list_name or [new_list_items])
# -------------------------------------------------------------------------
nums.extend(['six', 'seven', 'eight']) # ['zero', 'one', 'seven', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

# Remove first occurrence of specific elements using remove()
# Syntax: list_name.remove(element_name)
# -----------------------------------------------------------------------
nums.remove('seven')            # ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

# Remove specific index elements using pop()
# Syntax: list_name.pop(index_number), default last index, neg count from last
# --------------------------------------------------------------------------------
nums.pop()                      # ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']
nums.pop(6)                     # ['zero', 'one', 'two', 'three', 'four', 'five', 'seven']
nums.pop(-2)                    # ['zero', 'one', 'two', 'three', 'four', 'seven']

# Delete a specific element or multiple elements
# Syntax: del list_name[index_number], for multiple- [start : stop], for all- [:]
# ---------------------------------------------------------------------------------
del nums[5]                     # ['zero', 'one', 'two', 'three', 'four']
del nums[3:]                    # ['zero', 'one', 'two']


nums.extend(['four', 'five', 'two'])    # ['zero', 'one', 'two', 'four', 'five', 'two']


# -----------------
#  Lists Methods  #
# -----------------

# len(list_name): Returns the length of the list.
# -------------------------------------------------------------
len(nums)                       # 6

# list_name.count(element_name): return no of occurrences of the element in the list.
# -------------------------------------------------------------------------
nums.count('two')               # 2

# list_name.index(element_name): returns the index of the first occurrence of the element in the list.
# -------------------------------------------------------------------------
nums.index('two')               # 2

# list_name.reverse(): reverses the order of the elements in the list.
# -------------------------------------------------------------------------
nums.reverse()                  # ['two', 'five', 'four', 'two', 'one', 'zero']

# list.sort(): Sorts the elements in the list (ascending by default).
# -------------------------------------------------------------
nums.sort()                     # ['five', 'four', 'one', 'two', 'two', 'zero']

# list_name.copy(): Return a shallow copy of the list.
# ---------------------------------------------------------------
new_nums = nums.copy()          # ['five', 'four', 'one', 'two', 'two', 'zero']

# list_name.clear(): just clear the list
# ---------------------------------------------------------------
new_nums.clear()                # []


# -----------
#  2D List  #
#------------

# 2D List: refers to a list in which conatins lists
# ---------------------------------------------------------------
breakfast = ['rice', 'mashed potato', 'egg']
lunch = ['rice', 'vagitables', 'dal', 'curry']
dinner = ['bread', 'meat']

foods = [breakfast, lunch, dinner]
# print('overall items: ', foods)
# overall items:  [['rice', 'mashed potato', 'egg'], ['rice', 'vagitables', 'dal', 'curry'], ['bread', 'meat']]

# print('third item of lunch: ', foods[1][2])
# third item of lunch:  dal

# print('items of dinner: ', foods[2])
# items of dinner:  ['bread', 'meat']