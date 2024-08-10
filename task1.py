def encryption(text, shift):
    result=""

    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result += chr((ord (char)+shift-65) % 26+65)
        elif(char.islower()):
            result += chr((ord(char)+shift-97) % 26 + 97)
        else:
              result += char
    return result 

def decryption(text,shift):
    result=""
    
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result += chr((ord (char)-shift-65) % 26+65)
        elif(char.islower()):
            result += chr((ord(char)-shift-97) % 26 + 97)
        else:
              result += char
    return result    
def main():
    print("Task 1- caesar-cipher")
    text=input("Enter the Message you wanna encrypt or decrypt:")
    shift= int(input("Enter the Shift Value(0-25):"))
    choice=input("Enter ('e') for encryption or ('d')for decryption:").lower()
    
    if choice == 'e':
     encrypted_text= encryption(text,shift)
     print("encrypted text:", encrypted_text)
    elif choice == 'd':
     dencrypted_text= decryption(text,shift)
     print("decrypted text:", dencrypted_text)
    else:
        print("Kindly enter a valid input")
if __name__ == "__main__":
    main()
        