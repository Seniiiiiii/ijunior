import json

class TaskManager:
    def __init__(self):
        self.tasks = [
            {"описание": "Первая задача", "статус": False},
            {"описание": "Вторая задача", "статус": False}
        ]

    def add_task(self, description: str):
        self.tasks.append({"описание": description, "статус": False})

    def complete_task(self, index: int):
        if index <= len(self.tasks):
            if self.tasks[index]:
                self.tasks[index]['статус'] = True
        else:
            print('такого в индекса нет')

    def remove_task(self, index: int):
        if index <= len(self.tasks):
            self.tasks.pop(index)
        else:
            print('такого в индекса нет')

    def save_to_json(self, filename: str):
        with open('self.tasks.json', 'w') as filename:
            json.dump(self.tasks, filename, indent=4)

    def load_from_json(self, filename: str):
        with open('self.tasks.json', 'r') as filename:
            self.tasks = json.load(filename)

    def view_list(self):
        for index, item in enumerate(self.tasks):
            print(f'{index}.{item['описание']} - Статус: {item['статус']}')