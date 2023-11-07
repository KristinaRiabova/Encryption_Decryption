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
