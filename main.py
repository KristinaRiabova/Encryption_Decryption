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