# Tarik Farhoud

def encode(password):
    total = ""
    for item in password:
        if int(item) < 7:
            item = int(item) + 3
            item = str(item)
            total = total + item
        elif int(item) <= 9 and int(item) >= 7:
            item = int(item) + 3
            item = int(item) % 10
            item = str(item)
            total = total + item
    return total

# Katherine Blanco
# Defines the function to decode the password from earlier
def decode(enc_pass, dec_pass=""):

    # For each number in the encoded password, decrease by 3
    # If the number is between 0 and 2, raise the result by 10 to not get a negative number
    for i in enc_pass:
        if int(i) > 2:
            dec_pass += str(int(i) - 3)
        elif 0 <= int(i) <= 2:
            dec_pass += str((int(i) - 3) + 10)

    print("The encoded password is " + enc_pass + ", and the original password is " + dec_pass + ".\n")



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
            decode(encoded_password)
        elif option_chosen == 3:
            break
        else:
            print("\nInvalid Option Chosen. Try Again!")
            print()