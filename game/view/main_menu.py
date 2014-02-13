import pygame, sys

from view.base_view import BaseView
from view.view_elements import *
from objects import card

class MainMenuView(BaseView):
    """
    The main menu view.
    """
    def exitButton(self):
    #What happens when exit is pressed
        sys.exit()
        
    def startButton(self):
    #What happens when start is pressed
        pass
        
    def loadButton(self):
    #What happens when load is pressed
        pass
        
    def creditsButton(self):
    #What happens when credits is pressed
        pass

    def __init__(self, **kwargs):
        """
        Initializes a new main menu view.
        """
        super().__init__(**kwargs)
        
        self.add_element(image.Image(
        'assets/view/main_menu/balls.png',
        'Background',
        (0, 0)))
        
        self.add_element(button.Button(
        'assets/view/main_menu/tempExit.png',
        'Exit Button',
        (5, 490),
        'assets/view/main_menu/tempExit2.png',
        'assets/view/main_menu/tempExit.png',
        self.exitButton))
        
        self.add_element(button.Button(
        'assets/view/main_menu/tempStart.png',
        'Start Button',
        (5, 380),
        'assets/view/main_menu/tempStart2.png',
        'assets/view/main_menu/tempStart.png',
        self.startButton))
        
        self.add_element(button.Button(
        'assets/view/main_menu/tempLoad.png',
        'Load Button',
        (5, 435),
        'assets/view/main_menu/tempLoad2.png',
        'assets/view/main_menu/tempLoad.png',
        self.loadButton))
        
        self.add_element(button.Button(
        'assets/view/main_menu/tempCredits.png',
        'Credits Button',
        (5, 545),
        'assets/view/main_menu/tempCredits2.png',
        'assets/view/main_menu/tempCredits.png',
        self.creditsButton))
        
        
