import pygame, sys, Button, Menus, elements

pygame.init()
mouse_pos = pygame.mouse.get_pos()       
clock = pygame.time.Clock()

screen = elements.set_screen((500,500), 'Window', True)


#INSTANCE DEFINING OF SOME KIND
#------------------------------
img1 = pygame.image.load('AI.png').convert_alpha()

testButton = Button.txtButton('Test',200,40,'#222222',(150,230),5,5)
button2 = Button.txtButton('other button',400,40,'#222222',(400,400),5,5)

button3 = Button.imgButton(img1,(100,100),0.08,(250,250),('#FFFFFF','#000000'),(5,5))
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