from user import User
from boardlist import BoardList


class Board(User):
    def __init__(self, name, color, boardlists=[]):
        self.name = name
        self.color = color
        self.boardlists = boardlists

    def __repr__(self):
        return """
        Board: {}
        {}
        """.format(self.name, self.boardlists)

    def change_board_name(self, newname):
        self.name = newname
        return self.name

    def change_board_color(self, newcolor):
        self.color = newcolor
        return self.color

    def search_board_by_name(self, searchname):
        if self.name == searchname:
            return self.name

    def add_team_member(self, newmember):
        if newmember not in User(self.fullname):
            self.fullname.append(newmember)
    
    def add_boardlist(self, boardlist):
        if isinstance(boardlist, BoardList):
            self.boardlists.append(boardlist)
        else:
            print("that isn't a board")
        

if __name__ == '__main__':
    firstboard = Board("hypothesis", "red")
    firstboard.add_boardlist(BoardList("To do"))
    print(firstboard)
    
