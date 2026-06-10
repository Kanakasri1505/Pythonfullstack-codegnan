'''
  ### ERROR HANDLING :
    NOTE:
    only errors that are not in programming rules(like syntax indentation) can be handled
    
    1.try block:
    the try block test a block of code for error(if it has a error or not)

    2.except block:
    the except block handles  if the try block contains error
ex
try:
    print(10/0)

except:
    print("error")

    3.else block:
    it is executed only when there is no error in try block code

try:
    print("any")

except:
    print("error")
else:
    print("hi")  #any and hi are printed


 if i mention particular error in except block it will only handle that particular error

try:
    print(10/0)

except NameError:
    print("error")
else:
    print("hi")  

note:
it will only handle the error in the flow of try block and not on the except block(if in the except block specific error is mentioned)

try:
    print("a"+5)
    print(a)

except NameError:  #here only type error is executed 
    print("error")

except TypeError:
    print("yo")

else:
    print("hi")


    4.finally block:
    it will be executed regardless of whether the code in try block has error or not
'''
try:
    print("hey")

except :
    print("error")
else:
    print("ho")

finally:
    print("hi")
