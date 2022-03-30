# Create an array of customer dictionaries
# Enter customer (Yes/No): y
# Enter customer Name: Mateo Battilana 
# Enter customer (Yes/No): y
# Enter customer Name: Sally Smith 
# Enter customer (Yes/No): n
# Mateo Battilana
# Sally Smith

from ast import Continue
from re import I


customers = []

while True:

    try:
        create_entry = input("Enter customer? (Yes/No)")
        # Stores just the first letter and makes it lowercase for operations
        create_entry = create_entry[0].lower() 

        if  create_entry == 'y':

            f_name, l_name = input("Enter customer name: ").split()
            customers.append({"f_name" : f_name, "l_name" : l_name})
            continue

        elif create_entry == 'n':
            break
        
        else:
            print("Please enter a valid answer...")
            continue
    
    except ValueError:
        print("Please enter just the first and last names")
        continue

print()
for value in customers:
    print(value['f_name'], value['l_name'])
print()