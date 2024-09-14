'''
Problem Name:
Problem Link:

import sys
sys.stdin = open('E:/Skill Edu/CS Fundamental/Python-Programming/input.txt', 'r')
sys.stdout = open('E:/Skill Edu/CS Fundamental/Python-Programming/output.txt', 'w')
'''
def k_args(**kargs):                    #args with key need 2 star(**)
    for key, val in kargs.items():
        print(key, ":", val)

k_args(Fast='Al', Last='Hasan', Vil='Tarali', PS='Kaliganj', Dist='Satkhira', Div='Khulna')