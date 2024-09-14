'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/V

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
a, s, b = map(str, input().split())
a = int(a)
b = int(b)

if s == '<':
    if a < b: print('Right')
    else: print('Wrong')
elif s == '>':
    if a > b: print('Right')
    else: print('Wrong')
else:
    if a == b: print('Right')
    else: print('Wrong')