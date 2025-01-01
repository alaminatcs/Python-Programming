#this file is about variable types with user taking user input

#takes user input and print it
# --------------------------------------------------------------------
print('user name: ', input('enter the user name: '), '\n')
#here input function always takes input and makes it's a string.


#string type variable
# --------------------------------------------------------------------
char_var = input("Enter the character type variable's value: ")
print('Character value: ', char_var, '\n')

str_var = input("Enter the string type variable's value: ")
print('String value: ', str_var, '\n')

multiline_str = '''this
is multiline string test.
i am just exploring this.'''
print('Multiline string:', multiline_str, '\n')


#number type variable
# --------------------------------------------------------------------
int_var = int(input("Enter the Integer type variable's value: "))
print('Integer value: ', int_var, '\n')

float_var = float(input("Enter the Float type variable's value: "))
print('Float value: ', float_var, '\n')


#list type variable
# --------------------------------------------------------------------
list_var = ['rice', 'tomato', 'onion', 'oil', 1, 0.5, 0.27, 0.02500005]
print('List value: ', list_var)


# Unpacking: unpack the elements(like a list, tuple, sets...) into individual variables.
# --------------------------------------------------------------------
print(*[1, 2, 3])                           #Output: 1 2 3

x, y, z = [1, 2, 3]
print(x, y, z)                              #Output: 1 2 3

x, *y = [1, 2, 3]
print(x, y)                                 #Output: 1 [2, 3]


# this is multi-line comment
'''
This is multiline comment:
int_var = 134
is_boolean = True
list_var = [3, 8, 1, 5, ]
'''