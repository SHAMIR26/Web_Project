# This is a simple web project that allows users to register and login.
# It is a Registration and Login system.

class Registration:
    user_data = {}  

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        if self.email in Registration.user_data:
            print("Email already registered.")
        else:
            Registration.user_data[self.email] = {
                "name": self.name,
                "password": self.password
            }
            print("Registration successful!")
            print("Welcome,", self.name)


class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        if self.email in Registration.user_data:
            if Registration.user_data[self.email]["password"] == self.password:
                print("Login successful!")
                print("Welcome back,", Registration.user_data[self.email]["name"])
            else:
                print("Incorrect password.")
        else:
            print("Email not registered.")


print("Welcome to the Registration and Login System!")
user_input = input("Enter 'register' to registration or 'login' to log in: ").strip().lower()

if user_input == "register":
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    reg = Registration(name, email, password)
    reg.register()
elif user_input == "login":
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    log = Login(email, password)
    log.login()
else:
    print("Invalid input. Please enter 'register' or 'login'.")
    

