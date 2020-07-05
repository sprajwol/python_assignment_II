# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


class Customer:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.address = ''
        self.contact = ''
        self.account_number = ''
        self.balance = ''

    def get_customer_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.address)
        print(self.contact)
        print(self.account_number)

    def set_customer_info(self):
        self.first_name = input("Enter first name:")
        self.last_name = input("Enter second name:")
        self.address = input("Enter address:")
        self.contact = input("Enter contact number:")
        self.account_number = input("Enter account number:")

    def deposit(self, amount):
        print("Deposit success")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if (self.balance > amount):
            print("Withraw success")
            self.balance = self.balance - amount

    def checkbalance(self):
        print(f"Balance: {self.balance}")
