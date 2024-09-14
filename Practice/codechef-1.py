'''
Problem Name:
Problem Link: https://www.codechef.com/DSAPREP_01/problems/PMD7

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
import math
test = int(input())
for i in range(test):
    x, m = map(int, input().split())
    res = 0
    while x:
        rem = x % 10
        rem = pow(rem, m, 10)
        res = res * 10 + rem
        x = x // 10

    if res % 7: print('NO')
    else: print('YES')