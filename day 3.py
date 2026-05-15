'''
   1.program to convert 24hr clock into normal clock
    like 23:34 ------->11:34 , from 24 hrs clock the minutes are same we only need to change hours
    so if we do 23-12 its 11. now to take input we can only take it as a string then convert to
    integer and do the subtraction and then print it.
'''
'''
time =input("enter 24 hours time")  #for user input we can use input()
parts = time.split(":")
hour = int(parts[0])
min_ = int(parts[0])
print(f"{time} is converted into {hour - 12}:{min_} pm")
----------------------------------------------------------------


    2.LIST
      list is a collection of different datatypes
      it is represented in [] and separated by ,(commas)
      ex ---------> any=[1,python,[1,2]]
      it is mutable
'''
#indexing
any=[1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]
print(any[2][2][1][8]) #these is what required to get p from this is python 3rd class
'''


      METHODS:
      1.append()
      this method is used to add a new item into list and it will add in the last index position
      syntax ------->variable_name.append(item)
      we can only add only 1 item at a time like even if its a list only 1 at a time

      ex----->any=[1,2,3]
              any.append(6)------>op will be[1,2,3,6]

    ******in immuatable datatypes we can directly write print(variable_name.replace("string"))
    cause string is immutable that is u try to modify the original string using methods the original is stored and print prints the
    modified string however if u print the original angain it will display original string onlyy.

    when the same cannot be done to list as it is mutable any.append(6) if u keep this in a list it will return none*****

    

    2.extend()
     --->this method is used to add iterable into list,and it will add in the last index position, each value or substring is given each index
     in the list
     syntax-----> variable_name.extend(iterable)
     consider above expample if we do extend any.extend(6) we cannot give like this any.extend([4,6]) beacuse it only takes iterables
     output will be [1,2,3,4,6] if we do to a string "python" output will be [1,2,3,4,6,'p','y','t','h','o','n']

     

     3.pop()
      used to remove the item from the list,but will mention here index position in the pop method
      syntax---->variable_name.pop(index)
'''
any=[1,2,3]
any.pop(0)
print(any)#----->it will print [2,3]
'''
     4.remove()
      used to remove item from the list should mention the exact item to be removed
      syntax----->variable_name.remove(item)

