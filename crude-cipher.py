# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def is_letter(letter):
    k = ord(letter)

    # Assume it's a letter, unless it meets some fiddly conditions
    isr = True

    # These are the fiddly conditions
    if k < 65:
        isr = False
    if k > 122:
        isr = False
    if k < 97:
        if k > 90:
            isr = False

    return isr


def shift_letter(letter,s):
    # Assume it's lowercase ...
    lowercase = True

    k = ord(letter)

    # ... but check that
    if k < 97:
:        lowercase = False

    # Assign the letter a number from 1 to 26 (well, from 0 to 25)
    if lowercase:
        k = k - 97
    else:
        k = k - 65

    # The actual Caesar shift
    k = (k + s) % 26

    # Take it back to its place in ASCII
    if lowercase:
        k = k + 97
    else:
        k = k + 65

    letter = chr(k)
    return letter


def CaesarShift(ciph,s):

    # Placeholder for plaintext
    plaintemp = ""

    # Do this character by character
    for c in range(len(ciph)):

        # If the character is a letter, shift it by s
        if is_letter(ciph[c]):
            plaintemp = plaintemp + shift_letter(ciph[c],s)

        # If the character is not a letter, just replicate it as-is
        else:
            plaintemp = plaintemp + ciph[c]
    return plaintemp


if __name__ == '__main__':
    # Demonstration simply cycles through all the letters and outputs each one
    for j in range (26):
        plain = "A = " + chr(j+65) + ": "

        # This ciphertext is from https://uploads.guim.co.uk/2020/12/03/Genius210.pdf

        plain = plain + CaesarShift("Tjyuffo tpmvujpot nvtu cf fodjqifsfe cfgpsf fousz jo uif hsje. Pof pg uiftf fousjft jt jojujbmmz bo bccsfwjbujpo.", j)
        print(plain)