import random

def cardSetup():
    '''returns pyramid and stock pile'''
    deck = []
    pyramid = []
    stock = []
    for n in range(1,53):                                                       # creates the deck
        deck.append(n)
    random.shuffle(deck)
    pyramid = deck[0:28]                                                        # splits the deck into the two main chunks - pyramid and stock
    stock = deck[28:52]
    return pyramid,stock

def cardLogic(firstCard,secondCard):
    '''compares card selections'''
    firstComparison = firstCard
    secondComparison = secondCard
    if firstCard > 13:                                                          # these if and while statements take any card number 1-52 and compares them as 1-13 number
        firstComparison = firstCard - 13
        while firstComparison > 13:
            firstComparison -= 13
    if secondCard > 13:
        secondComparison = secondCard - 13
        while secondComparison > 13:
            secondComparison -= 13
    if firstComparison + secondComparison == 13:                                # if the cards add to 13 then the cards can then be moved to the foundation pile
        return "pass"
    else:
        return "fail"

def stockRotate(stock,waste):
    '''simulates card flip from stock to waste pile'''
    if len(waste) > 0:
        if waste[0] == "**":                                                    # prevents errors if the waste is just ** as that isn't an integer
            waste.pop()
    if len(stock) != 0:                                                         # adds the top stock card to the top of the waste if the stock isn't empty
        waste.insert(0, stock[0])
    if len(stock) >= 1 :
        for n in range(len(stock)-1):                                           # this removes the stock card that is now on top of the waste pile
            stock[n] = stock[n+1]
        stock.pop()
    else:
        for n in range(len(waste)):                                             # makes the stock pile the reverse of the waste pile when the stock empties
            stock.insert(0,waste[len(stock)-n])
            waste.pop(0)
        waste = ["**"]                                                          # resets the waste place value
    return stock,waste

def numberToCard(cardsToDisplay):
    '''turns card number of a deck to real cards names'''
    cardsToDisplay = cardsToDisplay
    if cardsToDisplay == []:
        cardsToDisplay.append("**")
    for n in range(len(cardsToDisplay)):                                        # uses numerical values to make unique cards based on the logic that each suit is a multiple of 13 above the last
        if cardsToDisplay[n] != "**":
            suit = "S"
            offset = 39
            if cardsToDisplay[n] <= 39:
                suit = "C"
                offset = 26
                if cardsToDisplay[n] <= 26:
                    suit = "H"
                    offset = 13
                    if cardsToDisplay[n] <=13 :
                        suit = "D"
                        offset = 0
            if cardsToDisplay[n] - offset == 13:                                # makes the name - suit cards
                cardsToDisplay[n] = "K" + suit
            elif cardsToDisplay[n] - offset == 12:
                cardsToDisplay[n] = "Q" + suit
            elif cardsToDisplay[n] - offset == 11:
                cardsToDisplay[n] = "J" + suit
            elif cardsToDisplay[n] - offset == 1:
                cardsToDisplay[n] = "A" + suit
            else:
                cardsToDisplay[n] = str(cardsToDisplay[n] - offset) + suit      # makes the number - suit cards
    return cardsToDisplay

def cardToNumber(card):
    '''turns a real card back into a number from 1-52'''
    if card[0] == "A":                                                          # does the opposite of the function above basically
        number = 1
    elif card[0] == "J":
        number = 11
    elif card[0] == "Q":
        number = 12
    elif card[0] == "K":
        number = 13
    else:
        number = int(card[0])                                                   # makes the value of the main card then adds it by the suit number
    suitIndex = 1
    if card[1] == "0":
        number = 10
        suitIndex = 2
    if card[suitIndex] == "D":
        suit = 0
    elif card[suitIndex] == "H":
        suit = 13
    elif card[suitIndex] == "C":
        suit = 26
    elif card[suitIndex] == "S":
        suit = 39
    cardNumber = number + suit
    return cardNumber

def validityCheck(card,pyramid,stock,waste,function):
    '''checks to see if the card option is valid'''
    testPass = "fail"
    rows = [pyramid[0],pyramid[1:3],pyramid[3:6],pyramid[6:10],pyramid[10:15],\
    pyramid[15:21],pyramid[21:28]]                                              # seperates the rows of cards into 7 rows
    cardAccess = []
    if len(stock) > 0:                                                          # len(stock) and len(waste) >0 prevent index errors
        if stock[0] != "**":
            cardAccess.append(stock[0])
    if len(waste) > 0:
        if waste[0] != "**":
            cardAccess.append(waste[0])
    for n in range(len(rows[6])):                                               # adds the 7th row to the accessible cards if they aren't **
        if rows[6][n] != "**":
            cardAccess.append(rows[6][n])
    for row in range(len(rows)-1):
        if row != 0:
            for n in range(len(rows[row])):                                     # adds any other number that has no other cards above it
                if rows[row+1][n] == "**" and rows[row+1][n+1] == "**":
                    if rows[row][n] != "**":
                        cardAccess.append(rows[row][n])
        else:
            if rows[1][0] == "**" and rows[1][1] == "**":
                cardAccess.append(rows[0])                                      # does the final check for the first row access - the for loop above can't check single values, just lists
    for n in range(len(cardAccess)):
        if card == cardAccess[n]:
            testPass = "pass"                                                   # passes avaliables cards from A-Q
            if card % 13 == 0:
                testPass = "king"                                               # passes kings and returns a value that lets them skip second card inputs so they are removed straight away
    if function == "cardAccess":                                                # returns the card access list for the endgame function to use
        return cardAccess
    else:
        return testPass

