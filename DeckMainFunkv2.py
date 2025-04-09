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
        for carditerator, card in enumerate(numbersBySuit):
            
            #start the sorting only after the first iteration to get the previous cards' value to compare to
            if carditerator > 0:
                
                #Start the loop to compare the cards, from the current cards position to the start of the index.
                for suitIterator in range(((len(numbersBySuit) + carditerator) - len(numbersBySuit)), 0, - 1):
                    
                    #Compare the current card with every other card before it untill the start of the index
                    #If a match has been found that the current card is smaller than the previous one, swap their values.
                    if rankArray.index(numbersBySuit[suitIterator][1]) < rankArray.index(numbersBySuit[suitIterator - 1][1]):
                        numbersBySuit[suitIterator], numbersBySuit[suitIterator - 1] = numbersBySuit[suitIterator - 1], numbersBySuit[suitIterator]
                            
    return [card for suitcardlist in deckList for card in suitcardlist]
                    
            
newDeck = createDeck()
print(f"Original deck: {newDeck}",)
print("\n")

shuffledDeck = shuffleDeck(newDeck)
print(f"Shuffled deck: {shuffledDeck}")
print("\n")

sortedDeck = sortDeck(shuffledDeck)
print(f"Sorted deck: {sortedDeck}")
print("\n")

