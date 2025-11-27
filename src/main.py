from bank import Bank

def main():
    bank = Bank("My Bank")
    
    # Создание счетов
    acc1 = bank.create_account("Vktori", 1000)
    acc2 = bank.create_account("Anastasi", 500)
    
    # Операции
    acc1.deposit(200)
    acc1.withdraw(100)
    
    # Вывод информации
    print("All accounts:")
    for acc_info in bank.display_all_accounts():
        print(acc_info)

if __name__ == "__main__":
    main()
