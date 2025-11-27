class Account:
    def __init__(self, account_id, owner, balance=0):
        self._account_id = account_id
        self._owner = owner
        self._balance = max(0, balance) # добавлена защита от отрицательного баланса
    
    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"Account {self._account_id}: {self._owner}, Balance: ${self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
