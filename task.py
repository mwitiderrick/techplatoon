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
	TName = input("Assign Name: ")
	TDate = input("Assign Date: ")
	TTime = input("Assign Time: ")
	TComment = input("Assign Comment: ")

	New_Task = Task(TName, TDate,TTime, TComment)
	print(New_Task)

