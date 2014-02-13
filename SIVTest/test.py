import sys, pygame
pygame.init()
3
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
7
screen = pygame.display.set_mode(size)
9
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
12
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
        
	
		
