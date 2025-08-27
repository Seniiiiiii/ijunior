from task_manager import TaskManager

tasks = TaskManager()


class PyTest:
    def test_1(self):
        tasks.view_list()

        description = 'Третья задача'

        tasks.add_task(description)
        tasks.complete_task(1)

        tasks.view_list()


    def test_2(self):
        tasks.view_list()
        tasks.remove_task(1)
        tasks.view_list()

    def test_3(self):
        tasks.save_to_json('json')
        tasks.load_from_json('json')

test = PyTest()

test.test_1()
test.test_2()
test.test_3()