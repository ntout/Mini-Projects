# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won’t put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account


class Atm:
    def __init__(self):
        self.balance = 0
        self.interest = .1/100
        self.transaction = []

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.transaction.append('User deposited: ${}'.format(amount))
        return self.balance

    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.check_balance():
            self.balance -= amount
            self.transaction.append('User withdrew: ${}'.format(amount))
        else:
            print('Insufficient funds')
        return self.balance

    def calc_interest(self):
        interest = self.balance * self.interest
        return interest

    def print_transaction(self):
        for i in self.transaction:
            print(i)
        return

    def run_atm(self):
        while True:
            user = input('What would you like to do (deposit, withdraw, check balance, history)?\n')
            if user == 'deposit':
                amt = input('How much would you like to deposit?: ')
                self.deposit(int(amt))
            elif user == 'withdraw':
                amt = input('How much would you like to withdraw?: ')
                self.withdraw(int(amt))
            elif user == 'check balance':
                self.check_balance()
            elif user == 'history':
                self.print_transaction()
            done = input('Perform another action? (y/n): ')
            if done == 'n':
                break
        print('Have a great day.')


nate = Atm()
nate.run_atm()

