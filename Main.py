import pygame, sys

pygame.init()
screen = pygame.displayt.set_mode((500,500))
pygame.display.set_caption('Window Name')

#not sure about this one... **Nevermind I think I know
clock = pygame.time.Clock()

#Styling
gui_font = pygame.font.Font(None,30)

while True:
    #Exit logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #ACTUAL CONTENT GOES BELOW LINE
    #------------------------------
    
    #BG color
    screen.fill((121,128,241))
    
    pygame.display.update()
    #Assuming this keeps the 
    clock.tick(60)