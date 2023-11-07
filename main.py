def caesar_cipher(text, shift, encrypt=True):
    def shift_char(char):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            return chr(shifted + base)
        return char

    text = ''.join(map(shift_char, text))

    if encrypt:
        return text
    else:
        shift = -shift
        return ''.join(map(shift_char, text))

def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as f:
        raw_text = f.read()

    encrypted_text = caesar_cipher(raw_text, shift)

    with open(output_file, 'w') as f:
        f.write(encrypted_text)

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as f:
        encrypted_text = f.read()

    decrypted_text = caesar_cipher(encrypted_text, shift, encrypt=False)

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
            shift = int(input("Enter the shift value: "))
            encrypt_file(input_file, output_file, shift)
            print("Encryption complete.")
        elif choice == 'D':
            input_file = input("Enter the input file name: ")
            output_file = input("Enter the output file name: ")
            shift = int(input("Enter the shift value: "))
            decrypt_file(input_file, output_file, shift)
            print("Decryption complete.")
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'exit'.")

if __name__ == "__main__":
    main()