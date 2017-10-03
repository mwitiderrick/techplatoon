import sys
import csv
import re
import bcrypt


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

    @staticmethod
    def sign_in(email_to_be_entered, password_to_be_entered):
        with open("users.csv", "r") as user_file:
            users = csv.DictReader(user_file)
            for user in users:
                password_to_be_hashed = bytes(password_to_be_entered, 'utf-8')
                if email_to_be_entered == user['email'] and bcrypt.hashpw(password_to_be_entered, password_to_be_hashed) == hashe:
                    print("You are in..")
                else:
                    print("Wrong Credentials :(")


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
    return bcrypt.hashpw(password_to_hash, bcrypt.gensalt())


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
            hashed = hash_password(bytes(password, 'utf-8'))
            new_user = User(fullname=fullname, email=email, username=username, password=hashed)

            with open("users.csv", "a+") as users_file:
                csvWriter = csv.writer(users_file)
                dataRow = [fullname, email, username, hashed]
                csvWriter.writerow(dataRow)
                print("New user created successfully..")

        elif choice == '2':
            user_email = input('Enter your email address: ')
            user_password = input('Enter your password: ')
            User.sign_in(user_email, user_password)
        elif choice == 'q':
            sys.exit()
        else:
            print('Invalid input..')
