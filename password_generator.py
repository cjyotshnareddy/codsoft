import random
import string

def generate_password():
    length = int(input("Enter the desired password length: "))
    if length < 6:
        print("Password length should be at least 6 characters for security.")
        return
    
    print("Choose complexity level:")
    print("1. Letters only")
    print("2. Letters and numbers")
    print("3. Letters, numbers, and special characters")
    choice = int(input("Enter choice (1-3): "))
    
    if choice == 1:
        characters = string.ascii_letters
    elif choice == 2:
        characters = string.ascii_letters + string.digits
    elif choice == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice. Using default complexity (letters, numbers, special characters).")
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

generate_password()
