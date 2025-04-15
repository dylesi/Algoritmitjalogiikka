f = open("C:/Users/179492/git-repos/Algoritmitjalogiikka/encryption/sanat.txt", "r", encoding='utf-8')
lines = f.readlines()

muuttujoust = ""
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")


alphabet = [chr(x) for x in range(97, 123)] + ["å", "ä", "ö"]

def decode(word):
    returnstring = ""
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            for letter in word:
                if letter not in alphabet:
                    returnstring += letter
                else:
                    letterindex = alphabet.index(letter)
                    returnstring += alphabet[(letterindex - j + i) % len(alphabet)]
                # num += 5
            print(returnstring)
            returnstring = ""
   # return returnstring


print(decode("frxl, ujqe jkrelvr hqjxuv bqvqeqjblv"))
