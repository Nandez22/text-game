import pygame, sys, elements, time
from Button import *
#Add menu functions / classes here instead of Main

def start(clock):
    
    surface = elements.set_screen((800,600))
    font = pygame.font.SysFont('arialblack',40)
    
    gamePaused = False
    
    #Buttons
    button1 = txtButton('Resume', 500, 50, '#333333',(400,300),3,5,'#FFFFFF')
    
    while True:
        
        surface.fill((121,128,241))
        
        if gamePaused == True:
            
            txtButton.draw(button1,surface)
            if button1.checkPress(True,'#FFFFFF') == True:
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