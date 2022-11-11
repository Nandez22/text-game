import pygame, sys, Button, Menus, elements

pygame.init()
app_icon = pygame.image.load('AI.png')
pygame.display.set_icon(app_icon)

mouse_pos = pygame.mouse.get_pos()       
clock = pygame.time.Clock()

screen = elements.set_screen((500,500), 'Window', True)


#INSTANCE DEFINING OF SOME KIND
#------------------------------
img1 = pygame.image.load('AI.png').convert_alpha()

#------------------------------



Menus.start(clock)


'''
while True:
    #Exit logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #ACTUAL CONTENT GOES BELOW LINE
    #------------------------------
    screen.fill((121,128,241))
    testButton.draw(screen)
    print(testButton.checkPress(True))
    button2.draw(screen)
    button2.checkPress(True)
    
    button3.draw(screen)
    print(button3.checkPressed(True))
    #------------------------------

    
    pygame.display.update()
    clock.tick(60)
'''