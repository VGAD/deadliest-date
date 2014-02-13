import pygame
from pygame.sprite import LayeredUpdates
from event.event_manager import EventManager
from event.event_list import *


class GUI(LayeredUpdates):
    """
    FUCK
    """

    # number of GUI instances
    num_instances = 0

    def __init__(self, screen_rect, bg_color):
        """
        Set up the GUI and attach the view switch listener.
        """
        LayeredUpdates.__init__(self)

        if GUI.num_instances != 0:
            raise AssertionError("GUI: can only have one instance of a simulation")
        GUI.num_instances = 1

        self.screen = pygame.display.set_mode((screen_rect.w,
                                              screen_rect.h))
        self.bg_color = bg_color

        # The current view
        self.current_view = None
        
        # Attach the listeners
        EventManager.listener(EVENT_CHANGE_VIEW,
                              lambda event: self.switch_view(event.view))
        
        EventManager.listener(pygame.MOUSEBUTTONUP,
                              self.on_click)
        
    def on_click(self, e):
        """
        Handles click events appropriately.
        """
        self.current_view.on_click(e)

    def update(self):
        """
        Updates all necessary things in preparation for a render.
        """
        self.current_view.update()

    def draw(self):
        """
        Draws all necessary things to the screen in preparation for
        rendering.
        """
        self.screen.fill(self.bg_color)
        self.current_view.draw(self.screen)

    def switch_view(self, cls):
        """
        Switches the view to the view defined by the new class.
        """
        # Check to see if there's a current view
        if self.current_view:
            # Stop the old view
            self.current_view.stop()

        # Initialize the new view
        self.current_view = cls()

        # Start the new view
        self.current_view.start()
