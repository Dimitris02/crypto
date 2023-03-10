import hashlib as hl
from winsound import Beep as beep
from os import system
from random import randint

abc=' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςόύάέίήώ0123456789`!@#$%^&?*()_+=-|";:/,.~[]\'\\'   # Character list

def cls():            # Clear screen
    system('cls')

def pause():          # Pause
    system('pause')
    beep(1000,50)

def hash(text):       # Hash text
    return hl.sha256(text.encode()).hexdigest()

def find_in_abc(ch):           # Return  character's place in the character list
    return abc.find(ch)

def encode():
    global key                                                      # Import key
    beep(1000,50)
    cls()
    text=input('ENCODE: ')                                          # Read text

    text+=' '*randint(5,20)                                         # add a random number of spaces for extra ambiguity

    encoded_text=''                                                                    # Initialize encoded_text string
    for n,i in enumerate(text):                                                        # Iterate through the characters of the string
        encoded_text+=abc[(find_in_abc(i)+find_in_abc(key[n%len(key)]))%len(abc)]      # shift each character based on its corresponding key character (Vigenère cipher)
    
    print('\n'+encoded_text+'\n')
    pause()


def decode():
    global key                                               # Import key
    beep(1000,50)
    cls()
    text=input('DECODE: ')                                   # Read encoded text

    decoded_text=''                                          # Initialize decoded_text string
    for n,i in enumerate(text):                              # Iterate through the characters of the encoded string
        num=find_in_abc(i)-find_in_abc(key[n%len(key)])      # Undo character shift
        decoded_text+=abc[num%len(abc)]                      # shift each character based on its corresponding key character
    
    print('\n'+decoded_text+'\n')
    pause()


def menu():
    global key                            # Import key
    cls()
    print('1) Encode\n2) Decode\n')       # ╗
    ch=int(input('>'))                    # ╠ Pick Encode or Decode
    if ch==1: encode()                    # ║
    else: decode()                        # ╝
    menu()                                # Recursion


key=hash(input('KEY: '))        # Hash inputed private key
beep(1000,50)                   # Beep
menu()                          # Go to menu