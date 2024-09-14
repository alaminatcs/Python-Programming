# by default input() takes input as string
# ----------------------------------------
name = input('Put your name: ')
# type-casting input string into integer
# ----------------------------------------
age = int(input('Put your age: '))
# type-casting input string into float
# ----------------------------------------
height = float(input('Put your height: '))

print('\nHello ' + name)
print('You are ' + str(age) + ' years old')
print('You are ' + str(height) + 'cm tall')