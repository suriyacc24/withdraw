class amount:
    def amount(self,a):
        a=10000
        print("Total amount:",a)
class withdraw(amount):
    def withdraw(self,b):
        if (b<=7000):
            print("Transaction successful")
        else:
            print("Insufficient balance")

class deposit(withdraw):
    def deposit(self,c):
        print("amount is successfully deposit in your account:",c)
class total(deposit):
    def total(self,a,c):
        print("your total total balance in your account: ",(a+c))


d=total()
d.withdraw(7000)
d.withdraw(15000)
d.amount(10000)
d.deposit(10000)
d.total(10000,10000)