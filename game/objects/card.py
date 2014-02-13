"""
Created on 2013-05-23

@author: Blake Bouchard
"""

class Card():
    """
    This class instantiates battle cards.
    """
    
    POSITIONS = ['topLeft', 'topCenter', 'topRight', 
                 'midLeft', 'midCenter', 'midRight',
                 'bottomLeft', 'bottomCenter', 'bottomRight']
    
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'
    
    def __init__(self, slots):
        """
        Constructor for the Card class.
        
        Takes an array of slots as its constructor
        """
    
        self._slots = {'topLeft' : None,
                       'topCenter' : None,
                       'topRight' : None,
                       'midLeft' : None,
                       'midCenter' : None,
                       'midRight' : None,
                       'bottomLeft' : None,
                       'bottomCenter' : None,
                       'bottomRight' : None }
        
        for key in slots.keys():
            self._slots[key] = slots[key]
    
    def compareCard(self, card):
        """
        Compare another card's slot values against the current card's slot values
        """
        
        if card.getSlotsLength() != 9:
            print("Card has incorrect number of _slots: " + len(card.slots))
        
        currentScore = 0
        
        for key in self._slots.keys():
            currentScore += self.compareSlot(self.getSlot(key), card.getSlot(key))
        
        return currentScore
        
    def compareSlot(self, selfSlot, enemySlot):
        """
        Returns 1 if self's slot wins over enemy's slot
        Returns -1 if enemy's slot wins over self's slot
        Returns 0 on stalemate
        """
        
        if selfSlot is None and enemySlot is not None:
            return -1
        elif selfSlot is not None and enemySlot is None:
            return 1
        elif selfSlot is enemySlot:
            return 0
        elif selfSlot is self.ROCK:
            if enemySlot is self.PAPER:
                return -1
            elif enemySlot is self.SCISSORS:
                return 1
            else: 
                return 0
        elif selfSlot is self.PAPER:
            if enemySlot is self.SCISSORS:
                return -1
            elif enemySlot is self.ROCK:
                return 1
            else:
                return 0
        elif selfSlot is self.SCISSORS:
            if enemySlot is self.ROCK:
                return -1
            elif enemySlot is self.PAPER:
                return 1
            else:
                return 0
        
    def getSlot(self, key):
        """
        Returns the value of the slot. Available keys are:
        
        topLeft    topCenter    topRight
        midLeft    midCenter    midRight
        bottomLeft bottomCenter bottomRight
        """
        
        return self._slots[key]
    
    def getSlotsLength(self):
        """
        Returns the number of slots in the slots array.
        """
        
        return len(self._slots)
    
    def setSlot(self, key, value):
        """
        Sets the slot at [key] to the value passed.
        """
        
        if key not in self._slots.keys():
            print("ERROR: Passed a bad key to setSlot: " + key + " : " + value)
            
        if value is self.ROCK:
            self._slots[key] = self.ROCK
        elif value is self.PAPER:
            self._slots[key] = self.PAPER
        elif value is self.SCISSORS:
            self._slots[key] = self.SCISSORS
        elif value is None:
            self._slots[key] = None
        else:
            print("ERROR: Passed a bad value to setSlot: " + value + " (with key: " + key + ").")
