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
    
    display_txt = ('Display',20,'#FFFFFF','arialblack',True)
    audio_txt = ('Sound',20,'#FFFFFF','arialblack',True)
    controls_txt = ('Controls',20,'#FFFFFF','arialblack',True)
    profile_txt = ('Profile',20,'#FFFFFF','arialblack',True)
    
    #Images
    

    #Attributes
    gamePaused = False
    
    #Pause Buttons
    resume = button(resume_txt,(400,250),(200,50),('#333333','#FFFFFF'),(5,5))
    options = button(options_txt,(400,325),(200,50),('#333333','#FFFFFF'),(5,5))
    exit = button(exit_txt,(400,400),(200,50),('#333333','#FFFFFF'),(5,5))
    
    #Option Buttons
    display = button(display_txt,(300,50),(200,25),('#333333','#FFFFFF'),(5,5))
    audio = button(audio_txt,(350,50),(200,25),('#333333','#FFFFFF'),(5,5))
    controls = button(controls_txt,(450,50),(200,25),('#333333','#FFFFFF'),(5,5))
    profile = button(profile_txt,(500,50),(200,25),('#333333','#FFFFFF'),(5,5))
    
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