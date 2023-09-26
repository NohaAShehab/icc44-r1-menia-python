""" employees """
#
#
# emp = {
#     "name" :"Ahmed",
#     "id" :1,
#     "track" :"python"
# }
#
# emp2= {
#     "emp_id": 10,
#     'emp_name' :'mohamed',
#     'track': 'python'
# }


""" Classes   """

# new datatype --> object factory ---> create classes


# class Employee:
#     pass


"2- create object from class"
# emp = Employee()
# print(emp)
#
# if emp:
#     print('hi')
# else:
#     print('bye')

"3- populate object with data"
# emp.name = 'Ahmed'
# emp.salary =1000
# emp.email = 'ahmed@gmail.com'
#
# emp2 = Employee()
# emp2.fname = 'Ali'
# emp2.lname = 'Mohamed'
# emp2.emp_id = 10
# emp2.emp_salary = 10000
# print(isinstance(emp, Employee))
# print(isinstance(emp2, Employee))

"4- customize object creation "

""" constructor , init method """

# class Employee:
#     def __init__(self):
#         """ when you create new object --> constructor  function --> preserve new address in memory
#             to save the object content in
#         """
#         print(f'--- object creation --- {self}')
#         self.name ='ahmed'
#         self.id =10
#         self.salary = 10000
#
#
# emp1 = Employee()
# print(emp1)
# emp2 = Employee()
# print(emp2)
#
#
#

# class Employee:
#     def __init__(self, name, id, salary):
#         """ when you create new object --> constructor  function --> preserve new address in memory
#             to save the object content in
#         """
#         print(f'--- object creation --- {self}')
#         """ name and id and salary --> instance variables """
#         self.name =name
#         self.id =id
#         self.salary = salary
#
#     # def __init__(abbass):
#     #     """
#     #     any function created inside python class --> python consider the first argument in the  function
#     #     represent the self =object reference / address =
#     #     """
#     #     print(f'--- object creation  {abbass}--- ')
#
# #
# emp1 = Employee("ahmed", 10, 2000)
# print(emp1)
# emp2 = Employee("ali", 22,2222)
# print(emp2)
# print(emp1.name)
#


"""class contain data and functionality  

    object wrap data and function into one container 
"""

# class Employee:
#     def __init__(self, name, id, salary):
#         self.name =name
#         self.id =id
#         self.salary = salary
#
#     """ printEmployee is instance method  --> behaviour depends on the caller instance/object"""
#     def printEmployee(self):
#         print(f"My name is {self.name}")
#
#
# #
# emp1 = Employee("ahmed", 10, 2000)
# print(emp1)
# emp1.printEmployee()
# emp2 = Employee("ali", 22,2222)
# print(emp2)
# # print(emp1.name)
# emp2.printEmployee()

""" define properties  related to the class not the object """
"""count = 0
class Employee:
    def __init__(self, name, id, salary):
        self.name =name
        self.id =id
        self.salary = salary
        global  count
        count +=1

    def printEmployee(self):
        print(f"My name is {self.name}")


#
emp1 = Employee("ahmed", 10, 2000)
print(emp1)
emp1.printEmployee()
emp2 = Employee("ali", 22,2222)
print(emp2)
# print(emp1.name)
emp2.printEmployee()
print(count)"""

# class Employee:
#     count = 0  # class variable --> represent shared property related to the class not the instance
#
#     def __init__(self, name, id, salary):
#         """ instance variables """
#         self.name = name
#         self.id = id
#         self.salary = salary
#         # self.__class__.count += 1
#         # print(self.__class__.count)
#         Employee.count +=1
#         print(Employee.count)
#
#
#
#     def printEmployee(self):
#         print(f"My name is {self.name}")
#
#
# #
# emp1 = Employee("ahmed", 10, 2000)
# emp2 = Employee("ali", 22, 2222)
# emp3 = Employee("bob", 33,33333)
#
# """ access class variable  using class name """
# print(f"total no of employees = {Employee.count}")
#
# emp3.count = 10 # create new instance variable for emp3 object --> value=10


"""class methods """

# class Employee:
#     count = 0  # class variable --> represent shared property related to the class not the instance
#     country = 'Egypt'
#
#     def __init__(self, name='', id=1, salary=1,days = [],*args):
#         """ instance variables """
#         self.name = name
#         self.id = id
#         self.salary = salary
#         # self.__class__.count += 1
#         # print(self.__class__.count)
#         self.projects = args
#         Employee.count += 1
#         print(Employee.count)
#         self.days = days
#
#     def printEmployee(self):
#         print(f"My name is {self.name}")
#
#     # ask user to modify country
#     @classmethod
#     def modifyCountry(cls):
#         print(cls)
#         Employee.country = input('please enter country name: ')
#
#     # class method is considered as object factory
#     @classmethod  #
#     def create_default_object(cls):
#         return  cls('test', 1, 10000)

# django --->

#

# Employee.modifyCountry()
# Employee.country = input('please enter country name: ')

# emp = Employee("ahmed", 10, 2000, 'django', 'mysql', 'odoo')
# """ I need to create another constructor for the class """
# emp3= Employee()
#
# emp4 = Employee.create_default_object()


""" ----> check this """


# class Employee:
#     count = 0  # class variable --> represent shared property related to the class not the instance
#
#     def __init__(self, name='', id=1, salary=1):
#         """ instance variables """
#         self.name = name
#         self.id = id
#         self.salary = salary
#         Employee.count += 1
#
#     def printEmployee(self):
#         print(f"My name is {self.name}")
#
#     # class method is considered as object factory
#     @classmethod  #
#     def create_default_object(cls):
#         return cls('test', 1, 10000)
#
#     @staticmethod
#     def calNetSal(salary):
#         return salary * 0.8
#
#
#
# emp1 = Employee('ahmed', 10, 10000)
#
# "how to use static methods ? "
# print(Employee.calNetSal(emp1.salary))
# print(emp1.calNetSal(1000000))
# # def calNetSal(salary):
# #     return salary * 0.8
#
#
# # print(calNetSal(emp1.salary))
# #
# # print(calNetSal(200000))



""" --------------"""

class Employee:
    count = 0  # class variable --> represent shared property related to the class not the instance
    instances = []

    def __init__(self, name='', id=1, salary=1):
        """ instance variables """
        self.name = name
        self.id = id
        self.salary = salary
        Employee.count += 1
        Employee.instances.append(self.__dict__)

    def printEmployee(self):
        print(f"My name is {self.name}")

    # class method is considered as object factory
    @classmethod  #
    def create_default_object(cls):
        return cls('test', 1, 10000)

    @staticmethod
    def calNetSal(salary):
        return salary * 0.8



emp1 = Employee('jjj', 10, 10000)
emp2 = Employee("ddd", 100, 100000)
#
# for obj in Employee.instances:
#     print(f"{obj.name}, {obj.id}")

# you to the save data in the object -->


"""magic property in python __dict__ """

print(emp1.__dict__)


for obj in Employee.instances:
    print(f"{obj['name']}, {obj['id']}")
