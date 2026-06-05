'''
   1. INHERITENCE:
     this allows one class to acquire the properties and methods of another class

     -->types
     1. single inheritance
     2.multiple inheritance
     3.multilevel inheritance
     4.hierarchical inheritance
     5.hybrid inheritance

     ---------------------------------------------------
     1.SINGLE INHERITANCE:
      ->a class inherits from a single parent class
      
        PARENT
          |
          |
        CHILD

class father:
    def land(self):
        print("my father has 5 acres")
class siri(father):
    def my_own(self):
        print("i have 2 acres")  ##accesimg parent class method using child class
fam=siri()
fam.land()

     2.MULTIPLE INHERITANCE:
     ->a class inherits from multoiple parent classes
     
        | PARENT 1| |PARENT 2|
         --------     --------
                 |   |
                 |   |
                 |   |
                 |   |
                 CHILD

class father:
    def land(self):
        print("my father has 5 acres")
class mother:
    def gold(self):
        print("mother has 2 kg gold")
class me(father,mother):
    def my_own(self):
        print("i have nothing")
fam=me()
fam.land()
fam.gold()


      3.MULTI-LEVEL INHERITANCE:
      ->a class inherits from a parent class and another class inherits from the child class

          parent class
          ------------
               |
               |
               |
               |
         child class (parent to the next)
         ------------
               |
               |
               |
          child class



class grandfather:
    def land(self):
        print("my grandfather has 5 acres")
class father(grandfather):
    def gold(self):
        print("father has a flat")
class me(father):
    def my_own(self):
        print("i have both of their prop")
        
fam=me()
fam.land()
fam.gold()
fam.my_own()


     4.HIERARCHICAL INHERITANCE:
      multiple child classes inherit from single parent class

                 PARENT CLASS
                      |
                      |
                      |
                --------------
                |            |
                |            |
        CHILD CLASS 1     CHILD CLASS 2

        
class father:
    def land(self):
        print("my father has 10 acres")
class me(father):
    def gold(self):
        print("job")
class sis(father):
    def my_own(self):
        print("study")
        
mon=me()
mon.land()

inh=sis()
inh.land()


   5.HYBRID INHERITANCE:
     combination of two or more types of inheritance

class A:
    def some(self):
        print("class A")
class B(A):
    def any(self):
        print("class B")
class C(A):
    def so(self):
        print("class C")
class D(B,C):
    def say(self):
        print("class D")
kay=D()
kay.some()
kay.so()

    ##***SUPER() METHOD:
          super() is used to access methods and constructor of the parent class from the child class


class parent:
    def display(self):
        print("method parent")
class child(parent):
    def display(self):
        super().display()
        print("method child")
so=child()
so.display()
'''
class person:
    def __init__(self,name):
        self.name=name
class stu(person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno=rollno
    def display(self):
        print(f"name: {self.name}")
        print(f"roll no: {self.rollno}")
any=stu('siri',21)
any.display()
         

      
                
