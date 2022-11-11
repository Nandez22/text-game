import pygame, sys, Button, elements
#Add menu functions / classes here instead of Main

def start(clock):
    
    surface = elements.set_screen((800,600))
    font = pygame.font.SysFont('arialblack',40)
    
    gamePaused = False
    
    #Buttons

    
    while True:
        surface.fill((121,128,241))

        if gamePaused == True:
            pass
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