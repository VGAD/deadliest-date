EMPTY = 0
ROCK = 1
PAPER = 2
SCIS = 3

class Card:
    """
    A class that encapsulates everything associated with a card in the combat system.
    Contains relevant data and methods for your ease of use.
    
        Private Data:
            _data   -> the slots of the cards, RPS
            _id     -> the id number of the card

        Public Class methods:
            getId()     -> gets the card's ID number
            getData()   -> gets the card's data.
            overlay()   -> calculates resulting damage from a card being played on this one.
            
        Private Module Methods:
            _RPS(played, counter)   -> calculates the damage for a played cell
            _cRPS(counter, played)  -> calculates the damage for a counter cell
    """
    
    def __init__(self, idnum, data):
        """
        Inititialzies a new card with a specified ID number and
        with specified data.
        """
        self._id = idnum
        self._data = data

    def __repr__(self):
        """
        Returns a string representation of this card.
        Has the form:
            Card(ID: <idnum>, Data: [[x, x, x], [x, x, x], [x, x, x]])
        """
        parsedData = []
        for row in range(len(self._data)):
            parsedData.append([])
            for cell in range(len(self._data[row])):
                val = self._data[row][cell]
                if val == EMPTY:
                    parsedData[row].append("0")
                elif val == ROCK:
                    parsedData[row].append("R")
                elif val == PAPER:
                    parsedData[row].append("P")
                elif val == SCIS:
                    parsedData[row].append("S")
        return "Card(ID: {}, Data: {})".format(self._id, parsedData)

    def getId(self):
        """
        Gets this card's id.
        """
        return self._id

    def getData(self):
        return self._data

    def overlay(self, card):
        """
        Overlays the OTHER card ON THIS ONE.

        Returns (damageToEnemy, damageToSelf)
        Where each entry is a list of three lists of three values,
        each value being how much damage was done to that part of
        the respective players body.
        Self is considered to be the person playing the first card.
        Enemy is considered to be the person playing the overlay card.
        """
        #These are the return values
        dmgtoE = []

        #get the opposing card's data
        ocData = card.getData()
        for row in range(len(self._data)):
            #append the next row
            dmgtoE.append([])
            for cell in range(len(self._data[row])):
                #append the calculated damage to each row
                dmgtoE[row].append(_RPS(self._data[row][cell], ocData[row][cell]))
        rc =[[], [], []]
        print(dmgtoE)
        print(ocData)
        for i in range(3):
            for j in range(3):
                if (not dmgtoE[i][j] and
                    self._data[i][j] != ocData[i][j]):
                    rc[i].append(ocData[i][j])
                else:
                    rc[i].append(EMPTY)
        rc = Card(None, rc)
                    
        return (dmgtoE, rc)

def _RPS(played, counter):
    """
    Compares two values and returns the damage that results from the play.
    This is only for comparing attacking card -> counter
    """
    #if the played was empty there's no hope of causing damage
    if played == EMPTY:
        return 0
    #From here down,
    #if counter is a loss to played then 2 damage dealt
    #if counter is EMPTY then 1 damage dealt
    #if counter is the same or a win to played, then no damage dealt
    elif played == ROCK:
        if counter == SCIS: return 2
        elif counter == EMPTY: return 1
        else: return 0
    elif played == PAPER:
        if counter == ROCK: return 2
        elif counter == EMPTY: return 1
        else: return 0
    elif played == SCIS:
        if counter == PAPER: return 2
        elif counter == EMPTY: return 1
        else: return 0

