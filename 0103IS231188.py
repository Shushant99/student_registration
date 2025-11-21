#note ( user name will be your emailm followed by your beanch and password will be "password123 by drfault" )
students = {}
def register():
    name = input("Enter your name: ")
    branch = input("Enter your branch: ")
    age = input("Enter your age: ")
    fathers_name = input("Enter your father's name: ")
    mothers_name = input("Enter your mother's name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    tenth_percentage = input("Enter your 10th percentage: ")
    twelfth_percentage = input("Enter your 12th percentage: ")
    gender = input("Enter your gender: ")
    
# we will create username using email prefix and branch and a password default as 'password123'
    username = email.split('@')[0] +  branch
    password = "password123"
    students[username] = {
        'name': name,
        'age': age,
        'fathers_name': fathers_name,
        'mothers_name': mothers_name,
        'address': address,
        'phone': phone,
        'email': email,
        'tenth_percentage': tenth_percentage,
        'twelfth_percentage': twelfth_percentage,
        'gender': gender,
        'branch': branch
    }

    print(f"Student registered successfully! Your username is {username} and your default password is {password}")

def login():
    print("Login to your account")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in students and password == "password123":
        print("Welcome to lnct you have asuccessfully logged in")
        return username
    else:
        print("Invalid username or password")
        return None
def show_profile(username):
    student = students[username]
    print("Profile Details:")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")

def update_profile(username):
    student = students[username]
    print("Update Profile Details ")
    for key in student.keys():
        new_value = input(f"Enter new {key} (current: {student[key]}): ")
        if new_value:
            student[key] = new_value
    print("Profile updated successfully!")
def main():
    print("welcome to lnct regestation portal")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    print("\n1. Show Profile\n2. Update Profile\n3. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == '1':
                        show_profile(username)
                    elif sub_choice == '2':
                        update_profile(username)
                    elif sub_choice == '3':
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice, please try again.")
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
   