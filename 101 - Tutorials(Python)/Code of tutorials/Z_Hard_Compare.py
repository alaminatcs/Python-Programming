'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Z

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
import math
a, b, c, d = map(int, input().split())

r1 = b*math.log(a)
r2 = d*math.log(c)
if r1 > r2: print('YES')
else: print('NO')