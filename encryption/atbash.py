alphabet = [chr(x) for x in range(97, 123)] + ["å", "ä", "ö"]

def Atbash(word):
    encryptedWord = ""
    word = word.lower()
    for letter in word:
        if letter not in alphabet:
            encryptedWord += letter
        else:
            letterIndex = alphabet.index(letter)
            encryptedWord += alphabet[len(alphabet) - 1 - letterIndex]
    return encryptedWord

print(Atbash("Jbqp oru huuqyupyp öjäökv völtoujik"))
