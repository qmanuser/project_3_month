import json
import user_page


def landing_page():
    bottom = input("""
           1. Users
           2. Courses
    """)
    if bottom == "1":
        with open("users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                print(f"""
                firstname: {user["first_name"]}
                lastname: {user["last_name"]}
                username: {user["username"]}
                password: {user["password"]}
                status: {user["status"]}
                """)

    elif bottom == "2":
        user_page.course()
