import pygame
from pygame.sprite import Sprite


class ViewElement(Sprite):
    """
    A basic element which is rendered to a view.
    """
    def __init__(self, name=None, rect=None, background=None,
                  parent=None, **kwargs):
        super().__init__()

        # The name of the element
        self.name = name
        
        # The element's rectangle, relative to the parent
        self.base_rect = rect if rect is not None else pygame.Rect(0,0,0,0)
        
        # The parent element, if any. If there is one, this will be placed
        # relative to the parent
        self.parent = parent

        # The elements's bounding rectangle, i.e. its actual position on-screen
        # This should always be defined BEFORE you call super().__init__ in any
        # subclasses!
        self.rect = self.get_rect()

        # The image to render
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        if background:
            self.image.fill(background)
            
    def get_rect(self):
        """
        Returns the element's actual rect, adjusted to parent position
        """
        rect = self.base_rect.copy()
        
        # Offset by parent rectangle
        if self.parent:
            parent_rect = self.parent.get_rect()
            
            rect.move_ip(parent_rect.x, parent_rect.y)
            
        return rect
            
    def update(self):
        """
        Updates the element's position.
        """
        self.rect = self.get_rect()
        
        super().update()

    def click(self, event):
        """
        Called when the element is clicked.
        """
        pass
        
