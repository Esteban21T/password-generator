import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special=True, 
                      exclude_ambiguous=True, only_consonants=False, only_vowels=False):
    characters = string.ascii_lowercase
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"

    if only_consonants:
        characters = consonants
    elif only_vowels:
        characters = vowels
    else:
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        # Excluir caracteres similares y ambiguos si está habilitado
        if exclude_ambiguous:
            ambiguous_chars = '1l0O'
            characters = ''.join([c for c in characters if c not in ambiguous_chars])

    # Asegurarse de que la contraseña cumpla con ciertos criterios de seguridad
    if include_uppercase and include_numbers and include_special and not (only_consonants or only_vowels):
        while True:
            password = ''.join(random.choice(characters) for _ in range(length))
            if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password)):
                break
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    exclude_ambiguous = input("Exclude ambiguous characters (e.g., '1', 'l', '0', 'O')? (yes/no): ").lower() == 'yes'
    only_consonants = input("Use only consonants? (yes/no): ").lower() == 'yes'
    only_vowels = input("Use only vowels? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_uppercase, include_numbers, include_special, 
                                 exclude_ambiguous, only_consonants, only_vowels)
    print(f"Generated Password: {password}")
