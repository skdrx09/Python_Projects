message = input("Enter a message to Encrypt: ")
secret_message = ''
shiftkey = 0

while shiftkey > 26 or shiftkey < 1:
    shiftkey = int(input("How many characters should we shift? (1 - 25) "))

for char in message:

    if char.isalpha():
        char_code = ord(char) + shiftkey
        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char
print("Encrypted:", secret_message)

message = ''

for char in secret_message:
    if char.isalpha():
        char_code = ord(char) - shiftkey

        if char.upper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
           if char.lower():
               if char_code > ord('z'):
                   char_code -= 26
               elif char_code < ord('a'):
                   char_code += 26
        message += chr(char_code)
    else:
        message += char
print("Your Shift Key is:", shiftkey)
print("Decrypted Message:", message)