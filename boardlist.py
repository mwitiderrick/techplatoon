from task import Task


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
        task_to_delete = input('enter the task to delete: ')
        for element in tasks:
            if element == task_to_delete:
                new_task = input('enter a new task')
                element = new_task
                print(tasks)


    def delete_task(self, tasks):
         n = int(input("Enter the position:"))
         if n >= (len(tasks)+1):
            del tasks[n-1]
            print(tasks)
         else:
             print('Error')



userstory1 = BoardList()
