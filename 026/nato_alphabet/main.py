

alphabet = {"a": "alpha", "b": "bravo", "c": "charlie", "d": "delta", "e": "echo", "f": "foxtrot", "g": "gulf",
            "h": "hotel", "i": "india", "j": "juliet", "k": "kilo", "l": "lima", "m": "mike", "n": "november",
            "o": "oscar", "p": "papa", "q": "quebec", "r": "romeo", "s": "sierra", "t": "tango", "u": "uniform",
            "v": "victor", "w": "whiskey", "x": "xray", "y": "yankee", "z": "zulu", " ": " "}


# word should be any word that you need to spell out phonetically ie: Supercalifragilisticexpialidocious
def phonetic():
    word = input("What word do you need to spell out? ").lower()
    try:
        print([alphabet[letter] for letter in word])
    except KeyError:
        print("Numbers and Symbols are not a valid input.")
        phonetic()


phonetic()
