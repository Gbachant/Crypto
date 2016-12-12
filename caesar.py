from helpers import alphabet_position, rotate_character
from sys import argv, exit

def user_function_is_valid(cl_args):
    if len(cl_args) == 2 and type(cl_args[1]) is int:
        return True
    else:
        print("usage: python3 caesar.py n")
        return False
        exit()

def encrypt():
    """Switch all characters for new characters a specified distance away"""
    text = str(input("Type a message: "))
    rot = int(argv[1])
    new_text = ""
    for i in text:
        new_text += str(rotate_character(i, rot))
    print(new_text)
    return new_text
