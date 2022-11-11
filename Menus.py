import pygame, sys, Button, elements
#Add menu functions / classes here instead of Main

def start(clock):
    
    surface = pygame.display.set_mode(((500,500)))
    font = pygame.font.SysFont(None,75)
    
    while True:
        surface.fill((121,128,241))
        elements.draw_text('Test Menu', font, '#FFFFFF', surface, (250,75))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(60)