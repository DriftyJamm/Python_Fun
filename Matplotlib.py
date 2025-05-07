def row_column_encrypt(plaintext, key):
    while len(plaintext) % len(key) != 0:
        plaintext += ' '
    matrix = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    sorted_key = sorted(list(key))
    col_indices = [key.index(char) for char in sorted_key]
    ciphertext = ""
    for col in col_indices:
        for row in matrix:
            if col < len(row):
                ciphertext += row[col]
    return ciphertext

def row_column_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    sorted_key = sorted(list(key))
    col_indices = [key.index(char) for char in sorted_key]
    columns = [''] * num_cols
    index = 0
    for col in col_indices:
        for row in range(num_rows):
            columns[col] += ciphertext[index]
            index += 1
    plaintext = ""
    for row in range(num_rows):
        for col in range(num_cols):
            plaintext += columns[col][row]
    return plaintext.strip()  

plaintext = "HELLO WORLD"
key = "3142"
ciphertext = row_column_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
print("Decrypted:", row_column_decrypt(ciphertext, key))

