from task import  Task


class BoardList:
<<<<<<< Updated upstream
    def __init__(self, name):
        pass
    
    def add_task(self):
        pass
=======
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

    def edit_task(self, tasks, new_task):
        self.new_task = new_task
        n = int(input("Enter task title you will like to edit:"))
        for n in tasks:
            new_task = print("enter your new task: ")
            tasks.items(n)== new_task
            print(new_task)

>>>>>>> Stashed changes

    def delete_board_list(self):
        pass

<<<<<<< Updated upstream
    def view_tasks(self):
        pass


if __name__ == '__main__':
    pass
=======

    def delete_task(self):
        pass


userstory1 = BoardList('dd')
userstory1.add_task(Task("wash",'12/10/2017','09:00'))
print(userstory1)
userstory1.edit_task("wash", "newwash")
#
#
#
#
#
#
#
#     def delete_task(self):
#         task = input("please, enter task name to delete:")
#         self.tasklist.remove(task)
#         print("your task has been deleted")
#
#
# newboard = BoardList()
# exit = False
# while not exit:
#     answer = input(" do you want add a new task? Y/N:")
#     if answer.lower() == "y":
#         newboard.add_task()
#         exit = False
#     elif answer.lower() == "n":
#         exit = True
#
# else:
#     exit = False
# print(newboard)f
#
# # def delete_board_list(self):
# # pass
# #
# # def view_tasks(self):
# #         pass
# #
# # # class Card:
# # #
# # #     def _init_(self, name):
# # #         self.name = name
# # #
# # #     def _eq_(self, other):
# # #         if isinstance(other, dict):
# # #             return other.get("name", None) == self.name
# # #         return NotImplemented
# # #
# # #     def _repr_(self):
# # #         return "{}({!r}, {!r})".format(
# # #             self._class.name_, self.key, self.value)
# #
# # if __name__ == '__main__':
#     pass
>>>>>>> Stashed changes
