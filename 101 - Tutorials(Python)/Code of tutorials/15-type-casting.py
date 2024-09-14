#string to int type conversion
# ------------------------------------------------------
var = '15'
# print(type(var))         # Output: <class 'str'>

var = int(var)
# print(type(var))         # Output: <class 'int'>


# string to float type conversion
# ------------------------------------------------------
var = '15'
# print(type(var))           # Output: <class 'str'>

var = float(var)
# print(type(var))           # Output: <class 'float'>


# string to boolean type conversion
# empty string == False,    not empty string == True
# ------------------------------------------------------
var = '15'
# print(type(var))             # Output: <class 'str'>

var = bool(var)
# print(type(var))             # Output: <class 'bool'>


# integer to string type conversion
# ------------------------------------------------------
var = 1234
# print(type(var))               # Output: <class 'int'>

var = str(var)
# print(type(var))               # Output: <class 'str'>


# integer to float type conversion
# ------------------------------------------------------
var = 1234
var = float(var)
# print(type(var))               # Output: <class 'float'>


# integer to boolean type conversion
# 0 == False        -n, ..., -1, 1, ..., n == True
# ------------------------------------------------------
var = -1
# print(type(var))               # Output: <class 'int'>

var = bool(var)
# print(type(var))               # Output: <class 'bool'>


# float to string type conversion
# ------------------------------------------------------
var = 123.7
# print(type(var))               # Output: <class 'float'>

var = str(var)
# print(type(var))               # Output: <class 'str'>


# float to int type conversion
# ------------------------------------------------------
var = 136.2
# print(type(var))                 # Output: <class 'float'>

var = int(var)
# print(type(var))                 # Output: <class 'int'>


# float to boolean type conversion
# ------------------------------------------------------
var =  1.804
# print(type(var))                 # Output: <class 'float'>

var = bool(var)
# print(type(var))                 # Output: <class 'int'>