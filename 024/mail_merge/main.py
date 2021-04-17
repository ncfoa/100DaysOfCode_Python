# Form Letter writer

STRIP_ME = "[name]"

with open("./Input/Names/invited_names.txt") as sln:
    names = sln.readlines()

with open("./Input/Letters/starting_letter.txt") as lr:
    message = lr.read()
    for name in names:
        new_name = name.strip("\n")
        new_message = message.replace(STRIP_ME, new_name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as slw:
            slw.write(new_message)

