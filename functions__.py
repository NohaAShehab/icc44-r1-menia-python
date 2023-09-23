
''' function block of code can do specific task
    write once use many

'''

#################3 functions with mandatory arguments ####################
'1- define a function '
def myfun():
    pass


'calling function '
# myfun()


'2- function arguments'
# def sumnum(num1, num2):
#     print(f"num1 ={num1}, num2= {num2}")
#
#
# sumnum(4,4)
# res = sumnum(10,330)
# print(res)

# def sumnum(num1, num2):
#     print(f"num1 ={num1}, num2= {num2}")
#     return
#
#
# sumnum(4,4)
# res = sumnum(10,330)
# print(res)

'function returns with result? '


# def sumnum(num1, num2):
#     print(f"num1 ={num1}, num2= {num2}")
#     res= num1 + num2
#     return res
#
#
# sumnum(4,4)
# res = sumnum(10,330)
# print(res)

'function return with mutiple values'

def sumnum(num1, num2):
    print(f"num1 ={num1}, num2= {num2}")
    res= num1 + num2
    return res, num1, num2  # return with tuple


# sumnum(4 ,4)
# res = sumnum(10 ,330)
# print(res)
#
# res2 =  sumnum(19 ,20 ,2220 ,2022)  # TypeError: sumnum() takes 2 positional arguments but 4 were given


############################# function with optional arguments

# def calculator(num1,num2, num3=10):
#     print(f'num1={num1}, num2={num2},num3={num3}')
#     res = num1+ num2 + num3
#     print(res)
#
# calculator(2,3,3)
# calculator(3,4)
#
# print('ahmed', 'mohamed', 'ali', sep='_##_', end='||')
# print('hello world')

################## check this

# def calculator(num1,num2, num3):
#     print(f'num1={num1}, num2={num2},num3={num3}')
#     res = num1+ num2 + num3
#     print(res)
#
# calculator(2,3,3)
#
# calculator('ahmed','noha', 'omar')
#
# calculator('ahmed','noha', 10) #TypeError: can only concatenate str (not "int") to str


###########
# def calculator(num1:int,num2:int, num3:int):  # type hints --> documentary purpose
#     print(f'num1={num1}, num2={num2},num3={num3}')
#     res = num1+ num2 + num3
#     print(res)
#
# calculator(2,3,3)
#
# calculator('ahmed','noha', 'omar')

# calculator('ahmed','noha', 10) #TypeError: can only concatenate str (not "int") to str


########################### validation

print(isinstance('noha', str))
print(isinstance('ahmed', int))

# def calculator(num1:int,num2:int, num3:int):  # type hints --> documentary purpose
#     if isinstance(num1, int) and isinstance(num2, int ) and isinstance(num3, int):
#         print(f'num1={num1}, num2={num2},num3={num3}')
#         res = num1+ num2 + num3
#         print(res)
#     else:
#         print('==== not valid arguments =====')
#
# calculator(2,3,3)
#
# calculator('ahmed','noha', 'omar')
# calculator('ahmed','noha', 10)

""" ----------------> """
# print('Ahmed', 'noha','dddd')
# print()
# print('444')


################
""" functions with unknown number of arguments """

# def askforstudents(*students):   # * --> zero or more
#     print(students)  #tuple?
#
#
# askforstudents('john', 'mina', 'mohamed')
#
# askforstudents()
#
# askforstudents('omar')

""" """
def introduceyourself(**info):
    print(info)  # dict


introduceyourself(name='noha', work='iti', salary='1000')
introduceyourself('john')
introduceyourself(fname='ahmed',lname='mohamed')









