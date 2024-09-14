'''
Problem Name:
Problem Link:

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
def all_sum(a, b, *args):
    sum = a + b
    for i in args:
        sum = sum + i
    return sum

def all_sum_kargs(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(all_sum(5, 7, 9, 10))
print(all_sum_kargs(5, 7, 9, 10))