def removeCards(firstCard,secondCard,pyramid,stock,waste,foundation):
    '''moves cards from pyramid, stock or waste and adds them to foundation'''
    for n in range(len(pyramid)):                                               # checks all three card locations to find the cards to remove
        if pyramid[n] == firstCard or pyramid[n] == secondCard:
            foundation.append(pyramid[n])
            pyramid[n] = "**"                                                   # makes the pyramid empty card placeholder
    if len(stock) > 0:
        if stock[0] == firstCard or stock[0] == secondCard:
            foundation.append(stock[0])
            stock.pop(0)
    if len(waste) > 0:
        if waste[0] == firstCard or waste[0] == secondCard:
            foundation.append(waste[0])
            waste.pop(0)
    return pyramid,stock,waste,foundation

def refreshCards(pyramid,stock,waste):
    '''updates card display lists and display'''
    pcard,scard,wcard = pyramid[:],stock[:],waste[:]                            # copies the list to seperate lists so that the program lists stay as numbers
    numberToCard(pcard)
    numberToCard(scard)
    numberToCard(wcard)
    for n in range(20):                                                         # refreshes the screen and displays the pyramid
        print()
    print("      ",pcard[0])
    print("     ",pcard[1],pcard[2])
    print("    ",pcard[3],pcard[4],pcard[5])
    print("   ",pcard[6],pcard[7],pcard[8],pcard[9])
    print("  ",pcard[10],pcard[11],pcard[12],pcard[13],pcard[14])
    print(" ",pcard[15],pcard[16],pcard[17],pcard[18],pcard[19],pcard[20])
    print("",pcard[21],pcard[22],pcard[23],pcard[24],pcard[25],pcard[26],\
    pcard[27],"     ","Stock/Waste - ",scard[0],wcard[0])

def errorChecking(userInput,inputType):
    '''handles user inputs to prevent errors'''
    validCardsValues = ["1","2","3","4","5","6","7","8","9","A","J","Q","K"]    # creating the correct input strings
    validSuits = ["D","H","C","S"]
    if inputType == "menu":
        try:
            int(userInput)                                                      # prevents a value error if the user inputs a letter
        except ValueError:
            print("Use a numerical response")
            return "fail"
        if 0 < int(userInput) <= 3:                                             # prevents the user from inputting an erroneous menu error
            return "pass"
        else:
            print("Please choose a valid numerical option")
            return "fail"
    elif inputType == "cardChoice":
        length = True
        for n in range(0,2):
            try:
                userInput[n]                                                    # prevents the user from inputting an incorrect card name length
            except IndexError:
                length = False
        if length == True:
            for n in range(len(validCardsValues)):
                if userInput[0] == validCardsValues[n]:                         # checks to see if the user inputs the right card value
                    suitIndex = 1
                    if userInput[0] == "1":
                        suitIndex = 2
                        try:
                            userInput[2]
                        except IndexError:
                            length = False
                    if length == True:
                        for n in range(len(validSuits)):
                            if userInput[suitIndex] == validSuits[n]:           # checks if the user inputs the right suit names
                                return "pass"
        print("Invalid card name, try again")
        return "fail"

def cardSelection(pyramid,stock,waste,foundation):
    '''takes card input, validates, compares and removes valid cards'''
    validResponse = "fail"
    while validResponse == "fail":
        firstCard = input("Enter the valid card name, or go back (b) : ")       # collects the first card selection from the user
        firstCard = firstCard.upper()
        if firstCard == "B":
            print()
            return
        validResponse = errorChecking(firstCard,"cardChoice")
    firstCard = cardToNumber(firstCard)
    if validityCheck(firstCard,pyramid,stock,waste,"check") == "pass":
        validResponse = "fail"
        while validResponse == "fail":
            secondCard = input("Enter the second valid card to compare, or go \
back (b) : ")                                                                   # collects the second card from the user
            secondCard = secondCard.upper()
            if secondCard == "B":
                print()
                return
            validResponse = errorChecking(secondCard,"cardChoice")
        secondCard = cardToNumber(secondCard)
        if validityCheck(secondCard,pyramid,stock,waste,"check") == "pass":
            if cardLogic(firstCard,secondCard) == "pass":
                pyramid,stock,waste,foundation = removeCards(firstCard,\
                secondCard,pyramid,stock,waste,foundation)
    elif validityCheck(firstCard,pyramid,stock,waste,"check") == "king":
        pyramid,stock,waste,foundation = removeCards(firstCard,\
        "none",pyramid,stock,waste,foundation)
    print()

