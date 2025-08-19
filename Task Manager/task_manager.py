import json

class TaskManager:
    def __init__(self):
        self.tasks = [{'Первая задача': False}, {'Вторая задача': False}]

    def add_task(self, description: str):
        self.tasks.append({description: False})


    def complete_task(self, index: int):
        if len(self.tasks) >= index:
            for task in self.tasks:
                if self.tasks[task] == index: # Вот тут не понимаю -_-...
                    for _, status in task:
                        status == True
        else:
            print('такой задачи нет')

        print(self.tasks)

    def remove_task(self, index: int):
        self.tasks.pop(index)


    def save_to_json(self, filename: str):
        with open('self.tasks.json', 'w') as filename:
            json.dump(self.tasks, filename, indent=4)


    def load_from_json(self, filename: str):
        with open('self.tasks.json', 'r') as filename:
            self.tasks = json.load(filename)

test = TaskManager()

test.complete_task(1)