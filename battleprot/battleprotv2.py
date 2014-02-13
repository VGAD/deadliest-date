import cardv2
import sys

NONE = 0
ROCK = 1
PAPER = 2
SCISSORS = 3

card_queue = []

def doBattle(rounds=6):
    """
    Does a battle, essentially runs doRound as many times as you specified and then adds damage.
    """
    card_queue = []
    # whose turn is it? True = player 1's, False = player 2's
    p1Play = True

    # player healths
    player1 = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    player2 = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

    # rounds loop.
    for i in range(rounds):
        # print whose turn it is
        print("{}'s attack".format("player 1" if p1Play else "player 2"))
        # run a round
        dmgtoE = doRound()
        print("Damage to enemy: {}".format(dmgtoE))
        
        for row in range(len(player1)):
            for cell in range(len(player1[row])):
                if p1Play:
                    player2[row][cell] -= dmgtoE[row][cell]
                else:
                    player1[row][cell] -= dmgtoE[row][cell]

        # print out current health of players.
        print("----P1----")
        for row in range(3):
            print(player1[row])
        print("--------")
        print("----P2----")
        for row in range(3):
            print(player2[row])
        print("--------")
        # switch turns
        p1Play = not p1Play

def doRound():
    """
    Runs rounds.
    Essentially just asks for two cards then returns the damage values of the overlayed cards in a list of lists.
    """
    if not card_queue:
        card_queue.append(parseCard(prefix="first "))
        
    card_queue.append(parseCard(prefix="play "))

    atk_card = card_queue.pop(0)
    def_card = card_queue.pop(0)
    # return the overlayed result
    (dmgtoE, new_card) = atk_card.overlay(def_card)
    card_queue.append(new_card)
    print("New card: {}".format(new_card))
    return dmgtoE

def parseCard(prefix=""):
    """
    Takes input for cards from standard in and requests each value to be parsed.
    (THIS MIGHT MAKE IT EXTENSIBLE INTO READING FROM FILES YAY)
    """
    cardData = []
    # take input from lines, split on spaces, parse each input, append to a new list, then append to the card list
    # (LIST COMPREHENSION IS FUN AND STUFF)
    cardData.append([parseInput(i) for i in input("{}line 1: ".format(prefix)).split(" ")])
    cardData.append([parseInput(i) for i in input("{}line 2: ".format(prefix)).split(" ")])
    cardData.append([parseInput(i) for i in input("{}line 3: ".format(prefix)).split(" ")])
    rv = cardv2.Card(None, cardData)
    print(rv)
    return rv

def parseInput(char):
    """
    Parse input chars into constants.
    """
    if char == 'p':
        return PAPER
    elif char == 'r':
        return ROCK
    elif char == 's':
        return SCISSORS
    else:
        return NONE

if __name__ == "__main__":
    if len(sys.argv) > 1:
        doBattle(rounds=int(sys.argv[-1]))
    else:
        doBattle()
