from account import Account

class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = []
        self._next_account_id = 1
    
    def create_account(self, owner, initial_balance=0):
        account = Account(self._next_account_id, owner, initial_balance)
        self._accounts.append(account)
        self._next_account_id += 1
        return account
    
    def find_account(self, account_id):
        for account in self._accounts:
            if account._account_id == account_id:
                return account
        return None
    
    def display_all_accounts(self):
        return [str(account) for account in self._accounts]