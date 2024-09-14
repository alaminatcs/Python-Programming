'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/H

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
a, b = map(int, input().split())
res = a / b
res2 = a // b

print('floor', a, '/', b, '=', res2)

decp = (res-res2)*100
if decp == 0.0:
    print('ceil', a, '/', b, '=', res2)
else:
    print('ceil', a, '/', b, '=', res2+1)

if decp >= 50.0:
    print('round', a, '/', b, '=', res2+1)
else:
    print('round', a, '/', b, '=', res2)