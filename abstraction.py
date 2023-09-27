


""" abstraction ---> depends on inheritance


    abstract class classname{
        abstract function ();

    }


    class test extends classname{
        function (){
        }
    }


"""

""" when you need to construct abstract classes ---> extend from ABC"""


from abc import ABC, abstractmethod


""" abstract class must contain at least one abstract method """
#
# class Shape(ABC):
#     def myfunc(self):
#         print('----')
#
#
#
#
# s = Shape()
# s.myfunc()


class Shape(ABC):
    @abstractmethod
    def calArea(self):
        pass


# s= Shape()


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width =width
        self.height =height

    def calArea(self):
        print(self.width* self.height)

r= Rectangle(3,3)

r.calArea()
print(isinstance(r,object))

l = [333]
l.append("ddd")











