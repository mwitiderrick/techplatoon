class Task:
    def __init__(self,name,date,time,comment):
        self.name = name
        self.date = date
        self.time = time
        self.comment = comment

    def add_comment(self):
        return(self.comment)

    def delete_comment(self):
        if comment in self.comment:
            del comment

    def __repr__(self):
        return "{} is due on {} at {}".format(self.name, self.date, self.time)
    
if __name__ == "__main__":
    task_name = input("Assign Name: ")
    task_date = input("Assign Date: ")
    task_time = input("Assign Time: ")
    task_comment = input("Assign Comment: ")

    New_Task = Task(task_name, task_date,task_time, task_comment)
    print(New_Task)

