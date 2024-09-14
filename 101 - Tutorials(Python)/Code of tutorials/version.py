thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)

i = 0
n = len(thislist)
for element in thislist:
	if element == 'banana':
		thislist.pop(i)
	i += 1
print("\n", thislist)