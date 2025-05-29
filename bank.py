class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount


    def get_balance(self):
        return self.__balance

MENU = {
    '1.': 'Пополнить депозит',
    '2.': 'Снять депозит',
    '3.': 'Посмотреть баланс',
    '0.': 'Выход'
}

def main():
    my_account = BankAccount(100)

    while True:
        for key, value in MENU.items():
            print(f'{key} {value}')

        user_input = input('\nВведите номер для управления меню: ')

        if user_input == "1":
            amount = int(input('Введите сумму пополнения: '))
            my_account.deposit(amount)
        elif user_input == "2":
            amount = int(input('Введите сумму снятия: '))
            my_account.withdraw(amount)
        elif user_input == "3":
            print(f'На вашем депозите: {my_account.get_balance()}')
        elif user_input == "0":
            break
        else:
            print('Такого пункта меню нет.')

main()