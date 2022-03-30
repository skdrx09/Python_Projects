while True:
    try:
        in_num = int(input("Guess a number between 1 and 10: "))
        if in_num == 7:
            break
            print("You won!")
    except ValueError:                          
        print("You didn't enter a number...")
    except:
        print("Unknown Error")
