# Tarik Farhoud

def encode(password):
    total = ""
    for item in password:
        item = int(item) + 3
        item = str(item)
        total = total + item
    return total



if __name__ == "__main__":
    option_chosen = 0
    while option_chosen != 3:
        print("""Menu  
------------- 
1. Encode  
2. Decode  
3. Quit""")

        option_chosen = int(input("\nPlease enter an option: "))
        if option_chosen == 1:
            password = input("\nPlease enter your password to encode: ")
            print("\nYour password has been encoded and stored!")
            print()
            encoded_password = encode(password)
        elif option_chosen == 2:
            print(f"\nThe encoded password is {encoded_password}, and the original password is {password}.")
            print()
        elif option_chosen == 3:
            break
        else:
            print("\nInvalid Option Chosen. Try Again!")
            print()