
"most versatile datatype in python ---> "

""" based sequence """

""" non primitive datatype ? -->"""
"1- define a list"
'empty lists are falsy values'
l= []
myl = list()

""" 2-list can hold different values from different datatype even another list"""
myl = ['ahmed', 'omar', True, 333.33, 55, 'iti', 'test', 'iti', ['python', 'django', 'odoo'], None]

"4- you can access list elements using index --> starts from 0 "
print(myl[5])
print(myl[8][1])
"5- list is mutable "
myl[2] = 'updated'
print(myl)
# myl[100]='added'
"6- append element to the list ---> to the end of the list "
myl.append('appended')
print(myl)

"7- insert element"
myl.insert(5, 'inserted')
print(myl)

myl.insert(100, 'inserted')
print(myl)
"8- pop element in the list"
popped_element = myl.pop()  # return the popped element
print(myl)
print(popped_element)
"9- pop element at specific index "
# popped_element =myl.pop(6)  #return the popped element
# print(myl)
# print(popped_element)


"10- remove element  --> remove first occurrence of the element"
myl.remove('iti')
print(myl)

'11- list concat'
l1 = ['python', 'django', 'odoo']
l2 = ['docker', 'mysql', 20]
l3 = l1 + l2
print(l3)

'12- extend a list '
# l1.extend(l2)
# print(l1)
'13- clear'
# l1.clear()


'14-for loop over the list '

for item in l1:
    print(f'item ={item}')

'14- print item and its index ? '

for index, item in enumerate(l1):
    print(f'{index}:{item}')

l1 = [4,455,44]
l2 = ['ahmed', l1]
l1.append('abc')
print(l2)

# ### shallow copy in non primitive
l1= [4444,444]
l2 = l1  # refer to the same address in the memory

l2.append('rrrr')
print(l1)

# ## deep copy
mm = [4,4,5,'eee']
nn=mm.copy()
mm.append('fffff')
print(nn)

"""in operator ---> hint can be used with string """
print('iti' in myl)

'generate list of numbers '

nums = range(1,11,3)
print(nums)  # range object ===>
nums = list(nums)
print(nums)

'you can cast string to list and vice versa'
name = 'noha'
name = list(name)
print(name)

'split string to the list'
message = 'hello world iti'
print(message.split(' '))
'sort list  ---> make sure that all the list items from the same type ? '
names  = ['Ahmed', 'john', 'mina','Mohamed', 'Mostafa', 'abdulrahman']
# names.sort()
# print(names)
names.sort(reverse=True)
print(names)
'reverse'
myl.reverse()
print(myl)


'join list elements to one string ===> list elements must be all strings'
stds = '_'.join(names)
print(stds)