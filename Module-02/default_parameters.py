'''
Problem Name:
Problem Link:

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
def all_sum(a, b, c=0, d=0):
    sum = a + b + c + d
    return sum

print(all_sum(5, 7, 9, 10))    #when you pass c, d value then they take it. 

print(all_sum(5, 7))           #when you don't pass c, d value they take default value 0