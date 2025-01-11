class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is {self.age}")

    def info(self):  #self is always written
        item = input("Enter item name: ")
        code = input("Enter item code: ")
        print(f"we have {item} with {code}")

# object of the Student class
s1 = Student("Anil", 22)
s1.info()
