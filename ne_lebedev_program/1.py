class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        """Возвращает баланс счета."""
        return self.__balance

    def deposit(self, amount):
        """Увеличивает баланс на указанную сумму."""
        if amount < 0:
            raise ValueError("Сумма для пополнения должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount):
        """Уменьшает баланс на указанную сумму."""
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств")
        self.__balance -= amount

    def transfer(self, account, amount):
        """Переводит указанную сумму на другой банковский счет."""
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств")
        self.__balance -= amount
        account.deposit(amount)


if __name__ == "__main__":
    account1 = BankAccount(100)
    account2 = BankAccount(50)

    print("Баланс первого счета = ", account1.get_balance())
    print("Баланс второго счета = ", account2.get_balance())

    account1.deposit(50)
    print("Баланс первого счета после пополнения = ", account1.get_balance())

    account1.withdraw(30)
    print("Баланс первого счета после снятия = ", account1.get_balance())

    account1.transfer(account2, 70)
    print("Баланс первого счета после перевода = ", account1.get_balance())
    print("Баланс второго счета после получения перевода = ", account2.get_balance())
