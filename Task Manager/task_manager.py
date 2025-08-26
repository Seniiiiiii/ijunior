import json

class TaskManager:
    def __init__(self):
        self.tasks = [{"описание": "Первая задача", "статус": False}, {"описание": "Вторая задача", "статус": False}]

    def add_task(self, description: str):
        self.tasks.append({"описание": description, "статус": False})

    def complete_task(self, index: int):
        if self.tasks[index]:
            self.tasks[index]['статус'] = True

    def remove_task(self, index: int):
        self.tasks.pop(index)

    def save_to_json(self, filename: str):
        with open('self.tasks.json', 'w') as filename:
            json.dump(self.tasks, filename, indent=4)

    def load_from_json(self, filename: str):
        with open('self.tasks.json', 'r') as filename:
            self.tasks = json.load(filename)

    def view_list(self):
        i = 1

        for item in self.tasks:
            print(f'{i}.{item['описание']} - Статус: {item['статус']}')

            i += 1

    def get_list_tasks(self):
        return self.tasks()