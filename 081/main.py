
code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ".": ".-.-.-", "?": "..--.."}

message = input("What would you like to transcribe into morse code?\n").upper()
encoded_message = ""
for i in message:
    if i in code:
        encoded_message = encoded_message + f"{code[i]} "

print(encoded_message)

