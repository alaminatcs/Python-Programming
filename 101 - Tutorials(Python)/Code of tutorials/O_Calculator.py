'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/O

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
st = input()
f = ''
s = ''
r = ''
rem = 0
for i in st:
    if rem==0 and (i>='0' and i<='9'):
        f = f+i
    elif rem==1 and (i>='0' and i<='9'):
        s = s+i
    else:
        rem = 1
        r = r + i

f = int(f)
s = int(s)
if r == '+':
    print(f+s)
elif r == '-':
    print(f-s)
elif r == '*':
    print(f*s)
elif r == '/':
    print(f/s)


