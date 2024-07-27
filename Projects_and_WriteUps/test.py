def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Example usage:
text = "ak"
binary_representation = text_to_binary(text)
print(binary_representation)
