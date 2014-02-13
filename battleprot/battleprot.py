import card
import sys

NONE = 0
ROCK = 1
PAPER = 2
SCISSORS = 3

def doBattle(rounds=6):
    """
    Does a battle, essentially runs doRound as many times as you specified and then adds damage.
    """
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
        dmgtoE, dmgtoS = doRound()
        print("Damage to self: {}".format(dmgtoS))
        print("Damage to enemy: {}".format(dmgtoE))
        
        for row in range(len(player1)):
            for cell in range(len(player1[row])) and range(len(dmgtoS[row])):
                if p1Play:
                    player1[row][cell] -= dmgtoS[row][cell]
                    player2[row][cell] -= dmgtoE[row][cell]
                else:
                    player2[row][cell] -= dmgtoS[row][cell]
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
    # get two cards.
    playedCard = parseCard(prefix="played ")
    overlayCard = parseCard(prefix="overlay ")

    print(type(playedCard))
    # return the overlayed result
    return overlayCard.overlay(playedCard)

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
    rv = card.Card(None, cardData)
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
