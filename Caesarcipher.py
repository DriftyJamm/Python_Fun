def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char  
    return result

plain_text = "Hello, World!"
shift_amount = 3

encrypted_text = caesar_cipher(plain_text, shift_amount)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift_amount)
print("Decrypted:", decrypted_text)
