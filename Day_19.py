'''
  1.POLYMORPHISM:
  this means "many forms" it allows the same function,method or operator to behave differently
  depending on the object.

    1.METHOD OVERLOADING
    2.METHOD OVERRIDING
    3.OPERATOR OVERLOADING

    1.METHOD OVERLOADING:
     method overloading means defining multiple methods with the same name but different parameter 
    

class calc:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
ans=calc()
print(ans.add(24,25))
print(ans.add(24,25,1))

             
    2. METHOD OVERRIDING:
     This occurs when a child class provide its own implementation of a
     method already defined in the parent class


class animal:
    def sound(self):
        print("animal sounds")
class dog(animal):
    def sound(self):   #if u want to access parent class method use super().sound().....(super() keyword)
        print("dog barks")
ntg=dog()
ntg.sound()


    3.OPERATOR OVERLOADING:
     this allows operators such as +.-,* etc to perform different actions for user-defined objects



class stu_:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks ** other.marks
    
so_1=stu_(4)
so=stu_(5)

print(so_1 + so)

 NOTE:
 The operator inside the method will overload a special method or operator given in the call


     2.ABSTRACTION:
     -> This is the process of hiding internal implementation details and showing only the essential features to the user
     -> it focuses on what an object does rather than how it is done
     


'''
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimeters(self):
        return 2*self.a*self.b
an=rec(10,5)
print(an.area())
    
     
    
