#Arithmetic Operators
# --------------------------------------------------------------

var1, var2 = 17, 6

#addition
print(var1 + var2)

#subtraction
print(var1 - var2)

#multiplication
print(var1 * var2)

#division
print(var1 / var2)

#modulus
print(var1 % var2)

#floor division
print(var1 // var2)

#power eg: a^b
print(var1 ** var2)


# Comparison Operators: It returns boolean values: True or False
# -------------------------------------------------------------------------

#less than
print(5 < 10)
print(10 < 5)

#greater than
print(5 > 10)
print(10 > 5)

#less than OR equal
print(5 <= 10)
print(10 <= 5)

#greater than OR equal
print(5 >= 10)
print(10 >= 5)

#equal
print(5 == 10)
print(10 == 10)

#not equal
print(5 != 10)
print(5 != 5)


# Logical Operators
# --------------------------------------------------------------
x, y = True, False
result = x and y                    # False
result = x or y                     # True
result = not x                      # False

# print(5 == 5 and 3 == 3)          # True
# print(5 == 5 and 3 == 1)          # False

# print(5 == 5 or 3 == 1)           # True
# print(5 == 4 or 3 == 3)           # True
# print(5 == 4 or 3 == 2)           # False


# Bitwise Operators
# --------------------------------------------------------------
a = 10                                  # Binary: 1010
b = 5                                   # Binary: 0101

# &: Bitwise AND
result = a & b                          # Binary: 0000 (Decimal: 0)

# |: Bitwise OR
result = a | b                          # Binary: 1111 (Decimal: 15)

# ^: Bitwise XOR
result = a ^ b                          # Binary: 1111 (Decimal: 15)

# ~: Bitwise NOT
result = ~a                             # Binary: 10101 (Decimal: -11)

# <<: Left shift
result = a << 2                         # Binary: 101000 (Decimal: 40)

# >>: Right shift
result = a >> 2                         # Binary: 0010 (Decimal: 2)


# Membership Operators
# -----------------------------------------------------------------------
my_list = [1, 2, 3]

# in: Checks if a value is in a sequence
result = 2 in my_list                   # True

# not in: Checks if a value is not in a sequence
result = 4 not in my_list               # True


# Identity Operators
# -----------------------------------------------------------------------
x = [1, 2, 3]
y = x

# is: Checks if two objects are the same object
result = x is y                        # True

# is not: Checks if two objects are not the same object
result = x is not y                    # False