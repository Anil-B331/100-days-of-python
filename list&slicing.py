#lists
#lists are mutable,i.e we can change the list elements for example:
# note: string is immutable


l1=["Anil",21,"csit","parasi"]
l2=[5,7,2,22,69,2,34]
print(l1)
l1[0]="Gyanu"
print(l1)
print(l1[3:len(l1)])
print(l1[-3:-1])
print(l1[1:])


#list methods
l1.append("good guy") #will add that appended value in the last of list
print(l1)
l2.sort() # sorting is ascending 
l2.sort(reverse=True) # sorting is descending
l1.sort() # sorting mixed list is not possible
l2.reverse() #reverse the given list
l2.insert(0,999)
l2.insert(3,868)
l2.remove(2) 
l2.pop(2)
print(l2)