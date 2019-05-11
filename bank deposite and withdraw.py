class Account:
    
    def __init__(self,balance=0):
        self.balance = balance
        print("Wlcome To Axis Bank!!!!")
        print("Here is the details of Bank Accout!!!!")

    def deposite(self):
        amt = float(input("Enter the amount to be deposited:"))
        self.balance += amt
        print("\n Thank you!!, anount deposited:",amt)

    def withdraw(self):
        amt = float(input("Enter the amount to be withdraw:"))
        if self.balance >= amt:
            self.balance -= amt
            print("\n Withdrawl amount is",amt)
        else:
            print("\n Insuffcuent balance")

    def display(self):
        print("\n Net Balance available is =", self.balance)
        if self.balance >= 1000:
            print("Withdrawl limit upto 1000")
        else:
            print("Exceeds limit")

if __name__ == '__main__':
    a = Account()
    a.deposite()
    print(a)
    a.withdraw()
    print(a)
    a.display()
    print(a)
    #print(a.deposite())
    #print(a.withdraw())
    #print(a.display())
    