def endConditions(pyramid,stock,waste):
    '''checks to see if the game is completed or impossible to complete'''
    if len(stock) > 0:                                                          # sets up values to pass to validityCheck function
        emS = [stock[0]]
    else:
        emS = ["**"]
    if len(waste) > 0:
        emW = [waste[0]]
    else:
        emW = ["**"]
    pyramidAccess = validityCheck(0,pyramid,emS,emW,"cardAccess")               # makes the card access lists for this function
    pyramidAccess = pyramidAccess[2:]                                           # first two cards in pyramidAccess right now are the top of the stock and waste so they are removed
    cardAccess = validityCheck(0,pyramid,emS,emW,"cardAccess") + stock + waste  # makes a list of all accessible cards in game
    cardsToPop = []
    for n in range(len(cardAccess)):                                            # removes all of the card placeholders from the list if they exist
        if cardAccess[n] == "**":
            cardsToPop.append(n)
    if len(cardsToPop) > 0:
        for n in range(len(cardsToPop)):
            cardAccess.pop(cardsToPop[n])
    passCounter = 0
    for first in range(2,len(pyramidAccess)+2):                                 # checking valid pyramid cards with the stock and waste
        for second in range(len(cardAccess)):
            if cardLogic(cardAccess[first],cardAccess[second]) == "pass":
                passCounter += 1
    swCombinations = stock + waste
    for n in range(len(swCombinations)):
        if swCombinations[n] == "**":
            swCombinations.pop(n)
    for n in range(len(swCombinations)-1):                                      # checking to see if the stock and waste can make any final combinations
        if cardLogic(swCombinations[n],swCombinations[n+1]) == "pass":
            passCounter += 1
    if passCounter == 0:
        print("There are no more combinations!")
        return "end"                                                            # ends the game when the pyramid has cards left which can't be removed
    for n in range(len(pyramid)):
        if pyramid[n] != "**":
            return "continue"
        else:
            print("Well done! You removed the pyramid!")
            return "end"                                                        # ends the game when the pyramid is emptied

def scoring(pyramid,foundation):
    '''tracks the performance of the player'''
    rows = [pyramid[0],pyramid[1:3],pyramid[3:6],pyramid[6:10],pyramid[10:15],\
    pyramid[15:21],pyramid[21:28]]                                              # makes the card rows like in validityCheck function
    score = 0
    sortedPyramidCards = 0
    if pyramid[0] == "**":                                                      # adds score if the last pyramid card is removed
        score += 4200
        sortedPyramidCards += 1
    for row in range(1,len(rows)):                                              # adds score for the rest of the pyramid cards
        for card in range(len(rows[row])):
            scoreAddition = int(2100/row)
            if rows[row][card] == "**":
                score = score + scoreAddition
                sortedPyramidCards += 1
    for n in range(sortedPyramidCards, len(foundation)):                        # adds score for any extra cards not in the pyramid that removed (from stock/waste)
        score += 300
    print("Your score was: ",score)

def main():
    '''simulate regular program operation'''
    asciiArt = open("asciiArt.txt","r")
    print(asciiArt.read())                                                      # prints out the main title screen
    asciiArt.close()
    validResponse = "fail"
    while validResponse == "fail":
        choice  = input()
        validResponse = errorChecking(choice,"menu")
    choice  = int(choice)
    if choice == 2:
        information = open("rules.txt","r")
        print(information.read())                                               # prints the rules screen
        input()
    elif choice == 3:
        print("Closing game...")
        return
    endgame = "continue"
    waste = ["**"]
    pyramid,stock = cardSetup()
    foundation = []
    while endgame == "continue":
        refreshCards(pyramid,stock,waste)
        validResponse = "fail"
        while validResponse == "fail":
            print()
            choice = input("Choose: 1. Card Selection, 2. Stock Rotation, \
3. End Game : ")
            validResponse = errorChecking(choice,"menu")
        choice = int(choice)
        print()
        if choice == 1:
            cardSelection(pyramid,stock,waste,foundation)
            endgame = endConditions(pyramid,stock,waste)
        elif choice == 2:
            stock,waste = stockRotate(stock,waste)
            endgame = endConditions(pyramid,stock,waste)
        else:
            endgame = "end"
    scoring(pyramid,foundation)
    print()
    input("Press enter to end...")

main()
