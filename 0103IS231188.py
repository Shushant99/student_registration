students = {}

def register():
    print("\n--- Student Registration ---")
    
    name = input("Enter your name: ")
    branch = input("Enter your branch: ")
    age = int(input("Enter your age: "))
    fathers_name = input("Enter your father's name: ")
    mothers_name = input("Enter your mother's name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    tenth_percentage = float(input("Enter your 10th percentage: "))
    twelfth_percentage = float(input("Enter your 12th percentage: "))
    gender = input("Enter your gender: ")

    username = email.split('@')[0] + "_" + branch.lower()
    password = "password123"

    if username in students:
        print("User already exists! Try again.")
        return

    students[username] = {
        "name": name,
        "age": age,
        "fathers_name": fathers_name,
        "mothers_name": mothers_name,
        "address": address,
        "phone": phone,
        "email": email,
        "tenth_percentage": tenth_percentage,
        "twelfth_percentage": twelfth_percentage,
        "gender": gender,
        "branch": branch,
        "password": password
    }

    print(f"\nRegistered successfully!")
    print(f"Username: {username}")
    print(f"Default Password: {password}")


def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in students and students[username]["password"] == password:
        print("Login successful! Welcome to LNCT.")
        return username
    else:
        print("Invalid username or password.")
        return None


def show_profile(username):
    print("\n--- Profile Details ---")
    student = students[username]

    for key, value in student.items():
        if key != "password":
            print(f"{key.capitalize()}: {value}")


def update_profile(username):
    print("\n--- Update Profile ---")
    student = students[username]

    for key in student:
        if key == "password":
            continue

        new_value = input(f"Enter new {key} (current: {student[key]}) or press Enter to skip: ")
        if new_value:
            student[key] = new_value

    print("Profile updated successfully!")


def main():
    print("Welcome to LNCT Registration Portal")

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
                        print("Invalid choice.")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
