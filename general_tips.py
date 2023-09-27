l = [1, 13, 3, 3, 44, 4, 44, 444, 7]
# a,b,c,d = l


a, *b, c = l

# with open('myfile.txt', 'w') as fileobj:
#     fileobj.write('---abc ')

# with open('myfile.txt', 'r') as fileobj:
#     for l in fileobj:
#         print(l)


# l = [num for num in range(1,11)]
# print(l)
#
# odd = [num for num in range(1,11) if num % 2 ==1]
# print(odd)
#
# nums = [1,2,3,4,5,6,7,8, 0, True, 19]
# print(all(nums))  # return True if all the elements represent True
# print(any(nums)) # return True if only one of the elements represents True


""" lambda : anonymous function """

# def sumnum(num1, num2):
#     return num1 + num2
#
# print(sumnum(3,3))


"you can create function --> used only in specific situation "

# myfun =lambda num1, num2: num1+ num2
#
# print(myfun(4,4))
#
# print(myfun(3,33))

users = [
    {"id": 1, 'name': 'John', 'track': 'python'},
    {"id": 2, 'name': 'Bob', 'track': 'python'},
    {"id": 3, 'name': 'Mohamed', 'track': 'ai'},
    {'id': 4, 'name': 'Abdulrahman', 'track': 'python'}
]


# def filteruser(user):
#     if user['track'] == "python":
#         return user


# python_students = filter(filteruser, users)
# print(list(python_students))

# def filteruser(user):
#     if user['track'] == "ai":
#         return user


# python_students = filter(filteruser, users)
# print(list(python_students))

# define function where I will use it
# python_students = filter(lambda user: user['track'] == 'python', users)
# print(list(python_students))



""" apply function on iterable """

# def formatstring(anystr):
#     return anystr.upper()
#
# names = ['John', 'Mina', 'Mohamed', 'Abdelrahman', 'Eslam', 'Ahmed']
#
# # newnames = map(formatstring, names)
# # print(newnames)
# # newnames = list(newnames)
# # print(newnames)
#
#
# newnames = map(lambda name: name.upper(), names)
# print(newnames)
# newnames = list(newnames)
# print(newnames)
#
#


### generator


# def generate_num():
#     for i in range(10):
#         return  i
#
#
# num1 = generate_num()
# print(num1)
#
# num2 = generate_num()
# print(num2)


def generate_num():
    for i in range(10):
        yield  i


num1 = generate_num()
print(num1)

print(next(num1))
print(next(num1))



for i in num1:
    print(i)


print(next(num1))












