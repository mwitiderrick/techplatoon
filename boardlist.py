from task import  Task


class BoardList:
    def __init__(self, name, tasks = []):
        self.tasks = tasks
        self.name = name

    def __repr__(self):
        return """
        Boardlist: {}
        {}
        """.format(self.name,self.tasks)

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            print("that does not look like a task")

    def edit_task(self):


    def delete_task(self):
        pass


userstory1 = BoardList('dd')
userstory1.add_task(Task("wash",'12/10/2017','09:00'))
print(userstory1)


if __name__ == '__main__':
    pass