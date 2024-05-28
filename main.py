from login import login_page
from register import register


def main():
    web = input("""
             1.  Login
             2.  Register
    """)
    if web == "1":
        return login_page()

    elif web == "2":
        return register()

    else:
        print("Xatolik!")
        main()


if __name__ == "__main__":
    main()
