'''
Problem Name:
Problem Link:

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
def ret_fun(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div

a, b = map(int, input().split())
output = ret_fun(a, b)
print(output)