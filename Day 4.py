'''
concatination
-----------
------> (+) will only add the integers but for the other datatypes it will concatinate the given item
a=12
b=2
print(a+b)------>op will be 14
'''
'''
any="python"
is="is a language"
print(any+is)------->op will bw python is a language


'''
'''
  1.TUPLE
   collection of different datatypes seperated by commas,represented in()
   it is immutable
   as it is immutable.it has no other methods except indexing and count
'''
'''
index()
this used to give or find out index position of a item,and only gives the first occurance
some=(1,"python",[1,2],(3,4),"python")
print(some.index("python"))

count()
*this used to count the no of occurances
variable_name.count(item)
print(some.count("python"))
'''
'''
example for indexing in tuple
any=(1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4])
print(any.index[2][2][) to be done later

  2.DICTIONARY
  dict is a key : value pair, key and value is separated by : and the pair is separated by ,(comma) 
  represented by {}

my_details={"name":saranya,1:2,3:[2,4]}
print(type(my_details))


    **methods:
    
    1.keys()
    returns all keys from the dict
    syntax------>dict.keys()
    ex ----> my_details={"name":saranya,1:2,3:[2,4]} 


    2.values()
    returns all values from the dict
    syntax-------->dict.values()

    3.items()
     used to get key and values together
     output will be given like key and value seperated by comma in atuple sep by, in a list in a tuple
'''
'''
# to access value using key
my_details={"name":"saranya",1:2,3:[2,4]}
print(my_details["name"])

    4.update()
     used to add a new key:value pair into dict
     
'''
'''
my_details={"name":"saranya",1:2,3:[2,4]}
my_details.update({"age":25})
print(my_details)

#to update old key and can also add new key
my_details["aadhar"]="123456"
print(my_details)
'''
'''
     5.clear()
     used to remove all the items from the dict
     return empty dict
'''



     

