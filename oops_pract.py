class student:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    
    def avg(self):
        sum=0
        for mark in self.marks:
            sum +=mark
            avg = (sum)/3
        print(f"{self.name} has average mark of {avg:.2f}")
        
s1=student("anil",[98,97,92])
print(s1.avg())