'''
1. #Fibonacci:-
num = 0
num_2 = 1
def fibonacci(num,num_2):
    limit_ = int(input("Enter the limit:"))
    print(num,num_2,end=" ")
    for i in range(1,limit_):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3, end =" ")
fibonacci(num,num_2)

any = [2,5,7,9,2,7]
new_= []
def Dup(any,new_):
    for j in any:
        if j not in new_:
            new_.append(j)
    print(new_)
Dup(any,new_)
'''
count = 0
so ="News is information about current events. This may be provided through many different media: word of mouth, printing, postal systems, broadcasting."
def word_str(so,count):
    for j in so:
        count +=1
    print(count)
word_str(so,count)
