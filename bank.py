class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance


    def deposit(self, amount):
        try:
            amount = int(amount)
            if amount > 0:
                self.__balance += amount
            else:
                print('Не верное значение!')
        except ValueError:
            print('Не верное значение!')

    def withdraw(self, amount):
        try:
            amount = int(amount)

            if 0 < amount <= self.__balance:
                self.__balance -= amount
            else:
                print('Не верное значение!')

        except ValueError:
            print('Не верное значение!')

    def get_balance(self):
        return self.__balance


def main():
    my_account = BankAccount(100)

    MENU = {
        '1.': 'Пополнить депозит',
        '2.': 'Снять депозит',
        '3.': 'Посмотреть баланс',
        '0.': 'Выход'
    }

    while True:
        for key, value in MENU.items():
            print(f'{key} {value}')

        user_input = input('\nВведите номер для управления меню: ')

        if user_input == "1":
            amount = input('Введите сумму пополнения: ')
            my_account.deposit(amount)
        elif user_input == "2":
            amount = input('Введите сумму снятия: ')
            my_account.withdraw(amount)
        elif user_input == "3":
            print(f'На вашем депозите: {my_account.get_balance()}')
        elif user_input == "0":
            break
        else:
            print('Такого пункта меню нет.')

main()