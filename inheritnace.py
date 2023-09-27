# class Person:
#     pass
#
#
# class Employee(Person):
#     pass
#
#
# emp = Employee()
# print(isinstance(emp, Employee))
# print(isinstance(emp, Person))


"person --> constructor "
# class Person:
#     def __init__(self,name, age,salary):
#         self.name =name
#         self._age = age
#         self.__salary = salary
#
#
# class Employee(Person):
#     pass
#
#     def printEmployeeInfo(self):
#         print(f"{self.name}, {self._age}")
#
#
# emp = Employee("Ahmed", 10, 10000)
# emp.printEmployeeInfo()

""" add constructor  to the Employee class """
# class Person:
#     def __init__(self,name, age):
#         self.name =name
#         self._age = age
#
#     def printPerson(self):
#         print(f"Person : {self.name}, {self._age}")
# class Employee(Person):
#     def __init__(self,name,age,email, salary ):
#         # call parent constructor
#         super().__init__(name, age)
#         self.email = email
#         self.salary = salary
#
#     def printEmployeeInfo(self):
#         print(f"{self.name}, {self._age}, {self.salary}")
#
#
# emp = Employee("Ahmed", 10, 'ahmed@gmail.com', 3333333)
# emp.printEmployeeInfo()
# emp.printPerson()


"""overriding ? """
# class Person:
#     def __init__(self,name, age):
#         self.name =name
#         self._age = age
#
#     def printPerson(self):
#         print("---- I am a Person ----")
#         print(f"Person : {self.name}, {self._age}")
# class Employee(Person):
#     def __init__(self,name,age,email, salary ):
#         # call parent constructor
#         super().__init__(name, age)
#         self.email = email
#         self.salary = salary
#
#     # override
#     def printPerson(self):
#
#         super().printPerson()
#         print("--- I am an Employee ---")
#


#
# emp = Employee("Ahmed", 10, 'ahmed@gmail.com', 3333333)
# emp.printPerson()

""" multiple inheritance  """


# class Teacher():
#     pass
#
#
# class Engineer():
#     pass
#
#
# class Instructor(Teacher, Engineer):
#     pass
#
#
# python_in = Instructor()
# print(isinstance(python_in, Engineer))
# print(isinstance(python_in, Teacher))


""" case 1"""

# class Teacher():
#     def __init__(self, name):
#         self.name = name
#
# class Engineer():
#     pass
#
#
# class Instructor(Teacher, Engineer):
#     pass
#
#
# python_in = Instructor("noha")
# print(isinstance(python_in, Engineer))
# print(isinstance(python_in, Teacher))


""" case 2"""


# class Teacher():
#     pass
#
# class Engineer():
#     def __init__(self, sep):
#         self.sep = sep
#
#
# class Instructor(Teacher, Engineer):
#     pass
#
#
# python_in = Instructor("noha")
# print(isinstance(python_in, Engineer))
# print(isinstance(python_in, Teacher))



""" case 3"""
# class Teacher():
#     def __init__(self, name):
#         self.name =name
#
# class Engineer():
#     def __init__(self, sep):
#         self.sep = sep
#
#
# class Instructor(Teacher, Engineer):
#     pass
#
#
# python_in = Instructor("noha")


""" case 4 """
# class Teacher():
#     def __init__(self, name):
#         self.name =name
#
# class Engineer():
#     def __init__(self, sep):
#         self.sep = sep
#
#
# class Instructor(Teacher, Engineer):
#     def __init__(self,name ,course='python'):
#         super().__init__(name)
#         self.course =course
#
#
# python_in = Instructor("noha")


""" what about functions ? """
# class Teacher():
#     def __init__(self, name):
#         print("-- I am a teacher")
#         self.name =name
#         print("---------- teacher created -----------")
#     def printInfo(self):
#         print('I am a teacher')
#
#
# class Engineer():
#     def __init__(self, sep):
#         self.sep = sep
#         print("I am an engineer")
#         print("---------- engineer created -----------")
#
#     def printInfo(self):
#         print('I am an engineer')
#
#
# class Instructor(Teacher, Engineer):
#     def __init__(self,name ,course='python'):
#         super().__init__(name)
#         self.course =course
#
#
# python_in = Instructor("noha")
# python_in.printInfo()

""" -----"""

# class Test:
#     def __init__(self):
#         self.id = 100
# class Teacher():
#     def __init__(self, name):
#         print("-- I am a teacher")
#         self.name =name
#         print("---------- teacher created -----------")
#     def printInfo(self):
#         print('I am a teacher')
#
#
# class Engineer():
#     def __init__(self, sep):
#         self.sep = sep
#         print("I am an engineer")
#         print("---------- engineer created -----------")
#
#     def printInfo(self):
#         print('I am an engineer')
#
#
# class Instructor(Teacher, Engineer):
#     def __init__(self,name , sep, course='python'):
#         super().__init__(name)  # teacher
#         self.course =course
#         # super().__init__(sep)
#         Engineer.__init__(self, sep)
#         Test.__init__(self)  #not inheritance
#
#
# python_in = Instructor("noha", 'it')
# python_in.printInfo()
# print(isinstance(python_in, Test))

"""check this again """

# class Person:
#     def __init__(self, bdate):
#         self.bdate =bdate
#
#     def speak(self):
#         pass
#
#     pass
#
# class Teacher(Person):
#     def __init__(self, name):
#         # super().__init__()
#         print("-- I am a teacher")
#         self.name =name
#         print("---------- teacher created -----------")
#     def printInfo(self):
#         print('I am a teacher')
#
#
# class Engineer(Person):
#     def __init__(self, sep):
#         self.sep = sep
#         print("I am an engineer")
#         print("---------- engineer created -----------")
#
#     def printInfo(self):
#         print('I am an engineer')
#
#
# class Instructor(Teacher, Engineer):
#     def __init__(self,name , sep, bdate, course='python'):
#         super().__init__(name)  # teacher
#         # self.course =course
#         # # super().__init__(sep)
#
#         pass
#
#     def speak(self):
#         print(f"My name is {self.name}, {self.sep}")
#
# python_in = Instructor("noha", 'it', 99)
# # python_in.printInfo()

