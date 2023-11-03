#type: ignore

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ': '/', 
    '!': '-.-.--'}  #dictionary for morse code translations

while True:
    message = input("Your message: ").upper() #ask for input and convert it to uppercase so dictionary can read it 

    translate = "" #create empty translation

    if "-Q" in message: #exit script if "-Q" is in the message
        break

    for letter in range(len(message)): #for every letter in the message 
        translate += MORSE_CODE[message[letter]] + " " #translate letter and move to the next one 
    print (f"My translation: {translate}") #print translation
        
    