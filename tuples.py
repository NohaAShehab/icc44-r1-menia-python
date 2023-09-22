# 
#
""" based sequence """
# 
""" non primitive datatype ? -->"""
"1- define a tuple"
'empty tuples are falsy values'
t= ()
myt = tuple()
# 
""" 2-tuple can hold different values from different datatype even another tuple"""
myl = ('ahmed', 'omar', True, 333.33, 55, 'iti', 'test', 'iti', ('python', 'django', 'odoo'), None)
# 
"4- you can access tuple elements using index --> starts from 0 "
print(myl[5])
print(myl[8][1])
"5- tuple is immutable "
# myl[2] = 'updated'




'11- tuple concat'
t1 = ('python', 'django', 'odoo')
# t2 = ('docker', 'mysql', 20)
# t3 = t1 + t2
# print(t3)


'14-for loop over the tuple '

for item in t1:
    print(f'item ={item}')
# 
'14- print item and its index ? '

for index, item in enumerate(t1):
    print(f'{index}:{item}')


# ### shallow copy in
l1= (4444,444)
l2 = l1  # refer to the same address in the memory
# 


# """in operator ---> hint can be used with string """
print('iti' in myl)
# 
'generate tuple of numbers '

nums = range(1,11,3)
print(nums)  # range object ===>
nums = tuple(nums)
print(nums)
# 
'you can cast string to tuple and vice versa'
name = 'noha'
name = tuple(name)
print(name)
# 

# 
'join tuple elements to one string ===> tuple elements must be all strings'
names = ('abc', 'mmm', 'sss')
stds = '_'.join(names)
print(stds)