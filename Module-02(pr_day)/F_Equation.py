'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F
'''
x, y = map(int, input().split())
sum = -1
for i in range(0, y+1, 2):
    sum = sum + (x ** i)
print(sum)
