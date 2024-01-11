# 9.3.2023
#
# Morse code interpreter using implicit binary tree
#
#
# ! COMMENTS NOT FINISHED



                                # A node in the Morse tree has:
                                #
                                # alpha, the letter which it is
                                # dash: where in the tree it points if the next code character is dash
                                # dot: likewise if next is dot
class node:
    def __init__(self, alpha, dash, dot):
        self.alpha = alpha
        self.dash = dash
        self.dot = dot


                                # Table of characters which the interpreter will accept; anything else will be ignored
valid_inputs = [".","-"," ","/"]

                                # Implicit tree of Morse code, line by line
MorseTree = []
MorseTree.append(node(None,1,2))        # Begin with "no character", pointing to T or E depending on first input character

MorseTree.append(node("T",3,4))         # From here it branches, 2 each
MorseTree.append(node("E",5,6))

MorseTree.append(node("M",7,8))
MorseTree.append(node("N",9,10))
MorseTree.append(node("A",11,12))
MorseTree.append(node("I",13,14))

MorseTree.append(node("O",15,16))       # More branches
MorseTree.append(node("G",17,18))
MorseTree.append(node("K",19,20))
MorseTree.append(node("D",21,22))
MorseTree.append(node("W",23,24))
MorseTree.append(node("R",25,26))
MorseTree.append(node("U",27,28))
MorseTree.append(node("S",29,30))

MorseTree.append(node(None,None,None))  # Not every node in the tree contains a character
MorseTree.append(node(None,None,None))
MorseTree.append(node("Q",None,None))   # And in this fourth layer, almost all letters go nowhere next
MorseTree.append(node("Z",None,None))   # In the fifth (sixth?) layer are punctuation numbers etc but I have
MorseTree.append(node("Y",None,None))   # limited this one to just letters
MorseTree.append(node("C",None,None))
MorseTree.append(node("X",None,None))
MorseTree.append(node("B",None,None))
MorseTree.append(node("J",None,None))
MorseTree.append(node("P",None,None))
MorseTree.append(node(None,None,None))
MorseTree.append(node("L",None,None))
MorseTree.append(node(None,None,None))
MorseTree.append(node("F",None,None))
MorseTree.append(node("V",None,None))
MorseTree.append(node("H",None,None))


                            # Method takes an input string of Morse code, and a width parameter to set line lengths for readability
def Morse_decode(dotdash,width):
                            # Into this variable will go the decoded string
    plaintext = ""
                            # This variable will count the characters before a new-line is triggered
    line_length = 0

                            # Use the space character to separate the more code into individual letters (and slashes)
    message_list = dotdash.split(" ")

    for k in range(len(message_list)):
        line_length += 1
        ch = message_list[k]
                            # As long as the next "letter" isn't a slash...
        if ch != "/":
                            # get it translated into the alphabet
            plaintext = plaintext + get_alpha(ch)
        else:
                            # But if it IS a slash, output a space because slash means new word
            plaintext = plaintext + " "
                            # This bit triggers a newline if the width has been reached
            if line_length > width:
                plaintext = plaintext + "\n"
                line_length = 0

    return plaintext

def get_alpha(code):
    k = len(code)

    alpha = ""

    tree_pos = 0

    for j in range(k):

        if code[j] == "-":
            dash = MorseTree[tree_pos].dash
            if dash:
                tree_pos = dash
        if code[j] == ".":
            dot = MorseTree[tree_pos].dot
            if dot:
                tree_pos = dot

    alpha = MorseTree[tree_pos].alpha

    if not alpha:
        alpha = ""
    if len(code) > 4:
        alpha = ""

    return alpha



def clean_up(message):
    mess_length = len(message)
    k = 0
    while k < mess_length:
        if valid_inputs.count(message[k]) == 0:
            message = message.replace(message[k],"",1)
            k = k
        else:
            k += 1
        mess_length = len(message)


    return message





