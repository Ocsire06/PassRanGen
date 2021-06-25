# PassRanGen / PRG 1.0

# Library import

import time
import os
import platform
import random

# Clear define 

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# Oobe define

def oobe():
    print('Welcome to PassRanGen Navzard. (Version 1.0)')
    time.sleep(2)
    print('Please navigate using the keys below.')
    print("'r' to run the program.")
    print("'q' to quit the program.")
    print("")
    print('Please refer to readme.txt before using this program.')

    nav = input('> ')

    if nav == 'r':
        clear()
        print('Loading pre-requisites...')
        time.sleep(2)
        print('Loading libraries...')
        time.sleep(2)
        print('Validating...')
        time.sleep(1)
        print('Almost done...')
        time.sleep(1)
        clear()
        prg()
    elif nav == 'q':
        clear()
        print('Thank you for using PassRanGen. See you soon! [Quitting in 3...]')
        time.sleep(3)
        exit()

# PRG define

def prg():
    print('Good day user. Welcome to PassRanGen.')
    print('It is time to generate a password!')
    print('')
    time.sleep(1)

    passlen = int(input("What should be the length of your password? [NOTE: Do not enter comically large numbers.] > "))
    sym = input("Should it contain symbols (y/n)? > ")

    if sym == 'y':
        print('Okay, including symbols.')
        s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*"
        clear()
        print('Generating your super-secure password...')
        time.sleep(2)
        p = "".join(random.sample(s,passlen ))
        print('Your password should be: ' , p)
        print('')
        hp = input('Return to the homepage (y/n)? > ')

        if hp == 'y':
            clear()
            prg()
        elif hp == 'n':
            clear()
            print('Thanks for using! Quitting in 3...')
            time.sleep(3)
            exit()
        else:
            print('WARNING: Unexpected Input. Ending program...')
            time.sleep(3)
            exit()
        

    elif sym == 'n':
        print('Okay, excluding symbols.')
        s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        clear()
        print('Generating your super-secure password...')
        time.sleep(2)
        p = "".join(random.sample(s,passlen ))
        print('Your password should be: ' , p)
        print('')
        hp = input('Return to the homepage (y/n)? > ')

        if hp == 'y':
            clear()
            prg()
        elif hp == 'n':
            clear()
            print('Thanks for using! Quitting in 3...')
            time.sleep(3)
            exit()
        else:
            print('WARNING: Unexpected Input. Ending program...')
            time.sleep(3)
            exit()

    else:
        print('WARNING: Unexpected Input. Ending program...')
        time.sleep(3)
        exit()





oobe()