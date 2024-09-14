'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/W

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''

a, s, b, e, c = map(str, input().split())
a = int(a)
b = int(b)
c = int(c)

if s == '+':
    if a+b == c: print('Yes')
    else: print(a+b)
elif s == '-':
    if a-b == c: print('Yes')
    else: print(a-b)
elif s == '*':
    if a*b == c: print('Yes')
    else: print(a*b)