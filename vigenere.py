from helpers import alphabet_position, rotate_character

def encrypt():
    """Encrypt a message with a vigenere cypher"""
    text = str(input("Type a message: "))
    key = str(input("Encryption key: "))
    key_text = (key * int((len(text) / len(key)) + 1))[:len(text)]
    new_text = ""
    i_index = 0
    for i in text:
        if i.isalpha():
            new_text += rotate_character(i, alphabet_position(key_text[i_index]))
            i_index += 1
        else:
            new_text += i
    print(new_text)
    return new_text
