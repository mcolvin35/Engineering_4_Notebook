#type: ignore

import time
import digitalio
import board

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

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

while True:
    message = input("Your message: ").upper() #ask for input and convert it to uppercase so dictionary can read it 

    translate = "" #create empty translation

    if "-Q" in message: #exit script if "-Q" is in the message
        break

    for letter in range(len(message)): #for every letter in the message 
        translate += MORSE_CODE[message[letter]] + " " #translate letter and move to the next one 
    print (f"My translation: {translate}") #print translation
    
    for letter in translate: 
        if letter == ".":
            led.value = True
            time.sleep(dot_time)
            led.value = False
            time.sleep(dot_time)
        if letter == "-":
            led.value = True
            time.sleep(dash_time)
            led.value = False
            time.sleep(dot_time)
        if letter == " ":
            led.value = True
            time.sleep(between_letters)
            led.value = False
            time.sleep(dot_time)
        if letter == "/":
            led.value = True
            time.sleep(between_words)
            led.value = False    
            time.sleep(dot_time)