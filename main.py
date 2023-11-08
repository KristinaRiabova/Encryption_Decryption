
def encrypt_char(char, key):
    if char.isupper():
        return chr((ord(char) - ord('A') + key) % 26 + ord('A'))
    elif char.islower():
        return chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    else:
        return char


def decrypt_char(char, key):
    if char.isupper():
        return chr((ord(char) - ord('A') - key) % 26 + ord('A'))
    elif char.islower():
        return chr((ord(char) - ord('a') - key) % 26 + ord('a'))
    else:
        return char


def process_text(text, key, transformation_func):
    return ''.join(transformation_func(char, key) for char in text)


def encrypt(raw_text, key):
    return process_text(raw_text, key, encrypt_char)


def decrypt(encrypted_text, key):
    return process_text(encrypted_text, key, decrypt_char)


def encrypt_file(input_file, key):
    with open(input_file, 'r') as f:
        raw_text = f.read()

    return encrypt(raw_text, key)



def decrypt_file(input_file, key):
    with open(input_file, 'r') as f:
        encrypted_text = f.read()

    return decrypt(encrypted_text, key)



def write_text_to_file(text, output_file):
    with open(output_file, 'w') as f:
        f.write(text)

def main():
    while True:
        choice = input("Enter 'E' for encryption, 'D' for decryption, or 'exit' to quit: ")

        if choice == 'exit':
            break
        elif choice == 'E':
            input_file = input("Enter the input file name: ")
            output_file = input("Enter the output file name: ")
            key = int(input("Enter the encryption key: "))
            encrypted_text = encrypt_file(input_file, key)
            write_text_to_file(encrypted_text, output_file)
            print("Encryption complete.")
        elif choice == 'D':
            input_file = input("Enter the input file name: ")
            output_file = input("Enter the output file name: ")
            key = int(input("Enter the decryption key: "))
            decrypted_text = decrypt_file(input_file, key)
            write_text_to_file(decrypted_text, output_file)
            print("Decryption complete.")
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'exit'.")

if __name__ == "__main__":
    main()