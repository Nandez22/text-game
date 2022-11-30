import pygame, sys, Menus, os

pygame.init()

app_icon = pygame.image.load('Assets/Icons/AI.png')
pygame.display.set_icon(app_icon)
pygame.mixer.init()
mouse_pos = pygame.mouse.get_pos()       
clock = pygame.time.Clock()

#INSTANCE DEFINING OF SOME KIND
#------------------------------


#------------------------------


#1#connect.play

Menus.pause(clock)



img1 = pygame.image.load('Assets/Icons/AI.png').convert_alpha()



#TODO Add screen size logic
#TODO Fix overlap issue with dropdown menus
#TODO Continue outfitting settings menu / UI / UX
#TODO Possibly create volume slizer
#TODO Create main game init
#TODO Start with playerdata json