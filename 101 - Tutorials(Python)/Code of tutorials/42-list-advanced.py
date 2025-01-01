'''
#taking multiple string input from user and store it in a list
inp = input('Enter your input: ').split(' ')        #split('which_character_should_define_the_dividing_part')
print(inp)

#taking multiple integer input from user and store it in a list
inp = list(map(int, input('Enter your list: ').split()))
print(inp)

#taking multiple float input from user and store it in a list
inp = list(map(float, input('Enter your list: ').split()))
print(inp)

'''
'''
#add/sub/mul/div with each element of list
ar = [1, 2, 3, 4, 5]            
ar = [i*5 for i in ar]          #[(expression-what to want with item) for item in list]
print(ar)

#iterating through a string using list comprehension
st = 'hello world'
st = [i for i in st]          #dif_way: st = list(st)
print(st)

#using range function in list comprehension
ar = [i for i in range(1, 10, 2)]       #dif_way: ar = list(range(1, 10, 2))
br = [i for i in range(2, 11, 2)]       #dif_way: ar = list(range(2, 10, 2))
print(ar)
print(br)

#list comprehension using if_else statement
ar = [i for i in range(1, 20) if(i%2 == 0)]
print(ar)

ar = [i for i in range(1, 20) if(i%2 != 0)]
print(ar)

ar = [i for i in range(1, 20) if(i%2==0 and i%2!=0)]
print(ar)

ar = [i for i in range(1, 20) if(i%2==0 or i%2!=0)]
print(ar)

ar = ['Odd' if(i%2) else 'Even' for i in range(1, 20)]
print(ar)

'''
'''
#2D list comprehension

#Transpose matrix conversion    #brute_force_way
ar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
br = []
for row in range(3):
    cr = []
    for col in ar:
        cr.append(col[row])
    br.append(cr)
print(br)

#Transpose matrix conversion    #short_cut_way
ar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
br = [[col[row] for col in ar] for row in range(3) ]
print(br)

'''
#swaping list two elements- day-10(v: 46)