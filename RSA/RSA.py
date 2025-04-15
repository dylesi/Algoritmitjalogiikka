from carmichael import *
from congruence import *
from coprimes import *
from eulerstotient import *
from greatestcommondivisor import *

def RSA():
    pass

#First prime
p = 79
#Secondary prime
q = 89
#half prime? first half of key
n = p * q
# used to get private key
t = carmichael(n)
#public key
e = 295

def getd (d):
    while True:
        if congruence(d * e, 1, t):
            return d
            break
        else:
            d += 1
#private key
d = getd(1)

def cryptMessage(message, n, e):
    cryptresult = []
    
    for letter in message:
        cryptresult.append(ord(letter) ** e % n)
    return cryptresult

word = "Hello world!"
cryptedMessage = cryptMessage(word, n, e)

def decryptMessage(message, n, d):
    decryptresult = []

    for cryptedletter in message:
        decryptresult.append(chr(cryptedletter ** d % n))
    return decryptresult

decryptedmessage = decryptMessage(cryptedMessage, n, d)

print(f"Original message: {word}. Crypted word: {cryptedMessage} and decrypted message: {decryptedmessage}")