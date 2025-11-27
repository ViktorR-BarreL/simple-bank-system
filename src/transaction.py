class Transaction:
    def __init__(self, transaction_id, account_id, amount, type, timestamp):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.type = type  # 'deposit' or 'withdraw'
        self.timestamp = timestamp
    
    def display_info(self):
        return f"T{self.transaction_id}: {self.type} ${self.amount} to Acc{self.account_id}"
