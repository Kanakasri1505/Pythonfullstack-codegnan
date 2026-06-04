'''
  ---->OOPS(obect oriented programming systems)
  1.class
   --->a class is a blueprint or a template used to create object
      to create a class use " class " keyword

      class stu:
          name="siri"
          
  2.object
    --> an object is an instance of a class
eg:
class stu:
    name='siri'

s1=stu()     #s1 is the object
print(s1.name)


 3.attributes:
 -->they are the variables that belongs to a class or an object

 class stu:
    name='siri'
    age=22

s1=stu()     #name and age are attributes of class stu or object s1
print(s1.name)
print(s2.age)

 4.methods:
  -->the functions defined inside the class is methods


class PFS_DA:
    def python(self):
        PFS_DA ='batch_03'
        print('this pfs and da batch03')
    def flask(self):
        PFS='batch03'
        print('this pfs batch03')
all_=PFS_DA()
all_.python()
all_.flask()

 4.constructor:
  -->a constructor is a special method that is automatically gets called when an object is created.
  -->every class consists of a constructer which helps to store and access the attributes in any method

class ATM:
    def __init__(self,balance,name):
        self.balance=balance
        self.name=name

    def check_balance(self):
        print(f"{self.name} your balance is {self.balance+700}")

    def name_(self):
        print(self.name)
card=ATM(balance=500000,name='siri')
card.check_balance()
card.name_()

 5.access specifiers:
  -->
  1.public
  -->this can be accessed from anywhere in the program

    class stu:
       name='siri'
    s1=stu()
    print(s1.name)
       
  2.protected
   -->this is represented using single _ (underscore)

    class stu:
       _name='siri'
    s1=stu()
    print(s1._name)
   
  3.private
  -->this is represented using double underscore __

   class stu:
       __name='siri'
    s1=stu()
    print(s1._stu__name)  (we'll omly call class in protected and attribute in private only when attribute is  directly in class)

  6.encapsulation:
   -->is the process of binding (holding) data and methods together
'''
class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def depo_(self,amount):
        self.__balance +=amount
    def get_bal(self):
        return self.__balance
acc=Bank(1000)
acc.depo_(100000)
print(acc.get_bal())
        

    
