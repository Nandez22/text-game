import pygame, sys

pygame.init()
#The window is now resizeable (I can't spell that word)
screen = pygame.display.set_mode(((500,500)), pygame.RESIZABLE)
pygame.display.set_caption('The name of our game, which we will need to figure out. I guess we could also make the name of the window update with the action that is happening in the game since it will be sort of an idle game. (this is assuming that the window title can update without the window being closed and reopened)')

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
    #Assuming this keeps the 'fps' or ticks for animation
    clock.tick(60)