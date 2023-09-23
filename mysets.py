"""
    lists
    tuple
    set

    set ---> unordered datatype
    ---> remove duplication
    --> no index
"""

"1- define a set "
mys = set()


"2- set can hold different data from different datatypes"
ss = {'Ahmed', 'iti', 'noha',44,True, None, 44.44,'iti', 'python'}
print(ss)

" set is mutable  unordered datatype "

"3- add element to specific position"
ss.add('added element')
print(ss)

'4- get len of the set'
print(len(ss))
'5- check if the element exists in the set ... '
print('iti' in ss)

'6- pop element from the set ---> randomly'
popped_element = ss.pop()
print(popped_element)
print(ss)

"7- remove element from the set  --> known object"
ss.remove('iti')
print(ss)

'8- update the set '

myinfo = {"noha", 'Cairo', 'iti'}
ss.update(myinfo)
print(ss)


'add tuple, set to a set'

# myset = {'Ahmed', 'iti', 25, ('python', 'django', 'odoo', 'flask'), True}
# print(myset)

'what about adding a list'
# myset = {'Ahmed', 'iti', 25, ['python', 'django', 'odoo', 'flask'], True}
# print(myset) #TypeError: unhashable type: 'list'


""" set store only hashable datatype  =immutable= """






















