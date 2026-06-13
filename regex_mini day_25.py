'''
PROJECT BASED ON RegEx
----------------------
validation:
-----------
1.mobile number
10 digits in it

2.password
cap small digit special char atleast 8 length

3.mail
-->@gmail
-----------------------

###mobile validation
'''

import re

class validation:
    def __init__(self,mobile,password,email):
        self.mobile=mobile
        self.password=password
        self.email=email
    
        
    def mob(self):
        so=re.fullmatch('[6-9][0-9]{9}',self.mobile)
        if so:
            print("valid indian number")
        else:
            print(" invalid indian number")

    def password_(self):
         patt=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$"
         if re.fullmatch(patt,self.password):
            print("Valid Password")
         else:
            print("Invalid Password") 
        
    def mail(self):
        if re.fullmatch("^.+@gmail.com$",self.email):
            print("Valid Gmail")
        else:
            print("Invalid Gmail")

mobile=input("enter mobile no:")
password=input("enter password:")
email=input("enter email:")

val=validation(mobile,password,email)

val.mob()
val.password_()
val.mail()

