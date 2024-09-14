'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y
'''
n = int(input())

fibo = [0, 1]
for ind in range(2, n):
    fibo.append(fibo[ind-1] + fibo[ind-2])

if n == 1:
    print(0)
else:
    for val in fibo:
        print(val, end=' ')