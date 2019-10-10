import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
faces = ['Ace', 'King', 'Queen', 'Jack']
deck = []
for suit in suits:
    for num in range(2, 11):
        card = str(num) + " of " + suit
        deck.append(card)

for suit in suits:
    for face in faces:
        card = face + " of " + suit
        deck.append(card)

listlen = len(deck)
dealt = []


class Hand:
    def __init__(self, name):
        self.name = name

    def deal(self):
        counter = 2
        hand = []
        total = 0
        # print(self.name)
        while total < 5:
            a = random.randint(0, listlen - counter)
            dealtcard = deck[a]
            if dealtcard not in dealt:
                # print(dealtcard)
                dealt.append(dealtcard)
                hand.append(dealtcard)
                total += 1
            else:
                # print(dealtcard + " WAS ALREADY dealt")
                pass
        print(self.name, hand)
        return(hand)

    def score(self, cards):
        score = 0
        for i in cards:
            print(i[:4])
            if str(i[:4]) == "Jack" or "Quee" or "King":
                print("Face card ", i)
            elif int(i[:2]) > 0:
                print("Number card ", i)
        print(self.name + " has a score of " + str(score))

johnsHand = Hand("John")
johnscards = johnsHand.deal()
johnsHand.score(johnscards)
# for i in johnscards:
#     print(i)
#     try:
#         if int(i[:2]) > 0:
#             print(i[:2])
#     except:
#         print("Face card")
blairsHand = Hand("Blair")
blairsHand.deal()
charliesHand = Hand("Charlie")
charliesHand.deal()
mishaksHand = Hand("Mishka")
mishaksHand.deal()
dealersHand = Hand("Dealer")
dealersHand.deal()

# print(deck)