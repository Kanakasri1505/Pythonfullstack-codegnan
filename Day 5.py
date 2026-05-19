'''

    1.SETS
      -a set is a collection of unique and unordered elements
      -duplicate values are not allowed
      -items are not stored in index order
      -{}
      -set always gives in ascending order
      -set is mutable
'''
'''
ex
any={1,2,2,3,4}
print(any)  #op {1,2,3,4}

      methods
      1.union()
       it will give all the values from 2 sets together in once
       syntax----->variable_name.union(another variable)
       
    '''
'''
any={1,2,2,3,4}
an={70,69}
print(any | an)
print(any.union(an))
'''
'''
      2.intersection
      to get the common elements from both the sets
      syntax----->variable_name.intersection(another variable)
      '''
'''
any={1,2,2,3,4}
an = {2,69}
print(any & an)
print(any.intersection(an))
'''
'''
     3.difference
     to get different values from the set
     syntax------>variable_name.difference(another var)
'''
'''
any={1,2,2,3,4}
an = {3,26,89}
print(any - an)
print(any.difference(an))
      #symmetric difference
 '''
'''
any={1,2,2,3,4}
an = {3,26,89}
print(any ^ an)
print(any.symmetric_difference(an))

   *** add()
   to add new elements into set--------->only 1 element
   syntax---->variable_name.add(element)
''''''
any={1,2,2,3,4}
any.add(41)
print(any)
''''''
   ****update()
   to add multiple elements into set
   syntax---->variable_name.update(element)

'''
any={1,2,2,3,4}
any.update([41,58,98])
print(any)
'''
'''
'''

     *****remove()
      ***it will remove the element from the set but it will throw an error(key error) if element not in set
      syntax----->variable_name.remove(element)

      ****discard()
      ***it will remove the element from the set but it will  not throw an error even  if element not in set
      syntax----->variable_name.discard(element)
      '''
   
      
