from view.base_view import BaseView
from view.view_elements import button, view_card
from objects import card

import pygame

# Magic numbers
HAND_SIZE_LIMIT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_X_CENTER = SCREEN_WIDTH//2

CARD_DIM = 75
CARD_SPACE = 15

CARD_Y = 500

class BattleView(BaseView):
    """
    The battle view.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new battle view.
        """
        super().__init__(**kwargs)
        
        # Store the cards in your hand here
        self._hand = []
        self._cardElements = []

        # Has the hand been updated
        self._handUpdated = False
        
    def start(self):
        """
        """
        self.add_element(button.Button(
            'assets/view/battle/draw_card.png',
            hover_image = 'assets/view/battle/draw_card_hover.png',
            on_click = self.add_card,
            name = 'draw_card',
            pos = (0, 550)))

    def update(self):
        """
        Overrides BaseView update.
        """
        super().update()
        
        if self._handUpdated:
            
            # Create the view element for the card
            newCard = view_card.ViewCard(
                self._hand[-1],
                'assets/view/battle/grid75.png',
                'assets/view/battle/rock25.png',
                'assets/view/battle/scissors25.png',
                'assets/view/battle/paper25.png')
                
            # Add the element
            self.add_element(newCard)
            self._cardElements.append(newCard)
            
            # Set its y
            newCard.rect.y = CARD_Y
            
            # Recalculate the xs
            pos = -(len(self._hand) // 2)
            odd = len(self._hand) % 2
            
            for card in self._cardElements:
                newX = (pos * (CARD_DIM + CARD_SPACE))
                
                if not odd:
                    newX += ((CARD_DIM + CARD_SPACE)//2)
                
                newX += SCREEN_X_CENTER
                
                card.rect.x = newX
                pos += 1
            
            self._handUpdated = False
        
    def draw(self, screen):
        """
        Overrides BaseView update.
        """
        super().draw(screen)
        
    def add_card(self):
        """
        Adds a card to your hand.
        """
        if len(self._hand) >= HAND_SIZE_LIMIT:
            return
        # Create a new card here?
        newCard = randomCard()
        
        # Notify that the hand has been updated
        self._handUpdated = True
        
        # Add the card to the hand
        self._hand.append(newCard)
        
def randomCard():
    """
    Generates a random card for testing.
    """
    import random
    
    positions = card.Card.POSITIONS
    data = {}
    
    vals = {0: None, 1: card.Card.ROCK, 2: card.Card.SCISSORS,
            3: card.Card.PAPER}
    
    for pos in positions:
        data[pos] = vals[random.randint(0,3)]
        
    return card.Card(data)
