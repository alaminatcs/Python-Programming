'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
def solve_fun():
    x, y = map(int, input().split())
    i = min(x, y)
    j = max(x, y)
    sum = 0
    if i%2 == 0:
        for i in range(i+1, j,  2):
            sum = sum + i
    else:
        for i in range(i+2, j, 2):
            sum = sum + i
    print(sum)

tc = int(input())
for i in range(tc):
    solve_fun()