import pygame, elements, sys
from dropdownclassTEMP import *


pygame.init()
surface = elements.set_screen((800,600),'Test')
clock = pygame.time.Clock()

size = (100,25)
pos = (400,300)

active_rect = 'Fullscreen'
options = ['Fullscreen', 'Borderless', 'Windowed','infinite','options','itssnowing','Happy','Lets go!']
options2 = ['Fullscreen', 'Borderless']

format = pygame.font.SysFont('arialblack',10)

d1 = dropdown(options,size,pos,'Fullscreen')

while True:
    
    surface.fill((121,128,241))
    
    d1.draw(surface)
    d1.drop(True) 
    d1.checkClick()
    


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gamePaused = True
                menu = 'paused'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)