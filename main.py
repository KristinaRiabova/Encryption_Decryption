def encrypt(raw_text, key):
    encrypted_text = []

    for char in raw_text:
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted_char = char

        encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)


def decrypt(encrypted_text, key):
    decrypted_text = []

    for char in encrypted_text:
        if char.isupper():
            decrypted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            decrypted_char = char

        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)



def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as f:
        raw_text = f.read()

    encrypted_text = encrypt(raw_text, key)

    with open(output_file, 'w') as f:
        f.write(encrypted_text)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as f:
        encrypted_text = f.read()

    decrypted_text = decrypt(encrypted_text, key)

    with open(output_file, 'w') as f:
        f.write(decrypted_text)

def main():
    while True:
        choice = input("Enter 'E' for encryption, 'D' for decryption, or 'exit' to quit: ")

        if choice == 'exit':
            break
        elif choice == 'E':
            input_file = input("Enter the input file name: ")
            output_file = input("Enter the output file name: ")
            key = int(input("Enter the encryption key: "))
            encrypt_file(input_file, output_file, key)
            print("Encryption complete.")
        elif choice == 'D':
            input_file = input("Enter the input file name: ")
            output_file = input("Enter the output file name: ")
            key = int(input("Enter the decryption key: "))
            decrypt_file(input_file, output_file, key)
            print("Decryption complete.")
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'exit'.")

if __name__ == "__main__":
    main()
