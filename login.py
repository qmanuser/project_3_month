from tools import User


def login_page():
    username = input("username: ")
    password = input("password: ")
    if User.check_user(username, password) is False:
        print("username yoki password hato kiritildi")
        return login_page()
    else:
        return User.check_user(username, password)
