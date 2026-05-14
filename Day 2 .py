'''
  1.OPERATORS:
   1. Arithmetic Operators
     +, -, *, /, //, %, **
     -----------------------
   2. Comparision Operators
     ==(*imp--->  looks for whether both values are equal or not) ,!=, >=, >=, < ,>
     -----------------------
   3. Assignment Operators
     =, += , -= ,*= ,/=
     ---------------------------
   4. Logical Operators
     and (both conditions must be true)
     or (any one condition should be satisfied)
     not (both conditions should be false)
     ---------------------------------
   5. Identity Operators
     is (*imp---> this operator looks for the object is same or not), is not
     --------------------------------------
   6. Membership Operators
     in
     not in
     -----------------------------------
   7. Bitwise Operators
     &, |, <<, >>
    ------------------------------
'''
'''
print(2*3)
print(5%4)
print(10**4)
print(105//6)
print(105/6)

count=1
for i in range(1,10):
    count *= i
print(count)
'''
'''
a=[1,2]
b=[1,2]
c=a
print(a==b)
print(b==c)
print(c is a)
print(a is not b)
print(id(a))
print(id(b))
'''
a=6
b=[1,4,5,7]
print(a in b)

'''
   2.Datatypes
    1.int (immutable cannot directly change the already assigned value in a variable i mean any operation
    cannot be done like if a and b are assigned once the value cannot be changed )
    --------------
    2. float
    
    3.STRINGS
     any data in between ' '," " is a string
     string is a sequence of characters that are enclosed in single double and triple quotes.
     string is immutable

     STRING METHODS:
      1.replace()
       used to replace with a new substring
       syntax------> variable_name.replace("old string","new string")
       ex----->
       any="python is a language"
       print(any.replace("python","java")  ------> it will print java is a language
       print(any) ------> it will print python is a language

       
      2.split()
        used to seperate the string into parts and it will split based on the substring where the part before substring
        is in one index and the part after is in another will be in another index.
        syntax-----> variable_name.split("substring")
        ex------> print(any.split("is"))  ------>it will print['python','a language']

        **len()(inbuilt function also used in list,tuple)
          get number of items
          syntax ------>len(variable_name)

      3.slicing()
        can give access to get particular index fron string.
        syntax---->variable_name[starting index:ending index]
        ex----->print(any[3:11] .------>it will give hon is a


      4.indexing
      used to get the substring in the index position specified
      syntax----->variable_name[index position]
      ex----->print(any(7)) ---->i
              print(any.index("ing")) ----->13


      
       
     
    
    
