import sys
import board
import boardlist
import task
import csv


class Account:
    def __init__(self, users=[]):
        self.users = users
        try:
            with open("contacts.csv", "x") as csv_file:
                csv_writer = csv.writer(csv_file)
                headers = ['fullname', 'email', 'username', 'password']
                csv_writer.writerow(headers)
        except:
            pass

    def menu(self):
        print("Welcome to the menu: ")
        board_name = input('Enter board name: ')
        board_color = input('Enter board color: ')
        board.Board(board_name, board_color)
        print("{} has been set up. Do you want to add a list to it y/n?".format(board_name))
        user_choice = input()
        if user_choice == 'y':
            list_name = input('Enter the name of the list: ')
            boardlist.BoardList(list_name)
        elif user_choice == 'n':
            pass
        else:
            print('Invlaid input')

    def add_user(self, user):
        self.users.append(user)
        print(self.users)

    def sign_in(self):
        user_email = input('Enter your email address: ')
        user_password = input('Enter your password: ')
        for account in self.users:
            if account.email == user_email and account.password == user_password:
                self.menu()


class User:
    def __init__(self, fullname, email, username, password):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return """          [{} Details]
                            Fullname: {}
                            Email:    {}
                            Username: {}
                            Password: {}
                    
        """.format(self.fullname, self.fullname, self.email, self.username, self.password)


derrick = Account()
if __name__ == '__main__':
    while True:
        print('Enter 1 to sign up 2 to sign in and q to exit ')
        choice = input()
        if choice == '1':
            print('Creating a new user:\n')
            fullname = input('Enter fullname: ')
            email = input('Enter email: ')
            username = input('Enter Username: ')
            password = input('Enter Password: ')
            derrick.add_user(User(fullname=fullname, email=email, username=username, password=password))
            with open("users.csv", "a+") as users_file:
                csvWriter = csv.writer(users_file)
                dataRow = []
                csvWriter.writerow(dataRow)
                print("contact exported to csv")

        elif choice == '2':
            derrick.sign_in()
        elif choice == 'q':
            sys.exit()
        else:
            print('Invalid input..')
