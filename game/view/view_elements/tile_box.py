import pygame
import helper
from view.view_elements.view_element import ViewElement


class TileBox(ViewElement):
    """
    A box made up of tiled images.
    """
    
    def __init__(self, name=None, rect=None,
        hBarWidth=0, vBarWidth=0, tileSheet="", **kwargs):
        """
        hBarWidth is the width of the horizontal bars on either side, while
        vBarWidth is the width of the vertical bars. The corners will be of size
        hBarWidth x vBarWidth.
        The tiles are loaded from the file with filename tileSheet.
        """
        
        self.rect = rect if rect else pygame.Rect()
        
        super().__init__(name=name, rect=self.rect, **kwargs)
        
        self.hBarWidth = hBarWidth
        self.vBarWidth = vBarWidth
        
        # Set the tilesheet
        self._tileSheet = None
        self.setTileSheet(tileSheet)
        
    def render(self):
        """
        Re-render the surface
        """
        
        # Create empty surface
        self.image = pygame.Surface(self.rect.size)
        
        # Find bounds of the center piece in the tileset
        tileCenterRect = pygame.Rect(
            self.hBarWidth,
            self.vBarWidth,
            self._tileSheet.get_width() - 2 * self.hBarWidth,
            self._tileSheet.get_height() - 2 * self.vBarWidth)
        
        # Find bounds of the center piece in the actual image
        centerRect = pygame.Rect(
            self.hBarWidth,
            self.vBarWidth,
            self.rect.width - 2 * self.hBarWidth,
            self.rect.height - 2 * self.vBarWidth)
    
        # Draw the horizontal edge
        if self.hBarWidth > 0:
            # Corners
            if self.vBarWidth > 0:
                # Left upper
                self.image.blit(self._tileSheet,
                                 (0, 0),
                                 pygame.Rect(0,
                                             0,
                                             self.hBarWidth,
                                             self.vBarWidth))
                
                # Right upper
                self.image.blit(self._tileSheet,
                                 (centerRect.right, 0),
                                 pygame.Rect(tileCenterRect.right,
                                             0,
                                             self.hBarWidth,
                                             self.vBarWidth))
                
                # Bottom left
                self.image.blit(self._tileSheet,
                                 (0, centerRect.bottom),
                                 pygame.Rect(0,
                                             tileCenterRect.bottom,
                                             self.hBarWidth,
                                             self.vBarWidth))
                
                # Bottom right
                self.image.blit(self._tileSheet,
                                 (centerRect.right, centerRect.bottom),
                                 pygame.Rect(tileCenterRect.right,
                                             tileCenterRect.bottom,
                                             self.hBarWidth,
                                             self.vBarWidth))
            
            # Bars
            for i in range(0, centerRect.height, tileCenterRect.height):
                # Cut off at the bottom of the bar
                clipHeight = tileCenterRect.height
                if i + clipHeight >= centerRect.bottom:
                    clipHeight = centerRect.bottom - i - self.vBarWidth
                
                # Left bar
                self.image.blit(self._tileSheet,
                                 (0, tileCenterRect.top + i),
                                 pygame.Rect(0,
                                             tileCenterRect.top,
                                             self.hBarWidth,
                                             clipHeight))
                                             
                # Right bar
                self.image.blit(self._tileSheet,
                                 (centerRect.right, tileCenterRect.top + i),
                                 pygame.Rect(tileCenterRect.right,
                                             tileCenterRect.top,
                                             self.hBarWidth,
                                             clipHeight))
        
        # Draw the vertical edge
        if self.vBarWidth > 0:
            # Bars
            for i in range(0, centerRect.width, tileCenterRect.width):
                # Cut off at the edge of the bar
                clipWidth = tileCenterRect.width
                if i + clipWidth >= centerRect.right:
                    clipWidth = centerRect.right - i - self.hBarWidth
                
                # Top bar
                self.image.blit(self._tileSheet,
                                 (tileCenterRect.left + i, 0),
                                 pygame.Rect(tileCenterRect.left,
                                             0,
                                             clipWidth,
                                             self.vBarWidth))
                                             
                # Bottom bar
                self.image.blit(self._tileSheet,
                                 (tileCenterRect.left + i, centerRect.bottom),
                                 pygame.Rect(tileCenterRect.left,
                                             tileCenterRect.bottom,
                                             clipWidth,
                                             self.vBarWidth))
        
        for x in range(0, centerRect.width, tileCenterRect.width):
            for y in range(0, centerRect.height, tileCenterRect.height):
                # Cut off at the edges
                clipWidth = tileCenterRect.width
                if x + clipWidth >= centerRect.right:
                    clipWidth = centerRect.right - x - self.hBarWidth
                    
                clipHeight = tileCenterRect.height
                if y + clipHeight >= centerRect.bottom:
                    clipHeight = centerRect.bottom - y - self.vBarWidth
                    
                self.image.blit(self._tileSheet,
                                 (tileCenterRect.left + x, tileCenterRect.top + y),
                                 pygame.Rect(tileCenterRect.left,
                                             tileCenterRect.top,
                                             clipWidth,
                                             clipHeight))
        
        
    def setTileSheet(self, sheetName):
        """
        Loads in the tilesheet and re-renders the box
        """
        
        self._tileSheet = helper.load_image(sheetName)
        
        # Render the image
        self.render()
