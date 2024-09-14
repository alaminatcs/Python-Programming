'''
Problem Name:
Problem Link: https://www.codechef.com/DSAPREP_01/problems/FNDINT

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
test = int(input())
for _ in range(test):
    x = int(input())
    x = x + 1
    while True:
        rem = str(x)
        status = 1
        for i in range(0, len(rem)-1):
            for j in range(i+1, len(rem)):
                if rem[j] == rem[i]:
                    status = 0
                    break
        if status:
            print(x)
            break
        else: x = x + 1
