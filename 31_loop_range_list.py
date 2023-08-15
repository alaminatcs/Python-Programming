#loop, range, list
#loop- for loop, while loop, nested looping in for and while.
'''
#for loop syntax:
                # for (item) in (sequence with condition):
for i in range(0, 10, 1):
    print('step no:', i)                #range syntax: range(initial, final, increment/decrement)

for i in range(10, 0, -1):
    print('step no:', i)

string = 'hello python!'
for i in string:
    print(i)

'''
''' 
#range details and put it into a list
rng = range(10)
print(rng)

#list details using range
lst = list(range(10))
print(lst)
lst = list(range(0, 10, 2))
print(lst)

lst = ['rice', 'alu', 'piaj', 'tel', 1, .5, .25, .05]
for item in lst:
    print(item)
    
'''
'''
#print summation of first 10 numbers
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

'''
'''
#while loop
            # initialization
            # while (condition):
                #statement
                #.
                #.
                #.
                #counter update
lst = 'hello world!'
i=0
ch = lst[i]
while ch!='!':
    print(ch)
    i += 1
    ch = lst[i]
    
'''
'''
#break statement- eg: print numbers before up to the 5
i = 0
while i<10:
    if(i==5):
        break
    print(i)
    i += 1
#continue statement- eg: print numbers without 5 up to 9
i = 0
while(i<10):
    i += 1
    if(i==5):
        continue
    print(i)

'''
'''
#infinite loop only possible into the while loop but not into the for loop cause of range parameter limitation
 
 #nested loop
i = 1
while i<6:
    j = 1
    while j<6:
        print(i, '*', j, '=', i*j)
        j += 1
    i += 1
    print()

'''
#nested list
bajar_list = [['chal', 'dal', 'alu', 'mix_spice'], ['50 tk/kg', '80 tk/kg', '20 tk/kg', '90 tk/kg'], [1, 0.5, 0.5, 0.25]]
for item in bajar_list:
    for details in item:
        print(details, end='\t')
    print()