from task import Task


class BoardList:
    def __init__(self, tasklist=[]):
        self.tasklist = tasklist

    def add_task(self):
        task = input("enter a task name:")
        self.tasklist.append(task)
        print("task has been added")

    def delete_task(self):
        task = input("please, enter task name to delete:")
        self.tasklist.remove(task)
        print("your task has been deleted")


newboard = BoardList()
exit = False
while not exit:
    answer = input(" do you want add a new task? Y/N:")
    if answer.lower() == "y":
        newboard.add_task()
        exit = False
    elif answer.lower() == "n":
        exit = True

else:
    exit = False
print(newboard)

# def delete_board_list(self):
# pass
#
# def view_tasks(self):
#         pass
#
# # class Card:
# #
# #     def _init_(self, name):
# #         self.name = name
# #
# #     def _eq_(self, other):
# #         if isinstance(other, dict):
# #             return other.get("name", None) == self.name
# #         return NotImplemented
# #
# #     def _repr_(self):
# #         return "{}({!r}, {!r})".format(
# #             self._class.name_, self.key, self.value)
#
# if __name__ == '__main__':
#     pass