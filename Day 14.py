'''
List Comprehension
--------------------
-->LC offers a shortest syntax when we want to create a new list from existing list
synatx--> vari_name = [expression loop condition]

old =[1,2,3,4,5]
new_ =[so for so in old]
print(new_)

old =[1,2,3,4,5]
new_ =[so for so in old_ if so%2==0]
print(new_)

old = [23,6,7,90,3,46]
new_ = [so if so%2!=0 else "even" for so in old]
print(new_)




Generators
-------------
-->Generators in python are a special type of iterable allows users to itterate over data effeciently without storing everything in memory...
--->They generate values lazily using yield keyword./ lazy evaluation

Why to use generators ?
--> Generators does not store the entire data set in a memory, but they generate values on the fly or runtime.
--> Avoiding the unnecessary storage of data speed up execution.
-->This is also used in pipelines
How it works?
-->It looks like normal function but uses the yield keyword instance instead of return .
-->When the function is called it doesnot execute immediately.instance instead it returns a generator object which can be itterated using loop or the next()function

Next():-

def simple_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

def any(num):
    for i in range(num):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))

def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))

def sqr(num):
    result =[]
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(5))

so = "Cybersecurity is the practice of protecting systems, networks, programs, and data from digital attacks. "
any = ' '
for j in so:
    if j not in "AEIOUaeiou":
        any += j
print(any)
'''










