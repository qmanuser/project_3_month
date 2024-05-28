from tools import User
from login import login_page

def register():
    print("Register Page")
    first_name = input("Ism: ")
    last_name = input("Familia: ")
    username = input("username: ")
    password1 = input("password: ")
    password2 = input("passwordni tastiqlash: ")
    while password1 != password2:
        print("Xatolik qaytadan urinib ko'ring!")
        password1 = input("password: ")
        password2 = input("passwordni tastiqlash: ")

    user = User(first_name, last_name, username, password1)
    user.save()
    return login_page()

