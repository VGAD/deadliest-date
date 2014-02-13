import pygame

def load_image(image):
    """
    If an image is passed, returns the image. If a string is passed, loads
    an image from the given filename.
    """
    temp_image = image
    
    # Load the image if a filename is given
    if type(image) == str:
        temp_image = pygame.image.load(image).convert_alpha()

    # Throw an exception if this wasn't a surface
    if type(temp_image) != pygame.Surface:
        raise(Exception("Tried to load a non-image!"))
        
    return temp_image
