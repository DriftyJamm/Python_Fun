def hill_encrypt(message, key_matrix):
    message = message.replace(" ", "").lower()
    
    if len(message) % 2 != 0:
        message += 'x'
    message_nums = [ord(char) - ord('a') for char in message]

    encrypted = ''
    for i in range(0, len(message_nums), 2):
        vector = message_nums[i:i+2]
        result = [
            (key_matrix[0][0]*vector[0] + key_matrix[0][1]*vector[1]) % 26,
            (key_matrix[1][0]*vector[0] + key_matrix[1][1]*vector[1]) % 26
        ]
        encrypted += ''.join([chr(num + ord('a')) for num in result])
    
    return encrypted

key = [[3, 3], [2, 5]]  
message = "help"
cipher_text = hill_encrypt(message, key)
print("Encrypted:", cipher_text)
