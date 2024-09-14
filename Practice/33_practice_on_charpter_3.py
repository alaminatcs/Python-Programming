'''
#multiplication table
num = int(input('Enter the number: '))
for i in range(1, 11):
    print(num, '*', i, '=', num*i)

'''
'''
#factorial
num = int(input('Enter the number: '))
fact = 1
for i in range(1, num+1):
    fact *= i
print('Factorial is: ', fact)

'''
'''
#fibonacci series
first, second = 0, 1
for i in range(1, 11):
    print(first, end=' ')
    rem = first+second
    first = second
    second = rem
print()

'''
'''
#count the number of digit in a number
inp = int(input('Enter the number: '))
cnt = 0
while inp:
    cnt += 1
    inp = inp//10
print('number of digit is: ', cnt)

#using length function
inp = input('Again, enter the number: ')
print('Length function use kore length ber kora:', len(inp))

'''
'''
#Armstrong Number

inp = int(input('Enter the no: '))
sum = 0
len = len(str(inp))
rem = inp
while (inp):
    a = inp%10
    inp //= 10
    sum += a**len
if(sum == rem):
    print('Armstrong Number')
else:
    print('Not Armstrong Number')

#Armstrong method-2
inp = input()
sum = 0
for i in inp:
    sum += int(i)**len(inp)

if(str(sum) == inp):
    print('Armstrong')
else:
    print('Not Armstrong')

'''
#Integer Reverse
inp = int(input('enter no: '))
rev = 0
while inp:
    rev = rev*10+(inp%10)
    inp //= 10
print(rev)
