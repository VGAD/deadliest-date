import pygame

from view.base_view import BaseView
from view.view_elements import *
from objects import card
from objects import animation

class DebugView(BaseView):
    """
    A debug view.
    """


    def test_func(self):
        self.get_element('test2').activate()
        self.get_element('test1').deactivate()
        self.remove_element('card viewing')

    def test2_func(self):
        self.get_element('test1').activate()
        self.get_element('test2').deactivate()
        
    def test3_func(self):
        self.remove_element('test3')

    def __init__(self, **kwargs):
        """
        Initializes a new debug view.
        """
        super().__init__(**kwargs)
        
        
        food = self.add_element(view_element.ViewElement(
            'food',
            pygame.Rect(50, 350, 0, 0)))

        self.add_element(text_box.TextBox(
            'textingAndDriving',
            pygame.Rect(50,0,200,150),
            text='^r!_^We now ^w_^Right ^w_^Align^w^ I Think. ^w_^... Lots of ^w!^bolding ^b!^BOLD ^B^and ^w~^italian ^g~^italics ^G^with ^i_^underlined ^w_^lines, and ^p!~_^ALL ^y!~_^stuff ^i!~_^haha. ^w_^This ->   ^w_^<-^w^ is empty. Oh look a penny. ^G^hahahahahhaahhahahahahahahawawaawawaw ^g!^<- long word got cut off at the end of the line.^G_^ Lotsa space     underline space race! ^r!^C^p!^O^y!^L^w!^O^g!^U^b!^R^i!^S^B!^!',
            colour=(200,200,200), fxspeed=30, parent=food))

        self.add_element(text_box.TextBox(
            'pizzaTime',
            pygame.Rect(250,100,300,150),
            text='The Pizza 73 Team aims to satisfy each and every customer by providing superb food, fast, friendly Service and true value.To make a short story long... The year was 1985. It was a magical time when hair defied gravity, neon spandex defied explanation, and pizza came in one of two choices: tasty or cheap. But that would soon change.',
            colour=(200,200,200), parent=food))
       
        
        test_group = self.add_element(view_element.ViewElement(
            'test_group',
            pygame.Rect(100, 150, 0, 0)))

        self.add_element(button.Button(
            'assets/view/debugview/test1.gif',
            'test1',
            (40, 80),
            'assets/view/debugview/test.gif',
            'assets/view/debugview/test2.gif',
            self.test_func,
            parent=test_group))

        self.add_element(button.Button(
            'assets/view/debugview/test1.gif',
            'test2',
            (150, 20),
            'assets/view/debugview/test.gif',
            'assets/view/debugview/test2.gif',
            self.test2_func,
            text='F U',
            pad=1,
            active=False,
            parent=test_group))
        
        self.add_element(button.Button(
            'assets/view/debugview/test1.gif',
            'test3',
            (100, 120),
            'assets/view/debugview/test.gif',
            'assets/view/debugview/test2.gif',
            self.test3_func,
            parent=test_group))

        self.add_element(text_box.TextBox(
            'testbox',
            pygame.Rect(50, 50, 100, 30),
            'here\'s a bunch of crap',
            parent=test_group))
            
        self.add_element(healthBar.HealthBar(
            pygame.Rect(-10, -10, 115, 34),
            100,
            'assets/view/debugview/bar0.png',
            'assets/view/debugview/bar00.png',
            'assets/view/debugview/bar000.png',
            10,
            13,
            5, 
            -4
            ))
            
        self.add_element(tile_box.TileBox(
            'tilebox',
            pygame.Rect(50, 50, 96, 96),
            12,
            12,
            'assets/view/debugview/testbox.png')) 
        
        self.add_element(view_card.ViewCard(
            card.Card({'topLeft' : 'ROCK',
                       'topCenter' : 'PAPER',
                       'topRight' : None,
                       'midLeft' : 'ROCK',
                       'midCenter' : None,
                       'midRight' : 'SCISSORS',
                       'bottomLeft' : None,
                       'bottomCenter' : None,
                       'bottomRight' : None }),
            'assets/view/debugview/grid.png',
            'assets/view/debugview/o.png',
            'assets/view/debugview/x.png',
            'assets/view/debugview/i.png',
            pos = (350, 50),
            name = 'card viewing'))
            
        self.add_element(image.Image(
            'assets/view/debugview/test.gif',
            'test_image',
            (50, 200)))
        
        self.test_animation = animation.Animation(
            'assets/view/debugview/animation.png',
            30,
            30,
            0.1)
            
        self.add_element(sprite_container.SpriteContainer(
            self.test_animation,
            'test_container',
            (50, 250)))
            
