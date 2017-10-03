import sys
import board
import boardlist
import task
import csv
import re


class Account:
    def __init__(self, users=[]):
        self.users = users
        # with open("users.csv", "w") as csv_file:
        #     csv_writer = csv.writer(csv_file)
        #     headers = ['fullname', 'email', 'username', 'password']
        #     csv_writer.writerow(headers)

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


def check_email(email_to_check):
    # Create email regex.
    email_regex = re.compile(r'''(
     [a-zA-Z0-9._%+-]+ # username
     @                 # @ symbol
     [a-zA-Z0-9.-]+    # domain name
     (\.[a-zA-Z]{2,4}) # dot-something
     )''', re.VERBOSE)
    if not email_regex.match(email_to_check):
        return  False
    return True


def hash_password(password_to_hash):
    pass


new_user_account = Account()
if __name__ == '__main__':
    while True:
        print('Enter 1 to sign up 2 to sign in and q to exit ')
        choice = input()
        if choice == '1':
            print('Creating a new user:\n')
            fullname = input('Enter fullname: ')
            while True:
                email = input('Enter email: ')
                if check_email(email):
                    break
                print('That does not look like a valid email address..')

            username = input('Enter Username: ')
            password = input('Enter Password: ')
            new_user_account.add_user(User(fullname=fullname, email=email, username=username, password=password))
            with open("users.csv", "a+") as users_file:
                csvWriter = csv.writer(users_file)
                dataRow = [fullname, email, username, password]
                csvWriter.writerow(dataRow)
                print("New user created successfully..")

        elif choice == '2':
            new_user_account.sign_in()
        elif choice == 'q':
            sys.exit()
        else:
            print('Invalid input..')
