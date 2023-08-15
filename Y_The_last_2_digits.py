'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Y

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
a, b, c, d = map(int, input().split())

a = a%100
b = b%100
c = c%100
d = d%100

if (a*b*c*d)%100 > 9: print((a*b*c*d)%100)
else:
    print('0',end='')
    print((a*b*c*d)%100)
