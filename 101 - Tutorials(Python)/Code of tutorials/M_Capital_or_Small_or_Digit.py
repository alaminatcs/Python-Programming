'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/M

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
char = input()

if char>='a' and char<='z':
    print('ALPHA\nIS SMALL')
elif char>='A' and char<='Z':
    print('ALPHA\nIS CAPITAL')
elif char>='0' and char<='9':
    print('IS DIGIT')