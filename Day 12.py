'''
---->inbuilt methods:
     print()
     input()
     len()
     type()
     max()
     min()
     sort()  --->(permanently sorts the list)
     sorted() ---->(sorts only during runtime)

m=[1,5,8,3,2]
print(sorted(m))
print(m) #here it prints unordered list only
m.sort()
print(m) #prints ordered only

----->RECURSIVE FUNCTION
     - a recursive function that calls itself to solve a problem by breaking it into small or simple sub problems
#### factorial
def fac(num):
    if num==1:
        return 1
    return num * fac(num-1)
print(fac(4))


---->return
     this ends a functions execution and sends a value back to the code that called the function

    eg:
    def add(a,b):
        return a+b #this only send the value down to where the function is called by assigning it to a different variable we can only print it
    res=add(4,5)
    print(res)

----->lambda function
     a lambda is a small anonymus function
     (n arguments but single expression it will throw an error if it has more errors)
     
     so= lambda a,b,c: a+b+c+a
     print(so(3,4,5))
'''
diff=lambda a,b,c:(b**c)**b
print(diff(1,2,3))
