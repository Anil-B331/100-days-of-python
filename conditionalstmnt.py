"""
q=input("Enter the color of traffic light:")
if(q=="red"):
    print("Stop")
elif(q=="yellow"):
    print("Look")
elif(q=="yellow"):
    print("Go")
else:
    print("Light is broken") 
    """

""""
food=input("Food=") # The syntax is:  variable=value_1 if condition else value_2
eat="yes" if food=="masu bhaat" else"no"
print(eat)
"""

# food=input("Food=") # syntax: statement_1 if< condition> else statement_2
# print("Sweet") if food=="cake" or food=="halwa" else print("spicy")

#clever if (conditional statement) syntax: var=(false_val,true_val) [<condition>]
salary=float(input("Enter your salary:"))
tax=salary*(0.1,0.2) [salary>=50000]
print("Your tax is:",tax)