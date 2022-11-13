import pygame, sys, elements, time
from button import *
#Add menu functions / classes here instead of Main

def pause(clock):
    
    
        #ASSETS
    #Display
    surface = elements.set_screen((800,600),'Weeeee')
    
    #Fonts
    font = pygame.font.SysFont('arialblack',40)
    header = pygame.font.SysFont('arialblack',60)
    
        #BUTTONS
    #Text
    resume_txt = ('Resume',20,'#FFFFFF','arialblack',True)
    options_txt = ('Options',20,'#FFFFFF','arialblack',True)
    exit_txt = ('Exit',20,'#FFFFFF','arialblack',True)
    
    #Image Loading
    display_import = (pygame.image.load('Assets\Icons\display_temp.png'),1)
    sound_import = pygame.image.load('Assets\Icons\sound_temp.png')
    controls_import = pygame.image.load('Assets\Icons\controls_temp.png')
    profile_import= pygame.image.load('Assets\Icons\profile_temp.png')

    #Formatted Images
    display_img = (display_import, 0.05)
    sound_img = (sound_import, 0.05)
    controls_img = (controls_import, 0.05)
    profile_img = (profile_import, 0.05)
    
    #Attributes
    gamePaused = False
    
    #Pause Buttons
    resume = button(resume_txt,(400,250),(200,50),('#333333','#FFFFFF'),(5,5))
    options = button(options_txt,(400,325),(200,50),('#333333','#FFFFFF'),(5,5))
    exit = button(exit_txt,(400,400),(200,50),('#333333','#FFFFFF'),(5,5))
    
    #Option Buttons
    display = button(display_import,(400,250),('image','image'),('#333333','#FFFFFF'),(5,5))
    audio = button(sound_img,(400,325),('image','image'),('#333333','#FFFFFF'),(5,5))
    controls = button(controls_img,(400,400),('image','image'),('#333333','#FFFFFF'),(5,5))
    profile = button(profile_img,(400,475),('image','image'),('#333333','#FFFFFF'),(5,5))
    
        #Navigation
    #Menus
    menu = 'null'
    settings = 'display'
    
    while True:
        
        surface.fill((121,128,241))
        
        #Paused
        if gamePaused == True:
            if menu == 'paused':
                settings = 'display'
                elements.draw_text('PAUSED', header, '#FFFFFF', surface, (400,150))
                
                resume.draw(surface)
                options.draw(surface)
                exit.draw(surface)
                
                if resume.checkClick(True) == True:
                    gamePaused = False
                if options.checkClick(True) == True:
                    menu = 'options'
                if exit.checkClick(True) == True:
                    pygame.quit()
                    sys.exit()
                
            #Options
            if menu == 'options':
                elements.draw_text('OPTIONS', header, '#FFFFFF', surface, (400,150))
                
                display.draw(surface)
                audio.draw(surface)
                controls.draw(surface)
                profile.draw(surface)
            
        else:
            elements.draw_text('Press ESC to pause', font, '#FFFFFF', surface, (400,300))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamePaused = True
                    menu = 'paused'
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(60)