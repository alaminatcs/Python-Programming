'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/X

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
l1, r1, l2, r2 = map(int, input().split())

if((l1<l2 and r1<l2) or (l1>r2 and r1>r2) or (l2<l1 and r2<l1) or (l2>r1 and r2>r1)):
    print(-1)
elif (l1<=l2 and l2<=r1):
    if r1 <= r2:
        print(l2, r1)
    else:
        print(l2, r2)
elif (l1>l2 and l2<=r1):
    if(r1 <= r1):
        print(l1, r1)
    else:
        print(l1, r2)

