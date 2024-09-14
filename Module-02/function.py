'''
Problem Name:
Problem Link:

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')

'''
def sum_fun(a, b):
    return a + b

def sub_fun(x, y):
    print(x - y)

a = int(input())
b = int(input())

print(sum_fun(a, b))
sub_fun(a, b)

def seq_check(first, last):
    print(first)
    print(last)

seq_check(last='Al', first='Hasan')     #In Py seq automatically detected if u provide key
seq_check(last='Hasan', first='Al')     #even if u didn't pass parameters sequentially