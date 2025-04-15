import random

#Create the original deck with two loops to add each number to a corresponding suit to an array.
def createDeck():
    suitArray = ["C", "D", "H", "S"]
    rankArray = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    deckArray = []
    
    for suit in suitArray:
        for rank in rankArray:
            deckArray.append(suit+rank)
    return deckArray

#Shuffle the deck randomizing the card locations in the deck
def shuffleDeck(deck):
    shuffledDeck = []
    while deck:
        randomIndex = random.randint(0, len(deck) - 1)
        shuffledDeck.append(deck[randomIndex])
        deck.pop(randomIndex)
    return shuffledDeck
    

#Order the deck into different suits
def sortDeck(deck):
    
    suitArray = ["C", "D", "H", "S"]
    sortedByRanksArray = [[], [], [], []]
    
    #Order Suits by checking each cards "suit" if it is in the suitArray,
    #If it is, add it to the sorted arrays correct index that we get from indexing the suit's
    #in the suitArray
    for card in deck:
        if card[0] in suitArray:
            sortedByRanksArray[suitArray.index(card[0])].append(card)
            
    #Order cards
    return insertionDeckSort(sortedByRanksArray)


#Main sorting function
def insertionDeckSort(deckList):
    
    rankArray = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    
    #"Slice" the array into suits
    for numbersBySuit in deckList:
        
        #enumerate the shuffled array with same type of suits, partitioning it to a iterator and a card
        for iterator, card in enumerate(numbersBySuit):
            
            #As usual with insertion sort, start the sorting only after the first iteration to get the previous card to compare to
            if iterator > 0:
                
                #Get the current card, and a the previous card to compare the value to.
                currentCard = rankArray.index(numbersBySuit[iterator][1])
                previousCard = rankArray.index(numbersBySuit[iterator - 1][1])
                
                if currentCard < previousCard:
                    
                    #After we have established that the current card is indeed smaller than the previous card
                    #start searching for the correct index to the current card by comparing it to the previous card starting from the
                    #beginning of the array.
                            
                    for suitIterator in range((len(numbersBySuit) + iterator) - len(numbersBySuit)):
                        if currentCard < rankArray.index(numbersBySuit[suitIterator][1]):
                            numbersBySuit[suitIterator], numbersBySuit[iterator] = numbersBySuit[iterator], numbersBySuit[suitIterator]


    
    #Flatten the array
    return [card for sublist in deckList for card in sublist]

    #Original
    #return deckList
                    
            
newDeck = createDeck()
print(f"Original deck: {newDeck}",)
print("\n")

shuffledDeck = shuffleDeck(newDeck)
print(f"Shuffled deck: {shuffledDeck}")
print("\n")

sortedDeck = sortDeck(shuffledDeck)
print(f"Sorted deck: {sortedDeck}")
print("\n")
