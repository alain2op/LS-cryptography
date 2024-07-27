import numpy as np
#the following are the same functions as that in hill_encryption
def toNumber(message):
    message = message.upper()
    encrypted_message = []
    for char in message:
        if ord(char) <= ord('Z') and ord(char) >= ord('A'):
            encrypted_message.append(ord(char) - ord('A'))
    while len(encrypted_message) % 3 != 0:
        encrypted_message.append(23)
    return encrypted_message

def toText(message):
    final_message = ""
    for number in message:
        final_message += chr(int(number) % 26 + ord('A'))
    return final_message

def key_set(keytext):
    keytext = keytext.upper()
    key_list = []
    for char in keytext:
        if ord(char) <= ord('Z') and ord(char) >= ord('A'):
            key_list.append(ord(char) - ord('A'))
    return np.array(key_list).reshape(3, 3)

def Hill_Encryption(key, message):
    key = key_set(key)
    initial_encrypted_message = toNumber(message)
    encrypted_message = []
    for i in range(0, len(initial_encrypted_message), 3):
        message_vector = np.reshape(np.array(initial_encrypted_message[i:i+3]), (3, 1))
        encrypted_vector = np.matmul(key, message_vector)
        encrypted_message.extend(encrypted_vector.flatten())
    return toText(encrypted_message)

plain_text=input("Enter the plain text: ")
cipher_text=input("Enter the cipher text: ")
plain_text_padded=plain_text.upper()+'X'*(len(cipher_text)-len(plain_text))#padding the plain_text
plain=np.array(toNumber(plain_text_padded)).reshape(-1,3)
cipher=np.array(toNumber(cipher_text)).reshape(-1,3)
key_vectors=[[],[],[]]
for n in range(3):#bruteforcing all the possibilities for a plaintext of length 9(after padding if required)
    for i in range(26):
        for j in range(26):
            for k in range(26):
                count=0
                for l in range(3):
                    if(i*plain[l][0]+j*plain[l][1]+k*plain[l][2])%26==cipher[l][n]:
                        count+=1
                if(count==3):
                    key_vectors[n].append([i,j,k])
possible_keys=[]
for i in key_vectors[0]:
    for j in key_vectors[1]:
        for k in key_vectors[2]:
            key=[]
            key.extend(i)
            key.extend(j)
            key.extend(k)
            possible_keys.append(toText(key))
possible_keys=list(set(possible_keys))#this is the set of all possible keys after initial analysis
block_count=3
block_max=len(cipher_text)/3
while(block_count<block_max):#verifying our possible keys for the further text and validating the possible keys
    keystoremove=[]
    for key in possible_keys:
        if(Hill_Encryption(key,plain_text_padded[3*block_count:3*block_count+3])!=cipher_text[3*block_count:3*block_count+3]):
            keystoremove.append(key)
    for key in keystoremove:
        possible_keys.remove(key)
    block_count+=1
print("Possible Keys Are: ")
for key in possible_keys:
    print(key)