class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance


    def deposit(self):
            amount = self.get_number()

            if amount > 0:
                self.__balance += amount
            else:
                print('Не верное значение!')

    def withdraw(self):
        try:
            amount = self.get_number()

            if 0 < amount <= self.__balance:
                self.__balance -= amount
            else:
                print('Не верное значение!')

        except ValueError:
            print('Не верное значение!')

    def get_balance(self):
        print(f'{self.__balance} Рублей на счету')

    def get_number(self):
        try:
            number = int(input('Введите сумму: '))
            return number
        except ValueError:
            print('Не верное значение!')

def main():
    my_program = True
    my_account = BankAccount(100)

    MENU = {
        '1': ('Пополнить депозит', my_account.deposit),
        '2': ('Снять депозит', my_account.withdraw),
        '3': ('Посмотреть баланс', my_account.get_balance),
    }

    while my_program:
        for key, (description, _) in MENU.items():
            print(f'{key}. {description}')

        user_input = input('\nВведите номер для управления меню: ')

        if user_input in MENU and not 0:
            _, action =  MENU[user_input]
            action()

main()