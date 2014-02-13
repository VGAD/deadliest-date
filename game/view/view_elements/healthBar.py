import pygame, sys
import helper
from view.view_elements.view_element import ViewElement
from pygame.locals import *

class HealthBar(ViewElement):
    """
    ViewElement Representing a health bar
    """    
    def __init__(self, rect=None, health=100, barImg=None, barImg2=None, borderImg=None, x=10, y=13, bx=5, by=-4):
        """
        Initialize the healthBar's variables and draw the healthBar once. 
        barImg and borderImg are the images to draw, and
        x and y are the position to draw at. self.length is the length of the bar.
        bx and by represent how much the border should be moved from the main bar.
        barImg2 is the part of the bar that is shown if health is missing. barImg2 should be
        the same length as barImg.
        """
        
        self.rect = rect if rect else pygame.Rect()
        
        super().__init__(name=None, rect=self.rect)
        
        self.maxHealth = health
        self.health = health
        self.x = x
        self.y = y
        self.bx = bx
        self.by = by
        
        if barImg:
            self.barImg = helper.load_image(barImg)
            self.length = self.barImg.get_rect()[2]
            self.width = self.barImg.get_rect()[3]
            
        if barImg2:
            self.barImg2 = helper.load_image(barImg2)
        
        if borderImg:
            self.borderImg = helper.load_image(borderImg)
            
        self.draw(self.x, self.y, self.bx, self.by)
        
    def change(self, amount):
        """
        Change health
        """
        self.health = self.health + amount
        self.draw(self.x, self.y, self.bx, self.by)
        
    def draw(self, x=10, y=13, borderLeft=5, borderUp=-4):
        """
        Draw the health bar at coordinate (x,y) using self.barImg and self.borderImg on the surface (self.image).
        BorderLeft and borderUp are where the border is moved relative to the bar
        """
        black = 0, 0, 0
        self.image.fill(black)
        self.barImg.set_clip(pygame.Rect(0, 0, self.length*self.healthPercent, self.width))
        self.barImg2.set_clip(pygame.Rect(0, 0, self.length*(1-self.healthPercent), self.width))
        drawItem = self.barImg.subsurface(self.barImg.get_clip())
        drawItem2 = self.barImg2.subsurface(self.barImg2.get_clip())
        self.image.blit(drawItem, (x, y))
        if self.healthPercent < 1:
            if self.healthPercent >= 0:
                self.image.blit(drawItem2, (x+self.length*self.healthPercent, y))
            else:
                self.image.blit(drawItem2, (x, y))
        if self.borderImg:
            self.image.blit(self.borderImg, (x-borderLeft, y+borderUp))
        
    @property
    def healthPercent(self):
        """
        Percentage of health remaining in decimal form
        """
        return self.health/self.maxHealth
        
    def getHealth(self):
        """
        Returns the amount of health
        """
        return self.health

#Stuff used for testing below (Requires the test bar sprites to be in the same folder)

#pygame.init() 
        
#r = pygame.Rect(0, 0, 113, 30)
#black = 0, 0, 0

#barImg = 'bar0.png'
#barImg2 = 'bar00.png'
#borderImg = 'bar000.png'

#surf = pygame.display.set_mode((500, 400), 0, 32) #Drawing surface

#h = HealthBar(r, 100, barImg, barImg2, borderImg)

#surf.blit(h.image, (10, 10))  

#while(True):
    #for event in pygame.event.get():
        #if event.type == QUIT:
            #pygame.quit()
            #sys.exit()
        #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_a:
                #h.change(-10)
                #surf.blit(h.image, (10, 10))
                #print(h.getHealth())  
            #if event.key == pygame.K_s:
                #h.change(10)
                #surf.blit(h.image, (10, 10))  
                #print(h.getHealth())  
            
    #pygame.display.update()
        
        
