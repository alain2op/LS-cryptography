def Riddler_XOR(a, b, c):
	return (ord(a)^ord(b)*ord(b)^ord(c))

# def reverseXOR(cipher, length):
# 	flag = [''] * length
# 	for i in range(2, length):
# 		for a in range(32, 127):
# 			for b in range(32, 127):
# 				for c in range(32, 127):
# 					if Riddler_XOR(chr(a), chr(b), chr(c)) == cipher[i-2]:
# 						flag[i-2] = chr(a)
# 						flag[i-1] = chr(b)
# 						flag[i] = chr(c)
# 						break
# 				if flag[i]:
# 					break
# 			if flag[i]:
# 				break
# 	if len(flag) > 2:
# 		for a in range(32, 127):
# 			for b in range(32, 127):
# 				for c in range(32, 127):
# 					if Riddler_XOR(flag[-2], flag[-1], chr(a)) == cipher[-2]:
# 						flag[0] = chr(a)
# 					if Riddler_XOR(flag[-1], flag[0], chr(a)) == cipher[-1]:
# 						flag[1] = chr(a)
    
# 	return ''.join(flag)

# def decrypt_riddler_xor(cipher):
#     length = len(cipher) + 2
#     flag = [None] * length
    
#     # Try to initialize known values if any
#     for i in range(len(cipher)):
#         if i < length - 2:
#             if flag[i + 1] is not None and flag[i + 2] is not None:
#                 flag[i] = chr(cipher[i] ^ (ord(flag[i + 1]) * ord(flag[i + 1])) ^ ord(flag[i + 2]))
                
#     # Solve for the last two characters
#     if flag[length - 2] is not None and flag[length - 1] is not None:
#         flag[length - 2] = chr(cipher[-2] ^ (ord(flag[length - 1]) * ord(flag[0])) ^ ord(flag[0]))
#         flag[length - 1] = chr(cipher[-1] ^ (ord(flag[0]) * ord(flag[1])) ^ ord(flag[0]))
    
#     # Debugging: Print flag list to identify None values
#     for i, f in enumerate(flag):
#         if f is None:
#             print(f"Flag at index {i} is None")
    
#     # Filter out None values before joining
#     filtered_flag = [f for f in flag if f is not None]
    
#     return ''.join(filtered_flag)

# # Example usage
cipher_1 = [12331, 6909, 15145, 9792, 12944, 3027, 12611, 13520, 2347, 9024, 2330, 1406, 8982, 13254, 2348, 8988, 11875, 7271, 2580, 10796, 9039, 10414, 7217, 12110, 9053, 12970, 2420, 10536, 10835, 13445, 15652, 7907]
flag="YoS"
for i in range(1,len(cipher_1)-1):
	flag+=chr(cipher_1[i]^(ord(flag[i+1])**2)^ord(flag[i]))
# flag = decrypt_riddler_xor(cipher_1)
# print(flag)

print(flag)