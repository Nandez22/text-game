import pygame, sys, elements, time
from button import *
#Add menu functions / classes here instead of Main

def start(clock):
    
    surface = elements.set_screen((800,600),'Weeeee')
    font = pygame.font.SysFont('arialblack',40)
    
    gamePaused = False
    text = ('Resume',20,'#FFFFFF','arialblack',True)
    text2 = ('Options',20,'#FFFFFF','arialblack',True)
    text3 = ('Exit',20,'#FFFFFF','arialblack',True)
    
    img = pygame.image.load('AI.png')
    img1 = (img,0.05)
    
    print(elements.get_center(surface))
    
    #Buttons
    resume = button(text,(400,175),(200,50),('#333333','#FFFFFF'),(5,5))
    options = button(text2,(400,275),(200,50),('#333333','#FFFFFF'),(5,5))
    exit = button(text3,(400,375),(200,50),('#333333','#FFFFFF'),(5,5))


    while True:
        
        surface.fill((121,128,241))
        
        if gamePaused == True:
            resume.draw(surface)
            options.draw(surface)
            exit.draw(surface)
            
            if resume.checkClick(True) == True:
                gamePaused = False
            if options.checkClick(True) == True:
                print('Options')
            if exit.checkClick(True) == True:
                pygame.quit()
                sys.exit()
                
            
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