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
dot_time = 1*modifier #dot time is 0.25 seconds
dash_time = 3*modifier #dash time is 0.75 
between_taps = 1*modifier #time between characters in one letter
between_letters = 3*modifier #time between letters
between_words = 7*modifier #time between words

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
    
    for letter in translate: #for every character in the translated message
        if letter == ".": #if the character is a dot
            led.value = True #turn LED on 
            time.sleep(dot_time) #wait for 0.25secs
            led.value = False #turn LED off
            time.sleep(between_taps) #wait 0.25 secs
        if letter == "-":
            led.value = True
            time.sleep(dash_time)
            led.value = False
            time.sleep(between_taps)
        if letter == " ":
            led.value = True
            time.sleep(between_letters)
            led.value = False
            time.sleep(between_taps)
        if letter == "/":
            led.value = True
            time.sleep(between_words)
            led.value = False    
            time.sleep(between_taps)