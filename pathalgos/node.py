class Node:
    def __init__ (self, name, connections):
        self.name = name
        self.connections = connections
        self.value = None
        self.explored = False

    def __str__ (self):
        return(f"name: {self.name}. Connections: {self.connections}. Value: {self.value}")


nodelist = []
nodelist.append(Node("A", {"F": 2, "C": 3})) 
nodelist.append(Node("C", {"A": 3, "E": 1, "D": 4}))
nodelist.append(Node("F", {"A": 2, "C": 2, "E": 3, "G": 5})) 
nodelist.append(Node("E", {"F": 3, "C": 1, "B": 2}))
nodelist.append(Node("D", {"C": 4, "B": 1}))
nodelist.append(Node("B", {"D": 1, "E": 2, "G": 2, "F": 6})) 
nodelist.append(Node("G", {"F": 5, "B": 1}))

for node in nodelist:
    print(node.connections)

if __name__ == "__main__":

    djik = open("pathalgos/djikstradata.txt", "r")
    lines = djik.readlines()

    for line in lines:
        line = " ".join(line.split())
        line = line.split(" ")


