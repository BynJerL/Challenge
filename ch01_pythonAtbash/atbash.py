# Python Atbash Cipher
import string

plainText = str(input("Input Plain Text: "))
cipherText = ""

for letter in plainText:
    if letter in string.ascii_uppercase:
        cipherText += chr(ord('Z') - (ord(letter) - ord('A')))
    elif letter in string.ascii_lowercase:
        cipherText += chr(ord('z') - (ord(letter) - ord('a')))
    elif letter in string.digits:
        cipherText += chr(ord('9') - (ord(letter) - ord('0')))
    else:
        cipherText += letter

print(f"Output Cipher Text: {cipherText}")