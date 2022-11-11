import pygame, sys, Button, elements
#Add menu functions / classes here instead of Main

def start(clock):
    
    surface = elements.set_screen((800,600))
    font = pygame.font.SysFont('arialblack',40)
    
    while True:
        surface.fill((121,128,241))
        elements.draw_text('Press SPACE to pause', font, '#FFFFFF', surface, (160,250))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(60)