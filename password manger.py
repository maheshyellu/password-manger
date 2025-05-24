def create_custom_password():
    print("Welcome to the Custom Password Creator!")
    print("You will choose each part of your password.")

    # Get input parts from user
    letters = input("Enter the letters you want (a-z, A-Z): ")
    numbers = input("Enter the numbers you want (0-9): ")
    symbols = input("Enter the symbols you want (!, @, #, etc.): ")

    # Combine all parts into one password
    password = letters + numbers + symbols

    # Optionally shuffle the password to make it stronger
    import random
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    print(f"\nYour custom password is: {final_password}")

def main():
    create_custom_password()

if __name__ == "__main__":
    main()
