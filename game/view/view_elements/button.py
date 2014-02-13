import pygame
import helper
from view.view_elements.text_box import TextBox


class Button(TextBox):
    """
    A clickable button.
    """
    def __init__(self, active_image, name=None, pos=None,
                   hover_image=None, off_image=None,
                   on_click=None, active=True, **kwargs):
        """
        Initializes a button with callback function
        for when clicked "callback", active image "active_image", and
        image when hovered over "hover_image", and inactive image
        "off_image".

        pos is a tuple containing the leftmost x and topmost y coordinates of
        the button

        If active is true then the button begins as
        active and rendered, if active is false then it's inactive and
        rendered.

        This function assumes all images are exactly the same size.
        """

        # Load in the active image
        self._active_image = helper.load_image(active_image)

        # Set the rectangle accordingly
        temp_rect = self._active_image.get_rect()
        if pos:
            temp_rect.move_ip(*pos)

        super().__init__(name=name, rect=temp_rect, **kwargs)

        # Load in other images
        if hover_image:
            self._hover_image = helper.load_image(hover_image)

        if off_image:
            self._off_image = helper.load_image(off_image)

        # Whether this is active
        self._active = active

        # Function to call when clicked
        self._on_click = on_click

        # Current image
        self.image = self._active_image

        # The source of current image.
        self._source = self._active_image

    def update(self):
        """
        Called every frame. Updates the button.
        """
        super().update()
        
        changed = False

        # Set the deactivated image
        if not self._active:
            if self._off_image and self._source != self._off_image:
                self._source = self._off_image
                changed = True

        # Set the hover image while hovering
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
                if self._hover_image and self._source != self._hover_image:
                    self._source = self._hover_image
                    changed = True

        # Revert to active image
        elif self._source != self._active_image:
            self._source = self._active_image
            changed = True

        # Redraw text when the surface changes
        if changed:
            self.image = self._source.copy()
            self.render_text()

    def activate(self):
        """
        Activates the button. Rendered and interactable.
        """
        self._active = True

    def deactivate(self):
        """
        Deactivates the button.
        This button is still rendered, but just doesn't do anything.
        """
        self._active = False

    def click(self, event):
        """
        Override to run the on_click function.
        """
        if self._active:
            self._on_click()
