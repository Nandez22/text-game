import pygame, sys, Button

pygame.init()
mouse_pos = pygame.mouse.get_pos()       
screen = pygame.display.set_mode(((500,500)), pygame.RESIZABLE)
pygame.display.set_caption('Name')
clock = pygame.time.Clock()

#INSTANCE DEFINING OF SOME KIND
#------------------------------

testButton = Button.txtButton('Test',200,40,'#222222',(150,230),5,5)
button2 = Button.txtButton('Other Button',400,40,'#222222',(200,200),5,5)
#------------------------------

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
    #------------------------------

    
    pygame.display.update()
    clock.tick(60)