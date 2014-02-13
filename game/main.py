"""
Deadliest Date Main File
"""

import sys
import pygame
from event.event_manager import EventManager
from event.event_list import *
from view import debugview, main_menu, battle
from gui import GUI

# Screen settings
RESOLUTION = pygame.Rect(0, 0, 800, 600)
BG_COLOR = (32, 32, 32)

# Initialize everything
#~ pygame.mixer.pre_init(22050, -16, 2, 512) # Small buffer for less sound lag
pygame.init()
pygame.display.set_caption("The Deadliest Date")

# Starting the main GUI
main_gui = GUI(RESOLUTION, BG_COLOR)

# Add event listeners
def quit_game(event):
    pygame.display.quit()
    sys.exit()


def on_keydown(event):
    """
    Handle keyboard input by delegating to the relevant function.
    """
    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        quit_game(event)

EventManager.listener(pygame.KEYDOWN, on_keydown)
EventManager.listener(pygame.QUIT, quit_game)

# Switch to Debug View using Pygame's event queue
#~ switch_to_debug = pygame.event.Event(EVENT_CHANGE_VIEW, view=battle.BattleView)
switch_to_debug = pygame.event.Event(EVENT_CHANGE_VIEW, view=debugview.DebugView)
pygame.event.post(switch_to_debug)

# Switch to main menu (Ctrl-e the below and ctrl-e the above to screw around with this)
#~ switch_to_main_menu = pygame.event.Event(EVENT_CHANGE_VIEW, view=main_menu.MainMenuView)
#~ pygame.event.post(switch_to_main_menu)

# Initialize more Pygame stuff
clock = pygame.time.Clock()

# Get command line arguments
argv = sys.argv[1:]

# The main game loop
while 1:
    EventManager.update()
    main_gui.update()
    main_gui.draw()
    pygame.display.flip()
    clock.tick(60)
