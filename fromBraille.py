# fromBraille.py: type in words using braille and sends the word to a discord channel

import keyboard
import time
import toBraille as tb
import sendDiscMessage as send
import getDiscMessage as receive
import discordConstants as dc

dots = [[0,0],[0,0],[0,0],[0,0]]
word = ""
content = ""

# returns the opposite binary value, 1 -> 0, 0 -> 1
def flip(b):
    if b == 0:
        return 1
    return 0

# returns the character equivalent of the entered braille matrix
def getLetter(dots):
    # if the entered matrix is empty, return a space ' '
    if dots == [[0,0],[0,0],[0,0],[0,0]]:
        return ' '
    for letter in tb.letterConstants:
        if tb.letterConstants.get(letter) == dots:
            return letter
    return ''

# infinite loop waiting for key presses
while True:
    # should later be changed to use a listener rather than if tests in an infinite loop to handle key presses

    # Enter key sends discord message
    if keyboard.is_pressed('Enter'):
        send.send_message(dc.channel, word)
        print('sent ', word)
        word = ""
        dots = [[0,0],[0,0],[0,0],[0,0]]
        # content = receive.retrieve_messages(dc.channel, content)
        time.sleep(0.1)

    # Space key moves on to next letter of string
    if keyboard.is_pressed('Space'):
        word += getLetter(dots)
        print(word)
        dots = [[0,0],[0,0],[0,0],[0,0]]
        time.sleep(0.1)

    # each of the following keys represents a dot position in a 4x2 braille matrix
    #   f-> 0 0 <-j
    #   d-> 0 0 <-k
    #   s-> 0 0 <-l
    #   a-> 0 0 <-;
    if keyboard.is_pressed('a'):
        dots[3][0] = flip(dots[3][0])
        print(dots)
        time.sleep(0.1)  
    if keyboard.is_pressed('s'):
        dots[2][0] = flip(dots[2][0])
        print(dots)
        time.sleep(0.1)
    if keyboard.is_pressed('d'):
        dots[1][0] = flip(dots[1][0])
        print(dots)
        time.sleep(0.5)  
    if keyboard.is_pressed('f'):
        dots[0][0] = flip(dots[0][0])
        print(dots)
        time.sleep(0.5)      
    if keyboard.is_pressed('j'):
        dots[0][1] = flip(dots[0][1])
        print(dots)
        time.sleep(0.5)    
    if keyboard.is_pressed('k'):
        dots[1][1] = flip(dots[1][1])
        print(dots)
        time.sleep(0.5)  
    if keyboard.is_pressed('l'):
        dots[2][1] = flip(dots[2][1])
        print(dots)
        time.sleep(0.5)  
    if keyboard.is_pressed(';'):
        dots[3][1] = flip(dots[3][1])
        print(dots)
        time.sleep(0.5)     

    # esc key ends the program                     
    if keyboard.is_pressed('esc'):
        break