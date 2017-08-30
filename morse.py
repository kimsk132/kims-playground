"""
Morse code 2-way translator.
Author: Pairode Jaroensri
Last visited: May 8, 2017
"""

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
         'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
         'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
         'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
         'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
         '.':'.-.-.-', ',':'--..--', '?':'..--..', '/':'-..-.',
         '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
         '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

def get_option():
    repeat = True
    while(repeat):
        print("Press 1 to translate from text --> Morse code.")
        print("Press 2 to translate from Morse code --> text.")
        a = input()
        if(a == '1' or a == '2'):
            repeat = False
            return a
        else:
            print("Invalid option. Please try again.")

def get_key(value):
    for k, v in morse.items():
        if v == value:
            return k

def encode(phrase):
    phrase = phrase.upper() + " "
    code = []
    coded_word = ""
    for char in phrase:
        if char != ' ':
            coded_word = coded_word + morse[char] + '/'
        else: #char == ' ':
            # Remove last character '/'
            corrected_word = coded_word[:-1]
            code.append(corrected_word)
            coded_word = ""

    return " ".join(code)


print("Welcome to Kim's Morse code translator V.2.10")
option = get_option()

if option == '1':
    phrase = input("Enter your phrase: ")
    try:
        print("Your Morse code is: " + encode(phrase))
    except Exception as e:
        print("Invalid character: " + str(e))

elif option == '2':
    print("Please enter in the following format:")
    print("This is an example: -/..../../... ../... .-/-. ./-..-/.-/--/.--./.-../.")
    code = input("Enter your Morse code here: ")
    words = []
    word = ""
    letter = ""
    for i in range(len(code)):
        if code[i] == '.' or code[i] == '-':
            letter = letter + code[i]
        elif code[i] == '/':
            letter = get_key(letter)
            word = word + letter
            letter = ""
        elif code[i] == ' ':
            letter = get_key(letter)
            word = word + letter
            words.append(word)
            word = ""
            letter = ""
        else:
            print("Invalid character.")

    letter = get_key(letter)
    word = word + letter
    words.append(word)
    word = ""
    letter = ""

    print("Your phrase is: " + " ".join(words))
