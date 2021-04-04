
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


def cesar(message, shift, todo):
    letters = alphabet.copy()
    move = []
    while len(move) < shift:
        move.append(letters[0])
        letters.remove(letters[0])

    for letter in move:
        letters.append(letter)

    message = list(message)

    if todo == "encode":
        encrypted = []
        for i in range(0, len(message)):
            if message[i] == " ":
                encrypted.append(" ")
            else:
                location = alphabet.index(message[i])
                encrypted.append(letters[location])

        print(f'Your {direction}d message is {"".join(encrypted)}')

    else:
        decrypted = []
        for i in range(0, len(message)):
            if message[i] == " ":
                decrypted.append(" ")
            else:
                location = letters.index(message[i])
                decrypted.append(alphabet[location])

        print(f'Your {direction}d message is {"".join(decrypted)}')


direction = ""
again = ""


def start():
    global again
    global direction
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