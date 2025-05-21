class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance
    def get_balance(self):
        return self.__balance

account1 = BankAccount("Bob", 100)
print(f"Name: {account1.name}, Balance: {account1.get_balance()}")
print(f"Name: {account1.name}, Balance: {account1.withdraw(100)}")
account2 = BankAccount("Bobr", 1000)
print(f"Name: {account2.name}, Balance: {account2.get_balance()}")
print(f"Name: {account2.name}, Balance: {account2.deposit(500)}")