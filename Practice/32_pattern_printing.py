#pattern printing using nested loop

'''
#triangle pattern
i = 0
for i in range(6):
    j = 0
    for j in range(i):
        print('*', end=' ')
        j += 1
    i += 1
    print()

'''

ca = 97
i = 0
for i in range(6):
    j = 0
    for j in range(i+1):
        print(chr(ca), end=' ')
        j += 1
    i += 1
    ca += 1
    print()