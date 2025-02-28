class Bank_account :
    def __init__(self, account_name, balance):
        self.__account_name = account_name
        self.__balance =balance

    def deposit(self, amount) :
        print("ra tanxis shemotana gsurt? ")
        amount = int(input())
        self.__balance += amount
        print(f"tanxis shetana shesrulebulia!  Balance: {self.__balance}")

    def withdraw(self,amount) :
        print("ra tanxis gamotana gsurt? ")
        self.__balance -= amount
        print(f"tanxis gamotana shesrulebulia!  balance: {self.__balance}")

p1 = Bank_account("Mamuka", 50)
p2 = Bank_account("Lana", 1450)

print("Sheiyvanet saxeli :")
name = input()
setattr(p1, "account_name" , name)
print("sheiyvanet tanxa")
balance = input()
setattr(p1, "balance" , balance)
print("sheiyvanet shesabamisi kodi romlis operaciac gsurt :")
print("1. tanxis shetana     2.tanxis gamnotana")
num = int(input())
if num == 1 :
    p1.deposit()
elif num == 2 :
    print("ra tanxis gamotana gsurt? ")
    amount = int(input())
    p1.withdraw(amount)

else :
    print("ERROR!")
