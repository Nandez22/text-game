import pygame, sys, Menus, elements

pygame.init()
app_icon = pygame.image.load('Assets/Icons/AI.png')
pygame.display.set_icon(app_icon)

mouse_pos = pygame.mouse.get_pos()       
clock = pygame.time.Clock()

#INSTANCE DEFINING OF SOME KIND
#------------------------------


#------------------------------



Menus.pause(clock)
img1 = pygame.image.load('Assets/Icons/AI.png').convert_alpha()