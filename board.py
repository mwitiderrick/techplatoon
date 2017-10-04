import sys
import csv
from boardlist import BoardList
from task import Task


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
    print("create a board")
    boardname = input("Board Name: ")
    boardcolor = input("Board Color: ")
    firstboard = Board(boardname, boardcolor)
    print('create boardlist and tasks')
    boardlistname = input("Boardlist name: ")

    board_list = BoardList(boardlistname, [Task('nm', '', '07:09', 'hhgghh')])
    firstboard.add_boardlist(board_list)
            
    firstboard.add_member("cave")
    firstboard.add_member("spicy")
    
    print(firstboard)
    
