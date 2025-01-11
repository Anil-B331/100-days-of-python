class account:
    def __init__(self,acc,balance):
        self.acc_num= acc 
        self.balance= balance

    def credit(self,amt):
        self.balance +=amt
        print(f"Balance after credit is: {self.balance}")

    def debit(self,amt):
        self.balance -= amt
        print(f"Balance after debit is: {self.balance}")

    def show(self):
        print(f"Account {self.acc_num} has balance of RS: {self.balance}")

a1=account(3455001,25000000)
a1.credit(250)
a1.debit(125)
a1.show()