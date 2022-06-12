class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount 
        else:
            print("insufficient funds")
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance +(self.balance * self.int_rate)
        return self
    


Account1 = BankAccount(.01, 0)
Account2 = BankAccount(.01, 0)

Account1.deposit(10).deposit(20).deposit(30).withdrawal(20).yield_interest().display_account_info()
Account2.deposit(100).deposit(50).withdrawal(5).withdrawal(10).withdrawal(5).withdrawal(10).yield_interest().display_account_info()
