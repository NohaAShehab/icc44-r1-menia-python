"""
        any string is immutable datatype

        string content cannot be changed after creation ?


"""




iti = 'information technology institute'
print(iti, type(iti))
#
"1- get num of char in the string"
print(len(iti))
#
"2- count occurence of char in the string"
print(iti.count('ti'))
#
"3- slicing the string using index --> start from 0 "

"this operations returns with new string "
print(iti[1:3])


print(iti[2:6])
print(iti[6:2:-2])
print(iti[::-1])  # reverse string
#
#
"""4- get index of char --> get the index of the first occurrence of the char """
print(iti.index('i'))
#
#
"""5- replace char in the string """

res=iti.replace('i', '$',3)  # return new string
print(res)
#
#
"6- concat string  +"
fname ='noha '
midname = 'abdelhady '
lname = 'Shehab'
#
#
fullname = fname + midname+ midname + lname
print(fullname)
#
"""7- string interpolation"""
#
fullname = fname + midname*2 + lname
print(fullname)
#
#
# """8- string format """

# no_of_students = 10
# course = 'python'
# #
# temp = "We have {0} student in {1} course."
# print(temp)
# # format this template with the given values
# print(temp.format(no_of_students,course))
#
# print(temp.format(course, no_of_students))
# #
# "keyword argument"
# temp = "We have {stds} students in {crs} course."
# #
# print(temp.format(stds=no_of_students, crs=course))
# print(temp)
#
# ###################################################
"9- format string  using f-format string "
""" format string depends on existing variables in the script """
# course = 'python'
# no_of_students = 25
# # #
# mystr = f'We have {no_of_students} student studying {course} course.'
# print(mystr)
#
#
"""10- format string itself"""
fullname = 'noha abdelhady shehab'
print(fullname.capitalize())
print(fullname.upper())
print(fullname.lower())
print(fullname.title())  # capitalize first char in each word
#
"11- ask user to enter value "

# myval = input('please enter val') # input function always returns with String
# #
# print(myval, type(myval))
# #
# num1 = input('please enter num1 : ')
# num2 = input('please enter num2 : ')
# res = num1 + num2
# print(res)
# res = int(num1) + int(num2)
# print(res)
"""12- check content of the string """
# #
# myval = input("please enter value")   ## always returns with string
# # #
# print(myval.isdigit())
# print(myval.isalpha())
# print(myval.islower())
# print(myval.isupper())
# print(myval.isspace()) # return True --> if the string consists only from spaces
# #
# # ask user for input ---> operation arithmetic ---> You must check if the value is int or not
# num = input("please enter number: ")
# print(num.isdecimal())
# num = float(num)
# """strip string ? ===> """
#
message= '      My name is Noha, Nice to meet you all          '
print(len(message))
print(message)
#
print(message.strip())  # strip white spaces from the beginning and the end of the string
print(message.lstrip())
print(message.rstrip())

#
print(message.strip("lM "))  # strip chars from the beginning and the end of the string
# print(message.lstrip("LM "))
# print(message.rstrip("lMa um"))
#
#
""" iterate over the string """

for item in message:
    print(f'item = {item}')

"in operator ---> "
print('n' in 'noha')

'enumerate function ? --> generate index for iterable'

# index= 0
# for char in 'hello world':
#     print(f'char at {index} = {char}')
#     index +=1


string_indices  =enumerate('hello world')  # enumerate object
print(string_indices)

for char , index in string_indices:
    print(index, char)




