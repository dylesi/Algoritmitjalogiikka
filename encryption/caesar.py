alphabet = [chr(x) for x in range(97, 123)] + ["å", "ä", "ö"]


def caesar(key, word):
    resultWord = ""
    upperList = []
    for iter, char in enumerate(word):
        if char.isspace():
            resultWord += (" ")
        elif char.isupper():
            lowchar = char.swapcase()
            charIndex = alphabet.index(lowchar)
            resultWord += alphabet[charIndex - key % len(alphabet)].capitalize()
        elif char not in alphabet:
            resultWord += char
        else:
            charIndex = alphabet.index(char)
            resultWord += alphabet[charIndex - key % len(alphabet)]

    return resultWord


for i in range(len(alphabet)):

    print(caesar(i, "Tlmxkbq tgw Huxebq tkx vtimnkxw"))