"""
@author: Blake Bouchard
"""

import pygame

CURRENT_USEREVENT_NUMBER = pygame.USEREVENT

def getUsereventNumber():
    global CURRENT_USEREVENT_NUMBER 
    CURRENT_USEREVENT_NUMBER += 1
    return CURRENT_USEREVENT_NUMBER

EVENT_ATTACK_CHARACTER = getUsereventNumber() # target, card
EVENT_CHANGE_VIEW = getUsereventNumber() # view
EVENT_DAMAGE_CHARACTER = getUsereventNumber() # target, damage
EVENT_HEAL_CHARACTER = getUsereventNumber() # target, healing
