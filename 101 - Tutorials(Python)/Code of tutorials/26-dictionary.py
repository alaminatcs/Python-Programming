# dictionary: used to contain multiple items as a key: value pairs.
# it allows to access item value quickly using hashing.
# syntax: dictionary_name = { key_name: value, ... }
# ----------------------------------------------------------------

birthPlaces = {'abir': 'dhaka', 'sabir': 'chittagong', 'kabir': 'sylhet'}
# print(birthPlaces)
# Output: {'abir': 'dhaka', 'sabir': 'chittagong', 'kabir': 'sylhet'}


# printing random individuals birthPlace among the dictionary
# -----------------------------------------------------------
# print(birthPlaces['kabir'])         # Output: sylhet
# print(birthPlaces['sabir'])         # Output: chittagong


# get() used to access a missing person's birthPlace to avoid error
# --------------------------------------------------------
# print(birthPlaces.get('bakkor'))    # Output: None
# print(birthPlaces.get('sabir'))     # Output: chittagong


# for all birthPlaces print using for loop
# ---------------------------------------------------------
for name in birthPlaces:
    # print(birthPlaces[name])
    pass


# show the keys of a dictionary as a list
# ---------------------------------------------------------
# print(birthPlaces.keys())
# Output: dict_keys(['abir', 'sabir', 'kabir'])


# show the keys and values of a dictionary as a list
# ---------------------------------------------------------
# print(birthPlaces.values())
# Output: dict_values(['dhaka', 'chittagong', 'sylhet'])


# show the items as a key-value pairs('dict_items')
# --------------------------------------------------------
# print(birthPlaces.items())
# Output: dict_items([('abir', 'dhaka'), ('sabir', 'chittagong'), ('kabir', 'sylhet')])

# show using for loop
for key, value in birthPlaces.items():
    # print(key + ": " + value)
    pass


# add a dictionary item
# --------------------------------------------------------
birthPlaces.update({'nadir':'rajshahi'})
# print(birthPlaces)
# Output: {'abir': 'dhaka', 'sabir': 'chittagong', 'kabir': 'sylhet', 'nadir': 'rajshahi'}


# update a dictionary item
# -------------------------------------------------------
# birthPlaces['kabir'] = 'khulna'
birthPlaces.update({'kabir': 'khulna'})
print(birthPlaces)
# Output: {'abir': 'dhaka', 'sabir': 'chittagong', 'kabir': 'khulna', 'nadir': 'rajshahi'}


# remove a dictionary item
# --------------------------------------------------------
# birthPlaces.pop('kabir')      
# print(birthPlaces)
# Output: {'abir': 'dhaka', 'sabir': 'chittagong', 'nadir': 'rajshahi'}

# birthPlaces.popitem() -> used to pop last updated one(see details)


# clear the dictionary items
# --------------------------------------------------------
birthPlaces.clear()
# print(birthPlaces)          # Output: {}