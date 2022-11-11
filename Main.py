import pygame, sys, Button

pygame.init()
mouse_pos = pygame.mouse.get_pos()       
screen = pygame.display.set_mode(((500,500)), pygame.RESIZABLE)
pygame.display.set_caption('Name')
clock = pygame.time.Clock()

#INSTANCE DEFINING OF SOME KIND
#------------------------------
img1 = pygame.image.load('AI.png').convert_alpha()

testButton = Button.txtButton('Test',200,40,'#222222',(150,230),5,5)
button2 = Button.txtButton('other button',400,40,'#222222',(400,400),5,5)

button3 = Button.imgButton(img1,(100,100),0.08,(250,250),('#FFFFFF','#000000'),(5,5))
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
    #testButton.draw(screen)
    print(testButton.checkPress(True))
    #button2.draw(screen)
    #button2.checkPress(True)
    
    button3.draw(screen)
    print(button3.checkPressed(True))
    #------------------------------

    
    pygame.display.update()
    clock.tick(60)