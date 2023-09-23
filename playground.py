

'''

    modules and packages

    module ---> any .py file is a python module
    -- you can import module or part of it .

'''

# def askforInt(message):
#     while True:
#         num  = input(message)
#         if num.isdigit():
#             return int(num)
#
#         print('===please enter valid number ====')
#
# def askforsalary():
#     salary = askforInt('please enter your salary')
#     print(salary)
#
#
# askforsalary()


""" import module"""





# import  myinputsmodule
#
# def askforsalary():
#     salary = myinputsmodule.askforInt('please enter your salary')
#     print(salary)
#
#
# askforsalary()


""" alais module name: """
# import  myinputsmodule as mm
#
# def askforsalary():
#     salary = mm.askforInt('please enter your salary')
#     print(salary)
#
#
# askforsalary()
#
# print(mm.askforpurealphas('please enter firstname: '))


""" import part of the module ? """
from myinputsmodule import  askforpurealphas

# print(askforpurealphas('please enter name: '))


# from myinputsmodule import  num
# print(num)
#
# num = 100
#
#
#
# import  math
#
# print(math.pi)
#
# """ package ---> is a directory contains set of modules"""

""" import module from the package
    import packagename.modulename 
 """

# import  iti.greetingmodule
#
# iti.greetingmodule.sayhello('Ahmed')

# import  iti.greetingmodule as gt
#
# gt.sayhello('Ahmed')



""" import part of the module from package """

# from iti.greetingmodule import  sayhello
# sayhello('Ahmed')



###
# import  itp.mymodule



from itp import testnumber

print(testnumber(10))













