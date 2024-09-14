'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')

'''
tc = int(input())
for i in range(tc):
    n = int(input())
    while True:
        print(n%10, end='')
        n = n // 10
        if n:
            print(end=' ')
        else:
            print()
            break
    