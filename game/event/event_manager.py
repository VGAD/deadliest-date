"""
@author: Blake Bouchard
"""

import pygame
from event.event_list import *


class EventManager:
    """
    This class deals with events that are thrown by the game as well as by the user.
    """
    
    _listing=[]
    _timez =  pygame.time.get_ticks()
    _listeners = {}

    @staticmethod
    def listener(event, function):
        """
        Register a listener. When the given event occurs, the function will be
        called. It will be passed the event as its argument.
        """

        if event not in EventManager._listeners:
            EventManager._listeners[event] = []

        EventManager._listeners[event].append(function)

    @staticmethod
    def update():
        """
        This is the main event handler function of Deadliest Date.

        All Event Handlers should branch off of this loop.
        """
        for event in pygame.event.get():
            # Check for a listener to this event
            if event.type in EventManager._listeners:
                # Call all listener functions
                for fn in EventManager._listeners[event.type]:
                    fn(event)
                    
        #Slow timer.get_ticks slower & less accurate than clock but couldnt get clock working for this purpose.
        if len(EventManager._listing)>0:
            #loop so that the list order dont matter thus faster text dont need to wait on slower text.
            for each in EventManager._listing:
                if (pygame.time.get_ticks() - EventManager._timez) >= each[0]: 
                    #ugly, only for render_text specific, can make for general timed function calling purposes later?
                    if not each[1].render_text():
                        EventManager._listing.remove(each)
                    EventManager._timez = pygame.time.get_ticks()

    @staticmethod
    def addTimed(timer, item):
        EventManager._listing.append([timer,item])
