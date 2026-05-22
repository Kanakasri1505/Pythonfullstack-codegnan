''''
*******nested loops

for i in range(1,10):
    for j in range(1,2):
        print(i)
        print(j)

        
******to print 9 table
num=9
for i in range(1,11):
    print(f"{num} x {i} = {i*num}")

***to reverse a string(instead of[::-1]

so=input("enter a word:")
empty_str=""
for j in so:
    empty_str=j + empty_str
    print(empty_str)

*****palindrome

so=input("enter a word:")
empty_str=""
for j in so:
    empty_str=j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")


******amstrong number(ex 153 1 cube+5 cube+3 cube=153)

num=int(input())
amstro=0
length=len(str(num))
for i in str(num):
    amstro+=int(i)**length
if amstro==num:
    print("amstrong")
else:
    print("not amstrong")

*****perfect number(ex 28 factors 1 2 4 7 14 their sum=28)

num=int(input())
per_num=0
for j in range(1,num):
    if num%j==0:
        per_num+=j
if per_num==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

*****prime number

num=int(input())
count=0
for i in range(1,num+1):
    if num % i==0:
        count+=1
if count==2:
    print("num is a prime")
else:
    print("num is not prime")

*********patterns

1.*
  **
  ***
  ****
  *****


star=5
for i in range(1,star+1):
    for j in range(1,i+1):
        print("*",end="")   ------->(end prints the star in smae line instead of next line)
    print()    ---->(here print is empty cause im pprinting star immediately after the loopd ends or all the stars will be in same line)


2.A
  A B
  A B C
  A B C D
  A B C D E



star=5
char=64
for i in range(1,star+1):
    for j in range(1,i+1):
        print(char(64 +j),end=" ")

    print()


3.1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5

star=5
count=0
for i in range(1,star+1):
    for j in range(1,i+1):
        count =+1
        print(j,end=" ")
    print()

4.*****
  ****
  ***
  **
  *

star=5
for i in range(star,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

5.  *
   * *
  * * *
 * * * *
* * * * *
'''



        
