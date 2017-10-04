import csv
from boardlist import BoardList


class Board():
    def __init__(self, name, color, boardlists=[], users=[]):
        self.name = name
        self.color = color
        self.boardlists = boardlists
        self.users = users

    def __repr__(self):
        return """
        Board: {}
        {} 
        Board Members: {}
        """.format(self.name, self.boardlists, self.users)

    def change_board_name(self, newname):
        self.name = newname
        return self.name

    def change_board_color(self, newcolor):
        self.color = newcolor
        return self.color

    def search_board_by_name(self, searchname):
        if self.name == searchname:
            return self.name

    def add_member(self, member):
        with open("users.csv", "r") as user_file:
            users = csv.DictReader(user_file)
            for user in users:
                if member == user['username']:
                    self.users.append(member)
                else:
                    print("member doesn't exist")

    def add_boardlist(self, boardlist):
        if isinstance(boardlist, BoardList):
            self.boardlists.append(boardlist)
        else:
            print("that isn't a board")
        

if __name__ == '__main__':
    firstboard = Board("hypothesis", "red")
    firstboard.add_boardlist(BoardList("To do", ["wash", '12/10/2017', '09:00', "please notify upon completion"]))
    firstboard.add_boardlist(BoardList("Doing", ["wash", '12/10/2017', '09:00', "please notify upon completion"]))
    firstboard.add_member("cave")
    firstboard.add_member("spicy")
    print(firstboard)
    
