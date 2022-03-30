# A - Z  ->  65 - 90
# a - z  ->  97 - 122   # Subtract 23 to make lower case a 2 digit number

norm_string = input("\nPlease enter an uppercase word: ")
print("\nYou entered:", norm_string)
u_value = ''

for char in norm_string:    
    u_value += str(ord(char) - 23) + ' '    

print("\nSecret Message:", u_value)

norm_string = ''
for i in range(0, len(u_value) - 1, 3):   # We know that each character translates into 2 digits (3 counting spaces)
    char_code = u_value[i] + u_value[i + 1]
    norm_string += chr(int(char_code) + 23)     # Add 23 back to decode it properly

print("\nBack to normal:", norm_string, '\n')

