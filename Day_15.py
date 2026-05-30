'''
   MODULES
   a module in python is a file that contains python code such as
   -variables
   -functions
   -classes
   -statements

   two types of modules:
   -user defined
   -built in

   1. USER DEFINED:
   which are created by user

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

   2.BUILT_IN:
   which are downloaded along with when we download python

import math
print(math.sqrt(25))
print(math.factorial(10))
print(int(math.(2,5)))

 ###if i only wanna access only 1 function

from math import pow
print(pow(8,3))

 ###using alias name(importing a module using diff name)

import math as m
print(m.sqrt(49))

##### 1.os
      used to communicate with the system
      (creates a file folder)
      (deletes in file format only)

import os
##os.mkdir("demo.txt")
##os.rmdir("demo.txt")(removes file folder)
os.remove("deo.txt")(removes file)

      2.sys

import sys
print(sys.version)
print(sys.path)
print(sys.exit)

      3.random(generate random values)

import random
print(random.randint(1000,9999))
'''

     ####COLLECTIONS:
from collections import Counter,defaultdict
data=['a','b','c','d','e']
counter=Counter(data)
print(counter)

dd=defaultdict(int)
dd['missing']+=1
print(dd['missing'])
print(dd)


     
