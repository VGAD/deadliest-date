import pygame

import helper
from view.view_elements.view_element import ViewElement
from objects import card


class ViewCard(ViewElement):
    """
    A view element which renders a card.
    """
    def __init__(self, cardData, gridImg,
                 oImg, xImg, iImg,
                 name=None, pos=None,
                 **kwargs):
        """
        Initializes ViewCard.
        Takes cardData to render from.
        Take gridImg as background and o/x/iImg as RPS symbols.
        Optional pos argument is (x, y) tuple defining the top left
        corner to render at.
        Optional name argument for the name of the element
        """
        # Load the grid image
        if gridImg:
            self._gridImg = helper.load_image(gridImg)
        else:
            raise AssertionError('Missing background for ViewCard.')
        
        # Set the rectangle accordingly
        temp_rect = self._gridImg.get_rect()
        
        # Move the rectangle to the desired position
        if pos:
            temp_rect.move_ip(*pos)
        
        super().__init__(name=name, rect=temp_rect, **kwargs)
        
        # Save the card data, raise error if none
        if cardData:
            self._cardData = cardData
        else:
            raise AssertionError('Missing card data for ViewCard.')
        
        # Load the symbol images
        if oImg and xImg and iImg:
            self._oImg = helper.load_image(oImg)
            self._xImg = helper.load_image(xImg)
            self._iImg = helper.load_image(iImg)
            if (self._oImg.get_width() ==
                self._xImg.get_width() ==
                self._iImg.get_width()):
                    self._symbolSize = self._oImg.get_width()
            else:
                raise AssertionError('Symbol sizes don\'t match.')
        else:
            raise AssertionError('Missing RPS symbols for ViewCard.')
            
        # Finally, update our image
        self.update()
        
    
    def update(self):
        """
        Renders the card and its items in the proper location on the card's grid
        """
        #rendering the grid
        self.image = self._gridImg
        
        positions = card.Card.POSITIONS
        
        #goes through each spot on the grid and renders the item at that spot if it has any.        
        for i in range(len(positions)):
            symbol = None
            if self._cardData.getSlot(positions[i]) == card.Card.ROCK:
                symbol= self._oImg
            elif self._cardData.getSlot(positions[i]) == card.Card.SCISSORS:
                symbol = self._xImg
            elif self._cardData.getSlot(positions[i]) == card.Card.PAPER:
                symbol = self._iImg
            else:
                symbol = None
            
            if symbol != None:
                self.image.blit(symbol,
                                (i%3 * self._symbolSize,
                                 i//3 * self._symbolSize))
