def encode_password(password):

    if len(password) != 8:
        print("Error: Password must have exactly 8 digits")

    else:
        encoded_password = ""
        for digit in password:
            encoded_digit = str((int(digit) + 3)%10)
            encoded_password += encoded_digit

        print("Your password has been encoded and stored!\n")
        return encoded_password


#Isabelle - decode
def decode_password(password):
        encoded = [int(x) for x in str(password)]
        for i in range(8):
            temp = encoded[i]
            encoded[i] = temp
        decodedPassword = ''.join(map(str, encoded))

        print(f'The encoded password is {password}, and the original password is {decodedPassword}\n')
        return decodedPassword

def main():
    while True:
        print("Menu\n-------\n1. Encode\n2. Decode\n3. Quit")
        menu_select = int(input("Please enter an option: "))
        if menu_select == 1:
            user_password = input("Please enter your password to encode: ")
            encoded_user_password = encode_password(user_password)

        #Isabelle - decode
        elif menu_select == 2:
            decode_password(encoded_user_password)
        elif menu_select == 3:
            break
        else:
            print("Invalid selection, please try again.")


if __name__ == '__main__':
    main()
