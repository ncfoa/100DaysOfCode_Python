# Cesar Shift Cipher


def logo():
    ascii_art = '''
      ______  _______     _______.     ___      .______                     
     /      ||   ____|   /       |    /   \     |   _  \                    
    |  ,----'|  |__     |   (----`   /  ^  \    |  |_)  |                   
    |  |     |   __|     \   \      /  /_\  \   |      /                    
    |  `----.|  |____.----)   |    /  _____  \  |  |\  \----.               
     \______||_______|_______/    /__/     \__\ | _| `._____|                                                                                     
                  ______  __  .______    __    __   _______ .______         
                 /      ||  | |   _  \  |  |  |  | |   ____||   _  \        
                |  ,----'|  | |  |_)  | |  |__|  | |  |__   |  |_)  |       
                |  |     |  | |   ___/  |   __   | |   __|  |      /        
                |  `----.|  | |  |      |  |  |  | |  |____ |  |\  \----.   
                 \______||__| | _|      |__|  |__| |_______|| _| `._____|   
                                                                            '''
    print(ascii_art)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

again = ""
def cesar(message, shift, todo):
    global again
    end_text = ""
    if todo == "decode":
        shift *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            shift_pos = position + shift
            end_text += alphabet[shift_pos]
        else:
            end_text += char
    print(f"The {todo}d text is {end_text}")




def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_num = int(input("Type the shift number:\n"))
    shift_num = shift_num % 26
    cesar(text, shift_num, direction)
    again = input("Would you like to try again? ('y'/'N')\n").lower()


logo()
start()

while again == "y":
    start()
else:
    print("Goodbye...")
    exit(0)





