class ToDoList:
    def __init__(self):
        self.tasks = {}


    def add_task(self, task):
        self.tasks.update({task: "не выполнено"})


    def complete_task(self, task_number):
        try:
            keys = list(self.tasks.keys())

            if 0 <= task_number - 1 < len(keys):
                self.tasks[keys[task_number - 1]] = 'выполнено'
                print('Задача удалена')
        except IndexError:
            print('Такой задачи нет.\n')


    def remove_task(self, task_number):
        try:
            keys = list(self.tasks.keys())

            if 0 <= task_number - 1 < len(keys):
                self.tasks.pop(keys[task_number - 1])
                print('Задача отмечена как выполнена.\n')
        except IndexError:
            print('Такой задачи нет.')


    def ist_tasks(self):
        number = 1

        print('Список задач:')
        for key, value in self.tasks.items():
            print(f'{number}. {key} | статус: {value}')
            number += 1

        print()

MENU = {
    '1.': 'Добавить новую задачу',
    '2.': 'Отметить задачу как выполнено',
    '3.': 'Удалить задачу',
    '4.': 'Список всех задач',
    '0.': 'Выход'
}

def main():
    my_ToDoList = ToDoList()

    while True:
        for key, value in MENU.items():
            print(f'{key} {value}')

        user_input = input('\nВведите номер для управления меню: ')

        if user_input == "1":
            task = input('Введите задачу')
            my_ToDoList.add_task(task)
            print('Задача добавлена.')
        elif user_input == "2":
            my_ToDoList.ist_tasks()
            task_number = int(input('\nВведите номер задачи для выполнения: '))
            my_ToDoList.complete_task(task_number)
        elif user_input == "3":
            my_ToDoList.ist_tasks()
            task_number =int(input('\nВведите номер задачи для удаления: '))
            my_ToDoList.remove_task(task_number)
        elif user_input == "4":
            my_ToDoList.ist_tasks()
        elif user_input == "0":
            break
        else:
            print('Такого пункта в списке нет.')

main()