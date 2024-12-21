def sum(a,b):
    return a+b
print(sum(5,9))

#to print length of list
li=[2,3,5,6,7]
lii=["hello","world"]
def str_len(l1):
    L=print(len(l1))
    return L

str_len(li)
str_len(lii)

# to print element of list in single line
li=[2,3,5,6,7]
lii=["hello","world"]
def elemnts(l1):
    for i in l1:
        print(i)

elemnts(li)
elemnts(lii)

# factorial of n
def fact(n):
    i=1
    f=1
    while i<=n:
        f=f*i
        i +=1
    print(f)

fact(5)

# INR TO NRP
def convert(inr):
    npr=inr*1.6
    print(npr,"NRP")
convert(10.5)