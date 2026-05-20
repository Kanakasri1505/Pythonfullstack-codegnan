
'''
STATEMENTS
 1.conditional statements
 2.control statements
 3.loops

 *****conditional statements
     1. if
     2. elif
     3. nested if

      if:
      only if the condition/staement is true itll go into the if and then execute the lines inside
      num = 5
      if num % 2 == 0:
          print("even")

      if-else
      else in the if statement,incase the condition is false then it will enter into fall back statement (else)
      itll execute whatever is present inside it

      um = 5
      if num % 2 == 0:
          print(f"{num} is even")

      else:
          print(f"{num} is odd")


###############max no between 2
num_1 = 5
num_2 = 4
if num_1 >= num_2:
    print(f"{num_1} is greater than {num_2} ")

else:
    print(f"{num_2} is greater than {num_1}")

*********eligibilty to vote
age = 5
if num >= 18:
    print(" eligible to vote")

else:
    print(f"u should wait for {18 - age} years more")

*******to find leap year

year =2024
if(year %4==0 and year %100!=0) or year % 400 ==0:
    print(f"{year}is a leap year")
else:
    print(f"{year} is not a leap year")


*************to check vowel
vowel="A"
if vowel in "AEIOUaeiou":
    print(f"{vowel}is a vowel)
else:
    print(f"{vowel}is a consonant")


*********to check a number is positive or neg no
num= 5
if num >= 0:
    print(f" {num}is positive")

else:
    print(f"{num} is negative")


********pass or fail
marks= int(input("enter ur marks"))
student_name=input("enter ur name")
if marks >= 45:
    print(f" {student_name} passed")

else:
    print(f"{student_name} failed")


*****divisibility checking
num=75
if num% 3==0 and num% 5 ==0:
    print(f" {num}is divisible by 3 and 5")

else:
    print(f"{num} is not divisible ")

******traffic signal
'''
signal=int(input("enter 1.green \n 2.red"))
if signal==1:
    print("go")
else:
    print("stop")










          
      
