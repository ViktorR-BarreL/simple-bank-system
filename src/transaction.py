class Transaction:
    def __init__(self, transaction_id, account_id, amount, type, timestamp):

        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        
        # Проверка допустимых типов транзакций
        valid_types = ['deposit', 'withdraw']
        if type not in valid_types:
            raise ValueError(f"Недопустимый тип транзакции: '{type}'. Допустимые значения: {valid_types}")
        self.type = type
        
        self.timestamp = timestamp
        
        # Автогенерация описания
        self.description = self._generate_description()
    
    def _generate_description(self):
        if self.type == 'deposit':
            return f"Пополнение счета на ${self.amount}"
        else:
            return f"Снятие средств со счета ${self.amount}"
    
    def display_info(self):
        return f"Транзакция #{self.transaction_id}: {self.description} (Счет: #{self.account_id})"
    
    def get_description(self):
        return self.description
    
    def __str__(self):
        return self.display_info()
