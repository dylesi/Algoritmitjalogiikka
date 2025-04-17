djik = open("pathalgos/djikstradata.txt", "r")
lines = djik.readlines()

for line in lines:
    line = " ".join(line.split())
    line = line.split(" ")
    for i in range(len(line)):
        line[i] = line[i].split(",")

    for k in range(1, len(line)):
        line[k] = {line[k][0]: line[k][1]}
print(line)