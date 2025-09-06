

import random

class BankAccount:
    database = {}
    promo_code = 2_000

    def __init__(self, name, amount, isAdmin=False, hasPromo=False):
        if hasPromo:
            amount += BankAccount.promo_code
        self.account_name = name
        self.account_balance = amount
        self.account_number = random.randint(100, 900)
        self.isAdmin = isAdmin
        self.isFrozen = False

    def deposit(self, amount):
        if not self.isFrozen:
            if amount > 0:
                self.account_balance += amount
                print(f"CREDIT ALERT: {amount} deposited into your account. New balance: {self.account_balance}")
                return self.account_balance
            else:
                print(f"Invalid amount: {amount}")
        else:
            print(f"Account is frozen. Contact Customercare.")

    def withdrawal(self, amount):
        if not self.isFrozen:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"DEBIT ALERT: {amount} withdrawn from your account. New balance: {self.account_balance}")
                return self.account_balance
            else:
                print(f"Insufficient balance")
        else:
            print(f"Account is frozen. Contact Customercare.")

    def transfer(self, recipient_account, amount):
        if not self.isFrozen:
            if self.account_balance >= amount:
                self.account_balance -= amount
                recipient_account.account_balance += amount
                print(f"DEBIT ALERT: {amount} transferred to {recipient_account.account_name}\n New balance: {self.account_balance}")
                print(f"CREDIT ALERT: {amount} received from {self.account_name}.\nNew balance: {recipient_account.account_balance}")
                return self.account_balance
            else:
                print(f"Insufficient balance")
        else:
            print(f"Account frozen. Contact Customercare.")

    def freeze_account(self, account_to_freeze, admin):
        if admin.isAdmin:
            account_to_freeze.isFrozen = True
            print(f"Account {account_to_freeze.account_name} has been frozen.")
        else:
            print(f"Only admins can freeze accounts.")

    def unfreeze_account(self, account_to_unfreeze, admin):
        if admin.isAdmin:
            account_to_unfreeze.isFrozen = False
            print(f"Account {account_to_unfreeze.account_name} has been unfrozen.")
        else:
            print(f"Only admins can unfreeze accounts.")

    def check_balance(self):
        print(f"Your current balance is: {self.account_balance}")

admin = BankAccount("Admin", 0, isAdmin=True)
jil = BankAccount("Jil", 1000)
jc = BankAccount("JC", 2000)

jil.check_balance()
jil.deposit(500)
jil.withdrawal(200)
jil.transfer(jc, 300)

admin.freeze_account(jil, admin)
jil.deposit(1500)  

admin.unfreeze_account(jil, admin)
jil.deposit(500)

