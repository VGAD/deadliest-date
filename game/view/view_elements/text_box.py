import pygame

from view.view_elements.view_element import ViewElement
from event.event_manager import *

# Basic font
pygame.font.init()
FONT_SIZE = 12
FONT_NAME="Arial"
FONT_COLOUR = (0, 0, 0)

class TextBox(ViewElement):
    """
    A view element containing text.
    """

    def __init__(self, name=None, rect=None,
                   text="", font=FONT_NAME, fontSize=FONT_SIZE, colour=FONT_COLOUR,
                   pad=3, spacing=3, fxspeed=0, **kwargs):
        """
        If text is defined then text with a given font will be blitted
        onto the images.
        Pad is used to determine how lines should be drawn. 
        Text will be right aligned to the top left corner of the rect
        Spacing is pixel spacing between lines
        Fxspeed is the time for each word to show up in milliseconds, almost like a "type writer" effect.
        """

        # Required for pygame sprite
        self.rect = rect if rect else pygame.Rect(0, 0, 0, 0)

        super().__init__(name=name, rect=self.rect, **kwargs)
        self._text = text      
        self._fontSize = fontSize
        self._fontName = font
        #should use pygame.font.match_font(name, bold=False, italic=False) to check if font exist?
        self._font = pygame.font.SysFont(font, self._fontSize, bold=False, italic=False)
        self._colour = colour
        self._pad = pad
        self._spacing = spacing
        self._speed = fxspeed
        #stores the current index of the text
        self.i = 0
        # Find the starting y height and Find x to render for the line
        self.y = self._spacing
        self.x = self._pad
        # used in getting x location of next word and for measuring line size.
        self.tempLine = []
        # list of tags for current word
        self.signs = []
        # Divide into letters
        self.words = list(self._text)
        
        #Note: colourDic IS case sensitive, e.g. b=blue, B=Black
        self._colourDic = {'r':(255,0,0), 'g':(0, 255,0), 'b':(0, 0, 255), 'w':(255,255,255), 'B':(0,0,0),
                            'p':(255,0,255), 'y':(255, 255, 0), 'i':(0, 255, 255), 'G':(122,122,122)}
                            
        EventManager.addTimed(self._speed,self)
        
    def lazyFunc(self):
        self.i +=1
        return self.words[self.i]
        
    def render_text(self):
        """
        Renders the text onto the current image.
        """
        # If text defined, blit it onto each image
        if self._text:
            # Find the maximum width of a line of text
            width = self.rect.width
            width -= self._pad * 2
            
            # Find height of the line
            height = self._font.size(self.words[0])[1]
            height -= self._spacing
            
            # Create the text surface
            self._text_surface = pygame.Surface(self.rect.size)
            
            # Handle blitting to all button surfaces:
            if self.i < len(self.words):
                while self.i < len(self.words):
                    l = self.words[self.i]
                    # Move to next line if next word doesn't fit in textbox 
                    # and after a space is found (dont want to cut words)
                    # NOTE: This cuts off super long words, or long words at the end of the line.
                    if l == " " and self._font.size(l+' '+" ".join(self.tempLine))[0] >= width:
                        l =  self.lazyFunc()
                        self.y += height + self._spacing
                        
                        # Reset the line and x since we have a new line
                        self.x = self._pad
                        self.tempLine = []
                    
                    # If a word has a color tag also set italics or bold if their prefix found.
                    bolden = False
                    italicize = False
                    underlined = False
                    
                    # stores the tag and offsets the indexes so tag doesn't get rendered
                    if l == "^":
                        self.signs = []
                        l = self.lazyFunc()
                        while l != "^":
                            self.signs.append(l)
                            l = self.lazyFunc()
                        l = self.lazyFunc()
                        
                    if l!='' and self.signs != []:
    
                        # checks for bold
                        if '!'in self.signs:
                            bolden = True 
    
                        # checks for italics
                        if '~'in self.signs:
                            italicize = True
                        
                        # checks for underlines
                        if '_' in self.signs:
                            underlined = True
                        
                        # sets color
                        self._colour = self._colourDic[self.signs[0]]
                    
                    # applies font, font size, bolding and italics
                    self._font = pygame.font.SysFont(self._fontName, self._fontSize, bold=bolden, italic=italicize)
                    
                    # applies underline if underline is true
                    pygame.font.Font.set_underline(self._font,underlined)
                    
                    # gets the color and then renders the word
                    wordSurface = self._font.render(l, True, self._colour) 
                    
                    self.tempLine.append(l)
                    
                    # Get the rendered text
                    self.image.blit(wordSurface, (self.x, self.y))
                    
                    # Find the x to render the next word in the propper location
                    self.x += self._font.size(self.tempLine[-1])[0]
                    
                    #increase iteration of what index word we are in the words list
                    self.i += 1
                    
                    #if it has a type writer effect, interrupt the while loop.
                    if self._speed > 0:
                        return True
                
                return False
