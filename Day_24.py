'''
   REGULAR EXPRESSIONS:(RegEx)
   
   -->RegEx is a sequence of characters that form a searching pattern...
   -->this can be used to check if a string contain the specified search pattern
   -->python has a built_in package called 're' which can be used to work with RegEx...

   functions in regular expressions:

   1.findall (returns if theres a match)
   2.search (gives the location of where the given )
   3.fullmatch (should be exact match of the string)

   Metacharacters:
   1. []-->a-z, A-Z,0-9 and any specified sequence
   
   
import re
any="c is a general purpose ,high level programming language"
print(re.findall('[a]',any))

any="c is a general purpose ,high level programming language"
print(re.search('[a]',any))

   2 . -->here each dot is 1 char

import re
any="c is a general purpose ,high level programming language"
print(re.findall('pr..r...i.g',any))

any="c is a general purpose ,high level programming language"
print(re.search('pr..r...i.g',any))

  3. ^ -->it looks whether the string is starting with specified sequence or not

import re
any="c is a general purpose ,high level programming language"
print(re.search('^c',any))

import re
any="c is a general purpose ,high level programming language"
print(re.findall('^c',any))

  4. $-->this checks whether a particular string ends with specified sequence or not

import re
any="c is a general purpose ,high level programming language"
print(re.search('age$',any))

import re
any="c is a general purpose ,high level programming language"
print(re.findall('age$',any))

  5.*--> 0 or more occurance
  
import re
any="c is a general purpose ,high level programming language"
print(re.findall('p*ogramming',any))

  6.?--> 0 or 1 occurance

import re
any="c is a general purpose ,high level programming language"
print(re.findall('p.?ogramming',any))

  7. +-->1 or more

import re
any="c is a general purpose ,high level programming language"
print(re.findall('p.+ogramming',any))

 8. {}-->returns upto specified length(SIZE)

import re
any="c is a general purpose ,high level programming language"
print(re.findall('l.{8}',any))


  special sequence:
  1.\s---> only spaces

import re
any="c is a general purpose ,high level programming language 23456"
print(re.findall('\s',any))
  
  2.\S-->no space
  
import re
any="c is a general purpose ,high level programming language 23456"
print(re.findall('\S',any))

  3.\D-->NO digits

import re
any="c is a general purpose ,high level programming language 23456"
print(re.findall('\D',any))


  4.\d-->only digits

import re
any="c is a general purpose ,high level programming language 23456"
print(re.findall('\d',any))

  5.\w-->matches any word char (letters,digits,underscore)
  
import re
any="c is a general purpose ,high level programming language -@23456"
print(re.findall('\w',any))


  6.\W-->returns non words

import re
any="c is a general purpose ,high level programming language -@23456"
print(re.findall('\W',any))

#### TO CHECK A MOBILE NUM  IS INDIAN OR NOT ###

'''
import re
mobno=input("enter mobile no")
so=re.fullmatch('[6-9][0-9]{9}',mobno)
if so:
    print(f"{mobno} is an indian no")
else:
    print(f"{mobno} is not an indian no") 
