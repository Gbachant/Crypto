import string
upper = []
lower = []
for i in string.ascii_uppercase:
    upper.append(i)
for i in string.ascii_lowercase:
    lower.append(i)

def alphabet_position(letter):
    """Determine what position a letter has in the alphabet"""
    if letter.isupper():
        return upper.index(letter)
    elif letter.islower():
        return lower.index(letter)

def rotate_character(char, rot):
    """Switch the character for a new character a specified distance away"""
    if char.isupper():
        return upper[((upper.index(char) + int(rot)) % 26)]
    elif char.islower():
        return lower[((lower.index(char) + int(rot)) % 26)]
    else:
        return char
