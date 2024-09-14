'''
Problem Name:
Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
'''
n = int(input())
inp_list = input()
numbers = [int(x) for x in inp_list.split()]

counter = 0
while True:
    rem = True
    for i in range(n):
        if numbers[i]%2 == 1:
            rem = False
            break
        else:
            numbers[i] = numbers[i] // 2
    if rem:
        counter = counter + 1
    else:
        break

print(counter)
