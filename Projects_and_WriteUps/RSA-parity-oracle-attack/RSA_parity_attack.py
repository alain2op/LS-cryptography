# import the necessary libraries here
import sympy
import math
import random

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_string):
    # Split the binary string into chunks of 8 bits
    binary_values = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    # Convert each chunk to an ASCII character
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    # Join the characters into the final text string
    return ''.join(ascii_characters)

def binary_to_integer(binary_string):
    return int(binary_string, 2)

def integer_to_binary(integer_value):
    return bin(integer_value)[2:]




class RSA:
    """Implements the RSA public key encryption / decryption."""

    def __init__(self, key_length):
        # define self.p, self.q, self.e, self.n, self.d here based on key_length
        self.p = sympy.randprime(2**(key_length/ - 1), 2**(key_length))
        self.q = sympy.randprime(2**(key_length - 1), 2**(key_length))
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e=random.randint(2,(self.p-1)*(self.q-1))
        while(math.gcd(self.e,(self.p-1)*(self.q-1))!=1):
            self.e=random.randint(2,(self.p-1)*(self.q-1))
        self.d = sympy.mod_inverse(self.e, self.phi)
        pass

    def encrypt(self, binary_data):
        # return encryption of binary_data here
        return pow(binary_data, self.e, self.n)
        pass

    def decrypt(self, encrypted_int_data):
        # return decryption of encrypted_binary_data here
        return pow(encrypted_int_data,self.d,self.n)
        pass

class RSAParityOracle(RSA):
    """Extends the RSA class by adding a method to verify the parity of data."""

    def is_parity_odd(self, encrypted_int_data):
        # Decrypt the input data and return whether the resulting number is odd
        decrypted_data = self.decrypt(encrypted_int_data)
        return decrypted_data % 2 == 1

def parity_oracle_attack(ciphertext, rsa_parity_oracle):
    # implement the attack and return the obtained plaintext
    l=0
    r=rsa_parity_oracle.n
    while(r-l>1):
        ciphertext*=pow(2,rsa_parity_oracle.e,rsa_parity_oracle.n)
        ciphertext%=rsa_parity_oracle.n
        if rsa_parity_oracle.is_parity_odd(ciphertext):
            l=(l+r)//2
        else:
            r=((l+r)//2)+1
    return r

    pass

def int_to_bytes(value):
    # Convert integer to bytes
    length = (value.bit_length() + 7) // 8
    return value.to_bytes(length, byteorder='big')


def main():
    input_text = input("Enter the message: ")
    input_binary=text_to_binary(input_text)
    input_integer=binary_to_integer(input_binary)

    # Generate a 1024-bit RSA pair    
    rsa_parity_oracle = RSAParityOracle(1024)
    # Encrypt the message
    cipherinteger = rsa_parity_oracle.encrypt(input_integer)
    print("Encrypted message is: ",cipherinteger)
    # print("Decrypted text is: ",rsa_parity_oracle.decrypt(ciphertext))

    # Check if the attack works
    plaintext_integer = parity_oracle_attack(cipherinteger, rsa_parity_oracle)
    plaintext_binary = integer_to_binary(plaintext_integer)
    plaintext=binary_to_text(plaintext_binary)
    print("Obtained plaintext: ",plaintext)
    print(input_integer,plaintext_integer)
    assert input_integer == plaintext_integer


if __name__ == '__main__':
    main()