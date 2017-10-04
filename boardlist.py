from task import Task


class BoardList:
    def __init__(self, name, tasks=[]):
        self.tasks = tasks
        self.name = name

    def __repr__(self):
        return """
        Boardlist: {}
        {}
        """.format(self.name, self.tasks)

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            print("that does not look like a task")

    def edit_task(self):
        pass

    def delete_task(self, tasks):
        n = int(input("Enter the position:"))
        if n >= (len(tasks)+1):
            del tasks[n-1]
            print(tasks)
        else:
            print('Error')


userstory1 = BoardList('dd')
userstory1.add_task(Task("wash", '12/10/2017', '09:00', "please notify upon completion"))
print(userstory1)
