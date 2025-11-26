class Account:
    def __init__(self, account_id, owner, balance=0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def display_info(self):
        return f"Account {self.account_id}: {self.owner}, Balance: ${self.balance}"