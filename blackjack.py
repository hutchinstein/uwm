import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace']

game = False
aceExists = False
playerWins = False
playing = True
blackjack = False
playerDone = False
hitting = True

purse = 0
bet = 0

deck = []
playerHand = []
dealerHand = []


def createDeck():
    for suit in suits:
        for card in cards:
            newCard = card + " of " + suit
            deck.append(newCard)


def shuffle(myDeck):
    for i in range(0, len(myDeck)):
        randNum = random.randint(0, 51)
        randCard = deck[randNum]
        tempCard = myDeck[i]
        myDeck[i] = randCard
        myDeck[randNum] = tempCard


def cardValue(value):
    global aceExists
    if value == 'Two':
        return 2
    elif value == 'Three':
        return 3
    elif value == 'Four':
        return 4
    elif value == 'Five':
        return 5
    elif value == 'Six':
        return 6
    elif value == 'Seven':
        return 7
    elif value == 'Eight':
        return 8
    elif value == 'Nine':
        return 9
    elif value == 'Ace':
        aceExists = True
        return 1
    else:
        return 10


def dealCard(hand):
    nextCard = deck.pop(0)
    hand.append(nextCard)


def startGame():
    # print("startGame")
    global game, bet, purse
    createDeck()
    shuffle(deck)
    game = True
    print("You have $" + str(purse) + " in your purse")
    if purse == 0:
        addMoney = int(input("You do not have any money in your purse.\n"
              "Add more money here: "))
        purse = addMoney
    bet = input("How much would you like to bet? ")
    if int(bet) > int(purse):
        print("You do not have enough in your purse!")
        startGame()
    else:
        for i in range(0, 2):
            dealCard(dealerHand)
            dealCard(playerHand)


def showHands():
    if game:
        # print('Show hands')
        print("Dealer's hand: " + str(dealerHand))
        print("Player's hand: " + str(playerHand))
        showScore("Dealer's", dealerHand)
        showScore("Player's", playerHand)


def getScore(hand):
    # print('getScore')
    global aceExists
    score = 0
    for card in hand:
        value = card.split(' ')[0]
        score += cardValue(value)
    if aceExists:
        if score + 10 <= 21:
            score += 10
        aceExists = False
    return score


def showScore(player, hand):
    print(player, "score is: ", getScore(hand))


def checkScore():
    dealerScore = getScore(dealerHand)
    global game, playerWins, blackjack
    playerScore = getScore(playerHand)
    if playerScore > 21:
        print("You bust! You lose!")
        game = False
        playerWins = False
        betting()
    elif dealerScore == 21 and playerScore == 21:
        print("Tie, dealer wins!")
        playerWins = False
        betting()
        game = False
    elif dealerScore == 21 and playerScore != 21:
        if playerDone:
            print("Dealer wins")
            playerWins = False
            game = False
            betting()
        else:
            playerAction()
    elif playerScore == 21 and dealerScore != 21:
        print("Blackjack! You win!")
        playerWins = True
        blackjack = True
        game = False
        betting()
    elif dealerScore > 21:
        print("Dealer busts! You win!")
        playerWins = True
        game = False
        betting()
    if not hitting:
        #TODO game still ending while hitting
        #TODO move this to stay function?
        if dealerScore == playerScore:
            print("Tie, dealer wins!")
            playerWins = False
            betting()
            game = False


def stay(dealerScore, playerScore):
    # print("stay")
    global game, playerWins
    checkScore()
    global playerDone
    playerDone = True
    while dealerScore < playerScore and dealerScore < 21:
        dealCard(dealerHand)
        dealerScore = getScore(dealerHand)
    if playerScore < dealerScore <= 21:
        showHands()
        game = False
        playerWins = False
        betting()
    if dealerScore > 21:
        showHands()
        checkScore()
    if dealerScore == playerScore:
        showHands()
        checkScore()
        #playerScore = getScore(playerHand)


def playerAction():
    global game, playing, hitting
    # print("playerAction")
    response = input("Would you like to (h)it or s(tay)? ")
    response = response.lower()
    print("\n")
    if response == 'h':
        dealCard(playerHand)
        showHands()
        checkScore()
        if game:
            playerAction()
    elif response == 's':
        if game:
            hitting = False
            stay(getScore(dealerHand), getScore(playerHand))
            showHands()
            #checkScore()
    else:
        print("Invalid response")


def betting():
    # print("Betting")
    global bet, purse, blackjack, game
    if blackjack:
        bet = int(bet) * 1.50
    if playerWins:
        print("You won $" + str(bet))
        purse += int(bet)
        game = False
    if not playerWins:
        print("You lost $" + str(bet))
        purse = int(purse) - int(bet)
    blackjack = False


def main():
    global dealerHand, playerHand
    # print("Main")
    startGame()
    showHands()
    global game
    while game:
        playerAction()
    dealerHand = []
    playerHand = []

purse = float(input("How much do you want to put in your purse? "))
purse = round(purse, 2)

while playing:
    continuePlaying = input("Would you like to (c)ontinue playing or (q)uit?")
    if continuePlaying == "q":
        break
    main()
