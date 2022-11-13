import pygame, sys, legacy_button, Menus, elements

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



Menus.pause(clock)
