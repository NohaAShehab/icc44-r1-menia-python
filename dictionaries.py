info = ['noha', 31, 'iti', 'cairo']





"comma seperated key value pair datatype "

'1- to define the dict '
d= {}
myd = dict()
'2- hold key:value pair --> comma '
'before python 3.7--> dict --> unordered ---> ---'
info = {
    'name':'Noha',
    'track': "opensource",
    'city': 'cairo',
    'work':'iti',
    'name': "Noha Shehab"
}
"dict doesn't allow key duplication ---? sets "
print(info)
'3- you access values of the dict using key '
print(info['name'])
'4- dict is mutable datatype '
info['city'] = 'October'
print(info)
info['country']='Egypt'
print(info)
'from 3.7 --> dict --> ordered datatype '
'5- pop element from the dict'
# popped_element = info.pop('country')
# print(popped_element)

'6- delete key:value '
# del info['city']

# info.clear()

'7-check if element exists in the dict '

print('iti' in info)  # check in the dict keys

'8- get keys of dict ?'
keys = info.keys()
print(keys, type(keys))
keys_list= list(keys)
print(keys_list)

'8- get values of dict ?'
values = info.values()
print(values, type(values))
values_list= list(values)
print(values_list)

'9- loop over the dict '

# for item in info:  # keys
#     print(item)

for item in info:  # keys
    print(f"{item}:{info[item]}")


enum_dict = enumerate(info)
print(enum_dict)
enum_dict = list(enum_dict)
print(enum_dict)

for index, key in enumerate(info):
    print(f"{index}:{key}:{info[key]}")
'10- update dict '
updated_info = {"fruits":'kiwi','food':'pizza', 'sleep':10}
info.update(updated_info)
print(info)
'11- get len of dict '
print(len(info))
'12- get items of the dict '

items = info.items()
print(items)
items = list(items)
print(items)

for k, v in info.items():
    print(f'{k}:{v}')


'13- clear dict '
