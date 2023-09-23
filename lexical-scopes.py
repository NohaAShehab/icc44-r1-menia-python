"""

    how the variable is represented in the memory ?

"""
""" any variable defined in the python script --> module --> variable with global scope """
course = 'python'  # global scope

# print(course)

"""  local scope """


# any variable defined inside the function --> has local scope  --> can be accessed only inside the function
def formatname():
    name = input('please enter name : ')  # local variable
    name = name.strip().capitalize()
    print(name)


# formatname()
# # print(name)


""" access global variable from inside the function"""
""" you cann access global variable from inside the function"""
course = 'python'


def printCourse():
    print(f"course = {course}")


""" modify global variable"""


def modifycourse():
    global course
    course = input("please enter coursename: ")
    print(f"after update {course}")


#
# modifycourse()
# print(f"after modify {course}")


# for i in range(10):
#     pass
#
# #
# print(i)
# name = 'Ahmed'
# while True:
#     name = 'Ali'
#     break
#
#
# print(name)
# # name = 'noha'

# name = 'ali'
# if name =='ahmed':
#     grade = 10
# else:
#     pass
#
#
# print(grade)

##### function inside a function

def outerfun():
    course = 'python'  # local scope

    def formatCourse():
        # # you can access local variable from inner function
        print(course.upper())

    formatCourse()

    def modifyCourse1():
        course = input('please enter course: ')  # new local variable for the inner function
        print(course)

    # modifyCourse1()

    def modifyCourse():
        nonlocal course
        course = input('please enter course: ')  # new local variable for the inner function
        print(course)

    modifyCourse()
    print(f'course= {course}')


outerfun()
