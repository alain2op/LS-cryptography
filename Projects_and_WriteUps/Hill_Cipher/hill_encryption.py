import numpy as np

def toNumber(message):#this function coverts a string to it's chacter array, for eg "Ae D" is written as [0,4,3]
    message = message.upper()
    encrypted_message = []
    for char in message:
        if ord(char) <= ord('Z') and ord(char) >= ord('A'):
            encrypted_message.append(ord(char) - ord('A'))
    while len(encrypted_message) % 3 != 0:
        encrypted_message.append(23)
    return encrypted_message

def toText(message):#this function does the reverse of toNumber function
    final_message = ""
    for number in message:
        final_message += chr(int(number) % 26 + ord('A'))
    return final_message

def key_set(keytext):#this function converts a key string to its corresponding 3*3 matrix
    keytext = keytext.upper()
    key_list = []
    for char in keytext:
        if ord(char) <= ord('Z') and ord(char) >= ord('A'):
            key_list.append(ord(char) - ord('A'))
    return np.array(key_list).reshape(3, 3)

def Hill_Encryption(key, message):# the function that encrypts using hill cipher
    key = key_set(key)
    initial_encrypted_message = toNumber(message)
    encrypted_message = []
    for i in range(0, len(initial_encrypted_message), 3):
        message_vector = np.reshape(np.array(initial_encrypted_message[i:i+3]), (3, 1))
        encrypted_vector = np.matmul(key, message_vector)
        encrypted_message.extend(encrypted_vector.flatten())
    return toText(encrypted_message)

message = input("Enter the message to encrypt: ")
key = input("Enter the Key text: ")
print("Cipher Text is: ",Hill_Encryption(key, message))

