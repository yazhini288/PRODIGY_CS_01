def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Choose an option (E for Encrypt, D for Decrypt): ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Exiting.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Must be an integer.")
        return

    if choice == 'E':
        encrypted_msg = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_msg}")
    else:
        decrypted_msg = caesar_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_msg}")

if __name__ == "__main__":
    main()
