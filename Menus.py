import pygame, sys, elements, time
from button import *
#Add menu functions / classes here instead of Main

def start(clock):
    
    surface = elements.set_screen((800,600),'Weeeee',True)
    font = pygame.font.SysFont('arialblack',40)
    
    gamePaused = False
    text = ('Resume',20,'#FFFFFF','arialblack',True)
    text2 = ('Options',20,'#FFFFFF','arialblack',True)
    text3 = ('Exit to menu',20,'#FFFFFF','arialblack',True)
    
    img = pygame.image.load('AI.png')
    img1 = (img,0.05)
    
    print(elements.get_center(surface))
    
    hair1 = pygame.Rect((0,0),(800,3))
    hair2 = pygame.Rect((0,0),(3,600))
    hair1.center = (400,300)
    hair2.center = (400,300)
    
    #Buttons
    button1 = button(text,(400,300),(200,50),('#333333','#FFFFFF'),(5,5))
    button2 = button(text2,(0,100),(200,50),('#333333','#FFFFFF'),(5,5))
    button3 = button(text3,(0,-100),(200,50),('#333333','#FFFFFF'),(5,5))
    button4 = button(img1,(400,300),('image','image'),('#333333','#FFFFFF'),(5,5))
    while True:
        
        surface.fill((121,128,241))
        pygame.draw.rect(surface, '#FFFFFF', hair1)
        pygame.draw.rect(surface, '#FFFFFF', hair2)
        
        if gamePaused == True:
            button1.draw(surface)
            button2.draw(surface)
            button3.draw(surface)
            button4.draw(surface)
            
            button2.checkClick(True)
            button3.checkClick(True)
            button4.checkClick(True)            
            
            if button1.checkClick(True) == True:
                gamePaused = False
        else:
            
            elements.draw_text('Press ESC to pause', font, '#FFFFFF', surface, (400,300))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamePaused = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(60)