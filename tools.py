from datetime import datetime
import json
import user_page
import admin_page


class User:
    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__password = password
        self.create_date = f"{datetime.now().date()}"
        self.status = "user"

    @property
    def get_password(self):
        return self.__password

    def save(self):
        with open("users.json", encoding="utf-8") as file:
            data = json.load(file)
        with open("users.json", "w") as f:
            new_user = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "username": self.username,
                "password": self.get_password,
                "create_date": self.create_date,
                "status": self.status
            }
            data["users"].append(new_user)
            json.dump(data, f, indent=6)
            print("Muvaffaqiyatli ro'yhatdan o'tildi")

    @staticmethod
    def check_user(username: str, password: str):
        with open("users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                if username == user["username"] and password == user["password"]:
                    if user["status"] == "user":
                        print("Welcome user page")
                        return user_page.landing_page()
                    elif user["status"] == "admin":
                        print("welcome admin page")
                        return admin_page.landing_page()

            return False
