import pygame
import helper
from view.view_elements.view_element import ViewElement

class SpriteContainer(ViewElement):
    """
    A view element which acts as a container for another sprite, updating it
    and drawing its image.
    """
    def __init__(self, sprite, name=None, pos=None, **kwargs):
        """
        Initializes the element. sprite is the sprite to be updated and drawn.
        """
        if not isinstance(sprite, pygame.sprite.Sprite):
            raise(Exception("Sprite passed to container was not a Sprite!"))
        
        # Set the rectangle accordingly
        temp_rect = sprite.rect
        if pos:
            temp_rect.move_ip(pos[0], pos[1])
        
        super().__init__(name=name, rect=temp_rect, **kwargs)
        
        self.sprite = sprite
        self.image = self.sprite.image
        
    
    def update(self):
        super().update()
        
        self.sprite.update()
        self.image = self.sprite.image

