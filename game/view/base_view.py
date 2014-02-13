import pygame
# from view.view_elements import view_element
from collections import namedtuple

Button = namedtuple('Button',
                        ['callback',
                        'active_image',
                        'hover_image',
                        'off_image',
                        'pos_rect'])


class BaseView:
    """
    The base view, all views extend from this.
    """

    def __init__(self, **kwargs):
        """
        Initializes the base view.
        """
        # All added elements of this view.
        self._elements = pygame.sprite.LayeredUpdates()

        # All possible buttons for this view
        # 'name': (callback, image, hover_image, off_image, screen_rect)
        self._buttons = {}

        # Active buttons for this view
        # 'name': rect
        self._active_buttons = {}

        # Inactive buttons for this view
        # Note, this is a set, not a dict as we don't need the rects
        self._inactive_buttons = set()

    def start(self):
        """
        Starts this view.
        Override this in subclasses for functionality.
        This is where all images and buttons should be added/loaded.
        """
        pass

    def stop(self):
        """
        Stops this view.
        """
        pass

    def update(self):
        """
        Updates this view.
        """
        self._elements.update()

    def draw(self, screen):
        """
        Draws this view onto a screen.
        """
        # Render added elements
        self._elements.draw(screen)

    def on_click(self, e):
        """
        Handles mouse clicks in this view.
        Iterates over current button rectangles to see if there's a
        collision. If there is the button call back function is used.

        An interesting problem is presented here; if the callback
        function modifies the dict of active buttons then a runtime
        error is raised. The solution is fairly simple and yet I feel
        it's inelegant.
        """
        function = None

        # Iterate over active buttons
        for element in self._elements:
            # If point is in rect then run associated button method
            if element.rect.collidepoint(e.pos):
                function = element.click
                break

        if function:
            function(e)

    def add_element(self, element):
        """
        Adds an element to the view. And returns the element.
        """
        self._elements.add(element)
        return element

    def get_element(self, name):
        """
        Finds an element in the view by its name, or None if it couldn't be
        found in the element group.
        """
        for element in self._elements:
            if element.name == name:
                return element

        return None
        
    def remove_element(self, element):
        """
        Removes an element from the view. If element is a string, calls
        get_element first to find the element with the given name
        """
        temp_elem = element
        
        # Get the given element if the type is a string
        if type(element) == str:
            temp_elem = self.get_element(element)
        
        # If it's not actually an element, give up
        if temp_elem == None: return
        
        # Remove the element
        self._elements.remove(temp_elem)
