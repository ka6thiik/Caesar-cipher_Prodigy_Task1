
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Encrypt the character
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    print("Caesar Cipher Program")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
