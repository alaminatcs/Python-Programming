# ------------------#
# Basic Operations  #
# ------------------#

# len(string): Returns the length of the string (number of characters).
# -----------------------------------------------------------------------
# print(len('Alamin Hasan'))                 # Output: 12


# string.upper(): Converts all characters in the string to uppercase.
# -----------------------------------------------------------------------
# print('Alamin Hasan'.upper())             # Output: ALAMIN HASAN


# string.lower(): Converts all characters in the string to lowercase.
# -----------------------------------------------------------------------
# print('Alamin Hasan'.lower())             # Output: alamin hasan


# string.capitalize(): Capitalizes the first character of the string and makes the rest lowercase.
# -----------------------------------------------------------------------
# print('amar sonar bangla'.capitalize())   # Output: Amar sonar bangla


# string.title(): Capitalizes the first character of each word in the string.
# ------------------------------------------------------------------------
# print('amar sonar bangla'.title())        # Output: Amar Sonar Bangla


# string.swapcase(): swaps the case of all characters in the string (uppercase becomes lowercase and vice versa).
# ------------------------------------------------------------------------
# print('Alamin Hasan'.swapcase())          # Output: aLAMIN hASAN


# string.isdigit(): Returns True if all characters in the string are digits, otherwise False.
# ------------------------------------------------------------------------
# print('Alamin Hasan'.isdigit())           # Output: False
# print('1234'.isdigit())                   # Output: True
# print('12 34'.isdigit())                  # Output: False


# string.isalpha(): Returns True if all characters in the string are alphabetic, otherwise False.
# ------------------------------------------------------------------------
# print('Alamin Hasan'.isalpha())           # Output: False
# print('alaminhasan'.isalpha())            # Output: True
# print('ala23ihasan'.isalpha())            # Output: False


# string.isalnum(): Returns True if all characters in the string are alphanumeric (digits or letters), otherwise False.
# ------------------------------------------------------------------------
# print('Alamin Hasan'.isalnum())           # Output: False
# print('alaminhasan'.isalnum())            # Output: True
# print('ala23ihasan'.isalnum())            # Output: True
# print('ala23ih@asan'.isalnum())           # Output: False



# ----------------------#
# Searching Operations  #
# ----------------------#

# string.find(substring): Returns the index of the first occurrence of the substring in the string, or -1 if not found.
# var_name.find('sub_str', start(optional), end(optional))
# ------------------------------------------------------------------
# print('Alamin Hasan'.find('as'))                         # Output: 8
# print('Alamin Hasan'.find('as', 9))                      # Output: -1 //not reamins from index 9


# string.rfind(substring): Returns the index of the last occurrence of the substring in the string, or -1 if not found.
# -------------------------------------------------------------------
# print('Alamin Hasan'.rfind('a'))                          # Output: 10
# print('i am alamin, i am an old person.'.rfind('am'))     # Output: 15


# string.startswith(prefix): Returns True if the string starts with the specified prefix, otherwise False.
# -------------------------------------------------------------------
# print('i am alamin, i am an old man'.startswith('am'))      # Output: False
# print('am alamin, i am an old man'.startswith('am'))        # Output: True


# string.endswith(suffix): Returns True if the string ends with the specified suffix, otherwise False.
# -------------------------------------------------------------------
# print('i am alamin, i am an old man'.endswith('man'))        # Output: True
# print('i am alamin, i am an old boy'.endswith('man'))        # Output: False


# string.count(substring): Returns the number of occurrences of the substring in the string.
# -------------------------------------------------------------------
# print('alamin hasan'.count('a'))                             # Output: 4
# print('alan akdj alan jalank adlan aka lan'.count('alan'))   # Output: 3
# print('alamin hasan'.count(''))                              # Output: 13
# print('alamin hasan'.count(' '))                             # Output: 1



# ----------------------#
# Modifying Operations  #
# ----------------------#

# string.replace(old, new): Replaces all occurrences of the old substring with the new substring.
# --------------------------------------------------------------------
# print('alamin'.replace('i', '_'))                 # Output: alam_n
# print('alamin'.replace('am', '_'))                # Output: al_in
# print('alamin'.replace('in', 'in hasan'))         # Output: alamin hasan


# string.strip(): Removes leading and trailing whitespace characters from the string.
# --------------------------------------------------------------------
# print('   hello world   '.strip())                  # Output: hello world
# print('   hello world   '.lstrip())                 # Output: hello world         //left
# print('   hello world   '.rstrip())                 # Output:    hello world      //right


# string.split(): Splits the string into a list of substrings based on specific characters.
# --------------------------------------------------------------------
# print('my name is: alamin hasan'.split(':'))         # Output: ['my name is', ' alamin hasan']


# string.splitlines(): Splits the string into a list of substrings based on newline characters.
# --------------------------------------------------------------------
# print('my name is\n alamin hasan'.splitlines())      # Output: ['my name is', ' alamin hasan']
# print('''my name is
# alamin hasan'''.splitlines())                        # Output: ['my name is', 'alamin hasan']


# string.join(iterable): Joins the elements of an iterable (e.g., list, tuple) into a single string using the string as a separator.
# ---------------------------------------------------------------------
fruits = ["apple", "banana", "orange"]
# print(' | '.join(fruits))                            # Output: apple | banana | orange


# F-strings allow you to embed expressions within string literals, making it easier to format strings dynamically.
# --------------------------------------------------------------------
name, age = "Alice", 30
greeting = f"Hello, {name}. You are {age} years old."
# print(greeting)                                      # Output: Hello, Alice. You are 30 years old.


# string multiplication with number allowed in python
# --------------------------------------------------------------------
# print('am ' * 3)                                     # Output: am am am 
# print('al-amin ' * 2)                                # Output: al-amin al-amin