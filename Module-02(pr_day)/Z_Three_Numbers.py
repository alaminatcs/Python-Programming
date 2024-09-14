'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Z
'''
k, s = map(int, input().split())
counter = 0
for i in range(0, k+1):
    if i > s:
        break
    for j in range(0, k+1):
        if (i+j) > s:
            break
        elif s-(i+j) <= k:
            counter = counter + 1
    
print(counter)