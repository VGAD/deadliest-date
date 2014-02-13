import pygame
import helper
from view.view_elements.view_element import ViewElement

class Image(ViewElement):
    """
    A view element which just displays an image.
    """
    def __init__(self, surface, name=None, pos=None, **kwargs):
        """
        Initializes the element. Surface is the surface which will be displayed,
        and will just be directly rendered to the view element's position.
        """
        temp_image = helper.load_image(surface)
        
        # Set the rectangle accordingly
        temp_rect = temp_image.get_rect()
        if pos:
            temp_rect.move_ip(pos[0], pos[1])
        
        if type(temp_image) != pygame.Surface:
            raise(Exception("Surface passed to view element is wrong type!"))
        
        super().__init__(name=name, rect=temp_rect, **kwargs)
        
        self.image = temp_image
