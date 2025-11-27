# UML Diagram - Bank System

## Диаграмма классов

![UML Diagram](RL9BQpCn3BpxLuWz9T_NXVQwK4XxxgszbM0KhvEO-h5O2kbI-j-x3plx83TBcf5cPEs8CVB5MNX5__NU4cidXB98D6JWHm2KuD7f2eZZ4A5IuUAPAdWpn9ylOxWVaVgRPG98KrTWFFU5KW3y1nKriixrJRXw7OU-3t10Yrxf2eus8CCpF6uhIAq7xj7u-iPSJLX1QqEDnLQYjPb1cs.png)

## Описание классов

### Класс Bank
- **Поля:**
  - `name: str` - название банка
  - `accounts: List[Account]` - список счетов
  - `next_account_id: int` - следующий ID для счета

- **Методы:**
  - `create_account(owner, balance)` - создание нового счета
  - `find_account(account_id)` - поиск счета по ID
  - `display_all_accounts()` - отображение всех счетов

### Класс Account
- **Поля:**
  - `_account_id: int` - идентификатор счета
  - `_owner: str` - владелец счета  
  - `_balance: float` - текущий баланс
  - `_transactions: List[str]` - история операций

- **Методы:**
  - `get_balance()` - получение баланса
  - `deposit(amount)` - пополнение счета
  - `withdraw(amount)` - снятие средств
  - `__str__()` - строковое представление

### Класс Transaction
- **Поля:**
  - `transaction_id: int` - ID транзакции
  - `account_id: int` - ID связанного счета
  - `amount: float` - сумма
  - `type: str` - тип ('deposit'/'withdraw')
  - `timestamp: str` - время операции
  - `description: str` - описание

- **Методы:**
  - `display_info()` - информация о транзакции
  - `get_description()` - получение описания
  - `_generate_description()` - генерация описания

## Связи между классами
- **Bank → Account:** Агрегация (1 ко многим)
- **Account → Transaction:** Композиция (1 ко многим)
