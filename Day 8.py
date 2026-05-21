'''
*****elif
same as if but is used to check more conditions

#**********grading system
stu_marks=87
if stu_marks>=90:
    print("A+")
elif stu_marks>=80:
    print("A")
elif stu_marks>=70:
    print("B+")
elif stu_marks>=60:
    print("B")
elif stu_marks>=50:
    print("C+")
elif stu_marks>=35:
    print("pass")
else:
    print("fail")

#******program to find max number out of 3
num1=int(input())
num2=int(input())
num3=int(input())
if ((num1>num2)and(num1>num3)):
    print("num1 is bigger")
elif ((num2>num1)and(num2>num3)):
    print("num2 is bigger")
else:
    print("num3 is bigger")

*****nested if

if inside an if condition
*******atm pin progrm
SBI_bank={"atm_pin":"6600"}
pin=input("enter 4 digit atm pin:")
if len(pin)==4:
    if pin in SBI_bank['atm_pin']:
        print("welcome to sbi")
    else:
        print("invalid pin")
else:
    print("enter 4 digit pin")


*****for statement
    used to iterate over a sequence
    only used on iterables like list string tuple

ex
any="python"
an=[1,2,3,4]
s0=(5,6,7,8)
for j in any:
    print(j) ------>here j is called a intial instance and is not required to be defined and anything can be used in its place like how why etc


******range
      is a inbuilt function used to generate numbers in a sequential manner
for i in range(1,100,2):
    print(i)

**********else in for
        once the iterations completed this else block will be execute

for i in range(1,100,2):
    print(i)
else:
    print("iterations complrted")

***break statement
  used to exit from the loop based on condition(or if the condition is met)

for i in range(1,10):
    if i == 5:

        break
    print(i)

*****continue
used to skip the loop if the condition is met

for i in range(1,10):
    if i == 5:
        continue
    print(i)

******pass

for i in range(1,10):
    if i == 5:
        pass
    print(i)

*******while
      while is a combination of for and if
      the loop runs untill the condition is met

i=0
while i<5:
    print(i)
    i+=1
'''

  
        



