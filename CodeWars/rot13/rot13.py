# simple letter substitution cipher that replaces a letter with the letter
def rot13(message):
    dif = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghJjklm")

    after_rot13 = message.translate(dif)

    return after_rot13