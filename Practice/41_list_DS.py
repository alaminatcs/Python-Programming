'''
#list DS
ar = ['chal', 'dal', 'alu', 'piyaj', 1, 0.5, .25, .05]
print(ar)
#show a specific elements from list and change it later.
print(ar[3])
ar[3] = 'spice'
print(ar[3])
print(ar)

#traverse the list
for i in ar:
    print(i)

#traverse the list using index
for i in range(len(ar)):
    print(ar[i])

#reverse traversing
for i in range(len(ar)-1, -1, -1):
    print(ar[i])
#negative indexing
for i in range(-1, -len(ar)-1, -1):
    print(ar[i])

#find an elements into the list DS
if 'alu' in ar:
    print('Yes, it remains into the list')
else:
    print('Not into the list')

#list slicing 
print(ar[::])       #[first_index : last_index : step]
print(ar[1: 4: 1])
print(ar[1: : 2])
print(ar[-1: -5: -1])

'''
#list built in methods

#addition method
list1 = [1, 3, 4]
list2 = [5, 6, 7]

print(list1+list2)
print(list2+list1)

#copy list
list3 = list1.copy()        #method-1
list4 = list2               #method-2
print(list3)
print(list4)

#add an element at the end of list
list3.append(2)
print(list3)

#insert an element at a specific index
list1.insert(1, 2)      #insert(index_no, element)
print(list1)

#convert string into list
str = 'hello world'
lst = list(str)
print(lst)

#count an element remains in a list
ar = [1, 2, 3, 3, 4, 5, 3, 2, 3]
print(ar.count(5))

#add multiple elements in a list
ar.extend([11, 12, 13])         #method-1
print(ar)

ar += [14, 15, 16]              #method-2
print(ar)

#remove last element
ar.pop()
print(ar)

#remove a specific element
ar.remove(3)
print(ar)

#reverse list
ar.reverse()            #method-1
print(ar)
ar = ar[::-1]
print(ar)

#sort list
ar.sort(reverse = True)     #descending order
print(ar)
ar.sort()       #ar.sort(reverse = True) -> ascending order             
print(ar)

#max / min element finding
print(max(ar))
print(min(ar))