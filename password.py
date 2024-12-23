import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for a strong password.")
        return None

    # Ensuring the password contains at least one lowercase, uppercase, digit, and special character
    characters = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill the rest of the password length with a mix of all character types
    characters += random.choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=length - 4
    )

    # Shuffle to ensure randomness
    random.shuffle(characters)

    return ''.join(characters)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")
