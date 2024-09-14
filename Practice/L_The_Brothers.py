'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/L

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
s1, s2 = map(str, input().split())
s3, s4 = map(str, input().split())
if s2 == s4:
    print('ARE Brothers')
else:
    print('NOT')
