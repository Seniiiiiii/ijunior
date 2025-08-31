import json

class TaskManager:
    def __init__(self):
        self.tasks = [
            {"description": "Первая задача", "status": False},
            {"description": "Вторая задача", "status": False}
        ]

    def add_task(self, description: str):
        self.tasks.append({"description": description, "status": False})

    def complete_task(self, index: int):
        if 0 <= index <= len(self.tasks):
            self.tasks[index]['status'] = True
        else:
            print('такого в индекса нет')

    def remove_task(self, index: int):
        if 0 <= index <= len(self.tasks):
            self.tasks.pop(index)
        else:
            print('такого в индекса нет')

    def save_to_json(self, file: str):
        with open(file, 'w') as my_file:
            json.dump(self.tasks, my_file, indent=4)

    def load_from_json(self, file: str):
        with open(file, 'r') as my_file:
            self.tasks = json.load(my_file)

    def view_list(self):
        for index, item in enumerate(self.tasks):
            print(f'{index}.{item['description']} - Статус: {item['status']}')

test = TaskManager()