'''
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S
'''
inp = input()
ar = [x for x in inp]

i = 0; size = 0; lenth = len(inp)
numbers = []
while i < lenth:
    j = 0
    while i<lenth and ar[i]=='L':
        j = j + 1; i = i + 1
        
    k = 0
    while i<lenth and ar[i]=='R':
        k = k + 1; i = i + 1
    
    if min(j, k) > 0:
        numbers.append(min(j, k))
        size = size + 1

if size:
    print(size)
    for no in numbers:
        for i in range(no):
            print('L', end='')
        for i in range(no):
            print('R', end='')
        print()
else:
    print(0)