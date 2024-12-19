l1=[1,4,9,16,25,36,49,64,81,100]
# l=len(l1)
x=int(input("Enter the number you want to search: "))
for l in l1:
    if(l==x):
        print("x found")
    else:
        print("x not found")

for i in range(2,20,2):
    print(i)


# practice questions 1 to 100
for i in range(1,101):
    print(i)

# 100 to 1
for i in range(100,0,-1):
    print(i)

# multiplication table of number n
n=int(input("enter number n : "))
for i in range(1,11):
    print(n * i)

#sum of first n number
n=int(input("enter n: "))
i=1
sum=0
while i<=n:
    sum +=i
    i=i+1
print("sum is: ",sum)