"""

    inheritance :
        base -parent- class --> child inherits parents' properties and methods
    polymorphism:
        poly --> many
        morphism  --> forms

        ---> overloading
        ---> overriding
    abstraction:
        hide details --> general architecture
        class methods a, b,c -> without implementation

    encapsulation:
        object
        property decorator




"""


###################################################################
""" Encapsulation ----"""


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # proptected
#         self.__salary = salary  # private
#
#
#     def printEmployee(self):
#         print(f"name={self.name}, email= {self._email} ,salary= {self.__salary}")
#
# emp = Employee("noha", "noha@gmail.com", 100000)
# print(emp)
#
# print(emp.name)
# emp.name=  'Noha Shehab'
#
# print(emp._email)  #Ethically don't do this
# emp._email = 'n@gmail.com'
#
#
# "what about private ? "
# # print(emp.__salary)  #AttributeError: 'Employee' object has no attribute '__salary'
#
# print(emp._Employee__salary) #Ethically don't do this
#
#
# emp.__salary = 9999999999999999  # add new property __salary to the object in the runtime
#
# emp._Employee__country = 'Egypt'





""" why we use access modifiers """
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # proptected
#         self.__salary = salary  # private
#
#     def printEmployee(self):
#         print(f"name={self.name}, email= {self._email} ,salary= {self.__salary}")
#
#     def getSalary(self):
#         return self.__salary
#
#     def setSalary(self, salary):
#         if isinstance(salary,int) or isinstance(salary, float):
#             self.__salary = salary
#
#         else:
#             raise TypeError('Salary must be an integer or float ')
# emp = Employee("noha", "noha@gmail.com", 100000)
#
# emp.setSalary("100000")
#
# print(emp.getSalary())



'introduce property decorator '

#
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # proptected
#         self.__salary = salary  # private
#
#     def printEmployee(self):
#         print(f"name={self.name}, email= {self._email} ,salary= {self.__salary}")
#
#     @property
#     def salary(self):
#         return self.__salary
#
#
#
#     def setSalary(self, salary):
#         if isinstance(salary,int) or isinstance(salary, float):
#             self.__salary = salary
#
#         else:
#             raise TypeError('Salary must be an integer or float ')
# emp = Employee("noha", "noha@gmail.com", 100000)
#
# print(emp.salary)
# emp.salary = 4000000  #AttributeError: property 'salary' of 'Employee' object has no setter
#
# print(emp.__dict__)




""" you cannot set propery without getting the value """


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # proptected
#         self.__salary = salary  # private
#
#     def printEmployee(self):
#         print(f"name={self.name}, email= {self._email} ,salary= {self.__salary}")
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#
#         else:
#             raise TypeError('Salary must be an integer or float ')
#
#
# emp = Employee("noha", "noha@gmail.com", 100000)
#
# print(emp.salary)
# emp.salary = 1000000
#
# print(emp.__dict__)


""" check this """
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # proptected
#         # self.__salary = salary  # private
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#
#         else:
#             raise TypeError('Salary must be an integer or float ')
#
#     def printEmployee(self):
#         print(f"name={self.name}, email= {self._email} ,salary= {self.__salary}")
#
#     @property
#     def salary(self):
#         return self.__salary *.8
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#
#         else:
#             raise TypeError('Salary must be an integer or float ')
#
#
# emp = Employee("noha", "noha@gmail.com", "iti")
#
# print(emp)
# print(emp.salary)


""" Never repeat yourself"""

class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email  # proptected
        # self.__salary = salary  # private
        self.sal = salary  # call property setter in the initialization
        print(self.__dict__)

    def printEmployee(self):
        print(f"name={self.name}, email= {self._email} ,salary= {self.__salary}")

    @property
    def sal(self):
        return self.__salary *.8

    @sal.setter
    def sal(self, salary):
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary

        else:
            raise TypeError('Salary must be an integer or float ')


emp = Employee("noha", "noha@gmail.com", 1000)

print(emp)
print(emp.sal)
emp.sal = 34455

































