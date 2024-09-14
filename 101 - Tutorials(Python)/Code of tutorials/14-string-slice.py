# by using indexing method u can slice a sub-string
# syntax: var_name = str_name[start : end(exclusive) : step]
# by default values of args: start-0, end-size, step-1
# ----------------------------------------------------------


varsity = 'Unknown University Of Engineering and Technology'
# print(len(varsity))             # Output: 48
# ----------------------------------------------------------
# print(varsity[:11])             # Output: Unknown Uni
# print(varsity[8:])              # Output: University Of Engineering and Technology


# here step-6 means step after each 5 char
# ----------------------------------------------
# print(varsity[::6])             # Output: Une gidn


# (-)ve index starts count from backward, it's start with -1
# ---------------------------------------------------------------
# print(varsity[:-30])             # Output: Unknown University
# print(varsity[8:-15])            # Output: University Of Engineering


# negative step means reverseing the string
# for (-)ve step: start reading from back to forward
# -------------------------------------------------------------------
# print(varsity[::-1])               # Output: ygolonhceT dna gnireenignE fO ytisrevinU nwonknU
# print(varsity[::-2])               # Output: yoohe n nrein Oyirvn wnn
# print(varsity[6::-1])              # Output: nwonknU
# print(varsity[32:7:-1])            # Output: gnireenignE fO ytisrevinU



# slice() method is more convenient cause of reusability of slice object
# syntax: slice(start, end, step)
# -------------------------------------------------------------------
# eg: to extract the website main-name
slice_part = slice(8, -4)             # removing 'https://' and '.com/org' part

web = 'https://python.org'
# print(web[slice_part])              # Output: python

web = 'https://python-django.com'
# print(web[slice_part])              # Output: python-django

slice_part = slice(8, -4, 2)
# print(web[slice_part])              # Output: pto-jno
