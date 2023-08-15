'''

#takes value of length and breadth of a rectangle from user and check if it is square or not?

length = int(input('Enter the length of the Rectangle: '))
breadth = int(input('Enter the breadth of the Rectangle: '))
if(length == breadth): print("It is a Square.")
else: print('It is a Rectangle.')

'''
'''
#takes three integer input from user and find the largest number between using if-elif-else statement.

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
if(n1>=n2 and n1>=n3): print('largest number is: ', n1)
elif(n2>=n3 and n2>=n1): print('largest number is: ', n2)
else: print('largest number is: ', n3)

'''
'''
#write a program using conditional statement whether a number is even or odd.

num = int(input('Enter the number: '))
if(num==0): print('It\'s Zero')
elif(num%2): print('Odd number.')
else: print('Even number.')

'''
'''
#grade calculation

num = int(input('Enter your number: '))
if(num>90): print('A')
elif(num>80 and num<=90): print('B')
elif(num>=60 and num<=80): print('C')
else: print('D')

'''
#leap year calculation
year = int(input('Enter the year: '))
if(year%400 == 0): print(year, ' is Leap year')
elif(year%4==0 and year%100!=0): print(year, ' is Leap year.')
else: print(year, ' is not a Leap year.')