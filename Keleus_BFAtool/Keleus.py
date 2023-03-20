'''
**Keleus v1.0**

Brute force password cracking tool, full powered by Python
Scripted by Alessandro Barro (email: alessandro.b0906@gmail.com)

! Disclaimer !
This script has been coded for educational purpose only. Do not use this tool to damage, violate, outrage another person's privacy or the person itself. Do not attempt to violate the law with anything contained here. If you planned to use the tool for illegal purpose, then close this tool immediately! Alessandro Barro will not be responsible for your any illegal actions. The author of this material, or anyone else affiliated in any way, is not going to accept responsibility for your actions.
'''

#Prints
print("               _        _______  _        _______           _______ ")
print("              | \    /\(  ____ \( \      (  ____ \|\     /|(  ____ \ ")
print("              |  \  / /| (    \/| (      | (    \/| )   ( || (    \/")
print("              |  (_/ / | (__    | |      | (__    | |   | || (_____ ")
print("              |   _ (  |  __)   | |      |  __)   | |   | |(_____  )")
print("              |  ( \ \ | (      | |      | (      | |   | |      ) |")
print("              |  /  \ \| (____/\| (____/\| (____/\| (___) |/\____) |")
print("              |_/    \/(_______/(_______/(_______/(_______)\_______)")
print("       ")
print('                          "Dubium sapientiae initium."')
print("       ")
print("       ")
print("       ")
print("Brute force password cracking tool, full powered by Python")
print("Scripted by Alessandro Barro (email: alessandro.b0906@gmail.com)")
print("       ")
print("! Disclaimer !")
print("This script has been coded for educational purpose only. Do not use this tool to damage, violate, outrage another person's privacy or the person itself. Do not attempt to violate the law with anything contained here. If you planned to use the tool for illegal purpose, then close this tool immediately! Alessandro Barro will not be responsible for your any illegal actions. The author of this material, or anyone else affiliated in any way, is not going to accept responsibility for your actions.")
print("       ")
print("OS: Windows")
print("       ")
print("       ")
print("Settings")

#Modules
import itertools
from msilib.schema import SelfReg
import string
import time
from unicodedata import numeric
from pynput.mouse import Listener
from pynput.keyboard import Key, Controller

#Variables
#Variables - Definitors and counters
keyboard = Controller()
pressCounter = 1
exeTime = 0
attUpt = 0
#Variables - User settings
l = input("Insert the password lenght [n]: ")
l = int(l)
l += 1
sel1 = input("Include letters (uppercase) [y/n]: ")
sel2 = input("Include letters (lowercase) [y/n]: ")
sel3 = input("Include numbers [y/n]: ")
sel4 = input("Include punctation [y/n]: ")
sel5 = input("Insert delay (seconds): ")
sel6 = input("Insert known chars: ")
sel7 = input("Select position of the known chars [before/after/none]: ")
sel8 = input("Select generation input method [onclick]: ")
#Variables - Others
delay = int(sel5)
numericValue = string.digits
knownChars = sel6
selChars = sel7

#Functions
#Functions - passGuess() > The core function of the script, outputs all the possible combinations depending on the user settings and automatically types them wherever is possible (notepads, websites, shells)
def passGuess(real):
    start_time = time.time()
    chars1 = string.ascii_uppercase
    chars2 = string.ascii_lowercase
    chars3 = string.digits
    chars4 = string.punctuation
    chars5 = string.ascii_uppercase + string.ascii_lowercase
    chars6 = string.ascii_uppercase + string.digits
    chars7 = string.ascii_lowercase + string.digits
    chars8 = string.ascii_uppercase + string.punctuation
    chars9 = string.ascii_lowercase + string.punctuation
    chars10 = string.digits + string. punctuation
    chars11 = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    chars12 = string.ascii_uppercase + string.ascii_lowercase + string.digits
    chars13 = string.ascii_uppercase + string.digits + string.punctuation
    chars14 = string.ascii_lowercase + string.digits + string.punctuation
    chars15 = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    global attUpt
    global exeTime

    if selChars == "before":
        for password_length in range(1, l):
            global i
            if (sel1 == "y") and (sel2 == "n") and (sel3 == "n") and (sel4 == "n"):
                for guess in itertools.product(chars1, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars2, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars3, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars4, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars5, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars6, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars7, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars8, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars9, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars10, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars11, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars12, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars13, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars14, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars15, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(knownChars + guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(knownChars + guess, attUpt)
                    time.sleep(delay)
            else:
                print("Error, please restart the script")

    elif selChars == "after":
        for password_length in range(1, l):
            global i
            if (sel1 == "y") and (sel2 == "n") and (sel3 == "n") and (sel4 == "n"):
                for guess in itertools.product(chars1, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars2, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars3, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars4, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars5, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars6, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars7, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars8, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars9, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars10, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars11, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars12, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars13, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars14, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars15, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess + knownChars)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess + knownChars, attUpt)
                    time.sleep(delay)
            else:
                print("Error, please restart the script")
    
    elif selChars == "none":
         for password_length in range(1, l):
            global i
            if (sel1 == "y") and (sel2 == "n") and (sel3 == "n") and (sel4 == "n"):
                for guess in itertools.product(chars1, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars2, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars3, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars4, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars5, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars6, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars7, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars8, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars9, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars10, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars11, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars12, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars13, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars14, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars15, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            else:
                print("Error, please restart the script")
    
    else:
         for password_length in range(1, l):
            global i
            if (sel1 == "y") and (sel2 == "n") and (sel3 == "n") and (sel4 == "n"):
                for guess in itertools.product(chars1, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars2, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars3, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars4, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "n"):
                for guess in itertools.product(chars5, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars6, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars7, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars8, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars9, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars10, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "n")  and (sel4 == "y"):
                for guess in itertools.product(chars11, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "n"):
                for guess in itertools.product(chars12, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "n") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars13, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "n") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars14, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            elif (sel1 == "y") and (sel2 == "y") and (sel3 == "y")  and (sel4 == "y"):
                for guess in itertools.product(chars15, repeat=password_length):
                    attUpt += 1
                    guess = ''.join(guess)
                    exeTime = (time.time() - start_time)
                    keyboard.type(guess)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print(guess, attUpt)
                    time.sleep(delay)
            else:
                print("Error, please restart the script")
        

#Functions - __init__() > script initialization
def __init__():
    if sel8 == "onclick":
        print("Click anywhere to start cracking (the outputs will be automatically be typed into the application if possible)")

        with Listener(on_click = on_click) as listener:
            listener.join()

        on_click()
    else:
        print("Error please select a valid input method")
        print("Process is ended")

#Functions - on_click() > Makes possible to start passGuess() only where the user wishes
def on_click(x, y, button, pressed):
        global pressCounter
        if pressed and (pressCounter == 1):
            pressCounter += 1
            print(passGuess(""))
            log()
            exit()
        if not pressed:
            return False

#Functions - log() > Returns a report of the process
def log():
    print('Attempts: {} | Time: {} minutes'.format(attUpt, (exeTime / 60)))

#Functions - exit() > Reports to the user the end of the process
def exit():
        print("Process is ended")

__init__()