import json


def print_course(course):
    with open("users.json", encoding="utf-8") as file:
        names = json.loads(file)
        for name in names["courses"]:
            if name["title"] == course:
                result = name
            return result


def tanlash():
    choice = input("""
                         1. Sotib olish
                         2. Orqaga
                >>> """)
    if choice == "1":
        print(f"Muvaffaqiyatli sotib olindi")
        return landing_page()

    elif choice == "2":
        return landing_page()

    else:
        print("Xatolik")
        return landing_page()


def course():
    courses = input("""
                 Kurslar
                 1. python
                 2. C dasturlash tili
                 3. Java
                 4. Orqaga
                >>> """)
    if courses == "1":
        print_course("python")
        tanlash()

    elif courses == "2":
        print("C dasturlash tili kursi")
        tanlash()

    elif courses == "3":
        print("Java kursi")
        tanlash()


def landing_page():
    course()
