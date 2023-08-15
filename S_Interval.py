'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/S

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
var = float(input())

if var>=0 and var<=25:
    print('Interval [0,25]')
elif var>25 and var<=50:
    print('Interval (25,50]')
elif var>50 and var<=75:
    print('Interval (50,75]')
elif var>75 and var<=100:
    print('Interval (75,100]')
else:
    print('Out of Intervals')
