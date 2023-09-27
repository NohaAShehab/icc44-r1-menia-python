



""" special method """

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # proptected
#         self.sal = salary
#
#     def __str__(self):
#         # must return with string
#         return f"{self.name}"
#
#     def __repr__(self):
#         return f"Employee(name={self.name}, _email={self._email}, salary={self.sal})"
#
#     def __len__(self):
#         # must return with number -integer-
#         return len(self.__dict__)
#
#     def __call__(self, *args, **kwargs):
#         print("--------------------------------")
#
#         # raise Exception('This is an object from the class , please donnot call it' )
#
#
# emp = Employee("ahmed", 'a@gmail.com', 78651278389)
# print(emp)  # python check if class contains __str__ or not __repr__


# l = [4,5,5,44]
# print(len(l))
#
# print(len(emp))
#

# emp()


#################################################################


class Employee:
    __slots__ = ['name', '_email', 'sal']
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email  # proptected
        self.sal = salary

    def __str__(self):
        # must return with string
        return f"{self.name}"

    def __repr__(self):
        return f"Employee(name={self.name}, _email={self._email}, salary={self.sal})"

    def __len__(self):
        # must return with number -integer-
        return 3

    def __call__(self, *args, **kwargs):
        print("--------------------------------")

        # raise Exception('This is an object from the class , please donnot call it' )


emp = Employee("ahmed", 'a@gmail.com', 78651278389)

# emp.country = 'Egypt'

# Employee.__slots__ = ['country']
# emp.country = 'Egypt'

Employee.country = 'Egypt'

print(emp.__repr__())

print(emp.__dict__) # runtime error