if __name__ == "__main__":

    message = "-.-. .-163 .-.. .-.. / -- . / .. ... .98tresrdt678ui... -- .- . .-.. .-.-.- / ... --- -- . / -.-- . .- .-. ... / .- --. --- --..-- / -. . ...- . .-. / -- .. -. -.. / .... --- .-- / .-.. --- -. --. / .--. .-. . -.-. .. ... . .-.. -.-- --..-- / .... .- ...- .. -. --. / .-.. .. - - .-.. . / --- .-. / -. --- / -- --- -. . -.-- / .. -. / -- -.-- / .--. ..- .-. ... . --..-- / .- -. -.. / -. --- - .... .. -. --. / .--. .- .-. - .. -.-. ..- .-.. .- .-. / - --- / .. -. - . .-. . ... - / -- . / --- -. / ... .... --- .-. . --..-- / .. / - .... --- ..- --. .... - / .. / .-- --- ..- .-.. -.. / ... .- .. .-.. / .- -... --- ..- - / .- / .-.. .. - - .-.. . / .- -. -.. / ... . . / - .... . / .-- .- - . .-. -.-- / .--. .- .-. - / --- ..-. / - .... . / .-- --- .-. .-.. -.. .-.-.- / .. - / .. ... / .- / .-- .- -.-- / .. / .... .- ...- . / --- ..-. / -.. .-. .. ...- .. -. --. / --- ..-. ..-. / - .... . / ... .--. .-.. . . -. / .- -. -.. / .-. . --. ..- .-.. .- - .. -. --. / - .... . / -.-. .. .-. -.-. ..- .-.. .- - .. --- -. .-.-.- / .-- .... . -. . ...- . .-. / .. / ..-. .. -. -.. / -- -.-- ... . .-.. ..-. / --. .-. --- .-- .. -. --. / --. .-. .. -- / .- -... --- ..- - / - .... . / -- --- ..- - .... --..-- / .-- .... . -. . ...- . .-. / .. - / .. ... / .- / -.. .- -- .--. --..-- / -.. .-. .. --.. --.. .-.. -.-- / -. --- ...- . -- -... . .-. / .. -. / -- -.-- / ... --- ..- .-.. --..-- / .-- .... . -. . ...- . .-. / .. / ..-. .. -. -.. / -- -.-- ... . .-.. ..-. / .. -. ...- --- .-.. ..- -. - .- .-. .. .-.. -.-- / .--. .- ..- ... .. -. --. / -... . ..-. --- .-. . / -.-. --- ..-. ..-. .. -. / .-- .- .-. . .... --- ..- ... . ... --..-- / .- -. -.. / -... .-. .. -. --. .. -. --. / ..- .--. / - .... . / .-. . .- .-. / --- ..-. / . ...- . .-. -.-- / ..-. ..- -. . .-. .- .-.. / .. / -- . . - --..-- / .- -. -.. / . ... .--. . -.-. .. .- .-.. .-.. -.-- / .-- .... . -. . ...- . .-. / -- -.-- / .... -.-- .--. --- ... / --. . - / ... ..- -.-. .... / .- -. / ..- .--. .--. . .-. / .... .- -. -.. / --- ..-. / -- . --..-- / - .... .- - / .. - / .-. . --.- ..- .. .-. . ... / .- / ... - .-. --- -. --. / -- --- .-. .- .-.. / .--. .-. .. -. -.-. .. .--. .-.. . / - --- / .--. .-. . ...- . -. - / -- . / ..-. .-. --- -- / -.. . .-.. .. -... . .-. .- - . .-.. -.-- / ... - . .--. .--. .. -. --. / .. -. - --- / - .... . / ... - .-. . . - --..-- / .- -. -.. / -- . - .... --- -.. .. -.-. .- .-.. .-.. -.-- / -.- -. --- -.-. -.- .. -. --. / .--. . --- .--. .-.. . .-..-. ... / .... .- - ... / --- ..-. ..-. --..-- / - .... . -. --..-- / .. / .- -.-. -.-. --- ..- -. - / .. - / .... .. --. .... / - .. -- . / - --- / --. . - / - --- / ... . .- / .- ... / ... --- --- -. / .- ... / .. / -.-. .- -. .-.-.- / - .... .. ... / .. ... / -- -.-- / ... ..- -... ... - .. - ..- - . / ..-. --- .-. / .--. .. ... - --- .-.. / .- -. -.. / -... .- .-.. .-.. .-.-.- / .-- .. - .... / .- / .--. .... .. .-.. --- ... --- .--. .... .. -.-. .- .-.. / ..-. .-.. --- ..- .-. .. ... .... / -.-. .- - --- / - .... .-. --- .-- ... / .... .. -- ... . .-.. ..-. / ..- .--. --- -. / .... .. ... / ... .-- --- .-. -.. --..-- / .. / --.- ..- .. . - .-.. -.-- / - .- -.- . / - --- / - .... . / ... .... .. .--. .-.-.- / - .... . .-. . / .. ... / -. --- - .... .. -. --. / ... ..- .-. .--. .-. .. ... .. -. --. / .. -. / - .... .. ... .-.-.- / .. ..-. / - .... . -.-- / -... ..- - / -.- -. . .-- / .. - --..-- / .- .-.. -- --- ... - / .- .-.. .-.. / -- . -. / .. -. / - .... . .. .-. / -.. . --. .-. . . --..-- / ... --- -- . / - .. -- . / --- .-. / --- - .... . .-. --..-- / -.-. .... . .-. .. ... .... / ...- . .-. -.-- / -. . .- .-. .-.. -.-- / - .... . / ... .- -- . / ..-. . . .-.. .. -. --. ... / - --- .-- .- .-. -.. ... / - .... . / --- -.-. . .- -. / .-- .. - .... / -- . .-.-.-"

    message = clean_up(message)

    message = Morse_decode(message,73)

    print(message)
