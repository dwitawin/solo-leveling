# create BankAccount Class
class BankAccount:
    '''This is BankAccount Class.
    Please insert your:
    - Account Number (str)
    - Balance (int)
    - Date of Opening (DD/MM/YYYY) (str)
    - Name (str)'''

    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} is successful. New balance: {self.balance}.")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} is successful. New balance: {self.balance}.")
        else:
            print("Insufficient funds--you broke a$$.")

    def check_balance(self):
        print(f"Your balance: {self.balance}")

#testing
if __name__ == "__main__":
    account = BankAccount("32165487609",69000,"21-01-2022","Dwita Alya")
    account.deposit(7500)
    account.withdrawal(2500)
    account.check_balance()