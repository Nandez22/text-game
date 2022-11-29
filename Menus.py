import pygame, sys, elements, os
from settings import *
from sprites import *
from level import Level
from pygame.locals import *

#Add menu functions / classes here instead of Main
def pause(clock):
    
        #ASSETS
    #Display
    hardwareDisp = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    surface = elements.set_screen((800,600),'Paused',True)

    #Fonts
    regular = pygame.font.SysFont('arialblack',40)
    sub = pygame.font.SysFont('arialblack',20)
    header = pygame.font.SysFont('arialblack',60)
    
        #BUTTONS
    #Text
    
    resume_txt = ('RESUME',20,'#FFFFFF','arialblack',True)
    options_txt = ('OPTIONS',20,'#FFFFFF','arialblack',True)
    exit_txt = ('EXIT',20,'#FFFFFF','arialblack',True)
    
    display_txt = ('DISPLAY',15,'#FFFFFF','arialblack',True)
    audio_txt = ('SOUND',15,'#FFFFFF','arialblack',True)
    controls_txt = ('CONTROLS',15,'#FFFFFF','arialblack',True)
    profile_txt = ('PROFILE',15,'#FFFFFF','arialblack',True)
    
    yes_txt = ('YES',30,'#FFFFFF','arialblack',True)
    no_txt = ('NO',30,'#FFFFFF','arialblack',True)
    
    #Images
    

    #Attributes
    gamePaused = False
    
    #Pause Buttons
    resume = elements.button(resume_txt,(elements.relative(400,250)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
    options = elements.button(options_txt,(elements.relative(400,325)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
    exit = elements.button(exit_txt,(elements.relative(400,400)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
    
    #Exit Buttons
    yes = elements.button(yes_txt,(elements.relative(300,300)),(elements.relative(125,65)),('#333333','#FFFFFF'),(5,5))
    no = elements.button(no_txt,(elements.relative(500,300)),(elements.relative(125,65)),('#333333','#FFFFFF'),(5,5))
    
    #Option Buttons
    display = elements.button(display_txt,(elements.relative(169,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    audio = elements.button(audio_txt,(elements.relative(323,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    controls = elements.button(controls_txt,(elements.relative(477,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    profile = elements.button(profile_txt,(elements.relative(631,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    
    
    #Option Dropdowns
    displaymode = elements.dropdown(['FULLSCREEN','WINDOWED','BORDERLESS'], (elements.relative(180, 35)), (elements.relative(657,239)), 'WINDOWED')
    resolution = elements.dropdown(['2560 x 1440','1920 x 1080','1280 x 720', '800 x 600', '640 x 480', '500 x 500'], (elements.relative(180, 35)), (elements.relative(657,314)), '800 x 600')
    
    displaymode.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
    resolution.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
        #Navigation
    #Menus
    menu = 'null'
    setting = 'display'
    
    #Settings up level
    #screen = pygame.display.set_mode((1200,700),pygame.RESIZABLE)
    clock = pygame.time.Clock()
    level = Level(level_map, surface)
    
    #Setters (no not that kind).
    Fullscreen = False
    Borderless = False
    Windowed = True
    
    while True:
        
        surface.fill((121,128,241))
        print(gamePaused, menu, setting)
        #Paused
        if gamePaused == True:
            if menu == 'paused':
                setting = 'display'
                
                elements.draw_text('PAUSED', header, '#FFFFFF', surface, (elements.relative(400,150)),'center')
                
                if resume.checkClick(surface, True) == True:
                    gamePaused = False
                if options.checkClick(surface, True) == True:
                    menu = 'options'
                if exit.checkClick(surface, True) == True:
                    menu = 'exit'
                
            #Options
            if menu == 'exit':
                elements.draw_text('ARE YOU SURE?', header, '#FFFFFF', surface, (elements.relative(400,200)),'center')

                if yes.checkClick(surface, True) == True:
                    pygame.QUIT()
                    sys.exit()
                    
                if no.checkClick(surface, True) == True:
                    menu = 'paused'

            if menu == 'options':
                elements.draw_text('OPTIONS', header, '#FFFFFF', surface, (elements.relative(400,75)),'center')
                elements.draw_box(surface,(elements.relative(400,140)), (elements.relative(610,46)), '#6169f2', 10, 'center')
                
                if display.checkClick(surface, True) == True:
                    setting = 'display'
                if audio.checkClick(surface, True) == True:
                    setting = 'audio'
                if controls.checkClick(surface, True) == True:
                    setting = 'controls'
                if profile.checkClick(surface, True) == True:
                    setting = 'profile'
                    
                    
                if setting == 'display':
                    display.active('#FF0000')
                    #Display Menu
                    elements.draw_box(surface,(elements.relative(400,240)), (elements.relative(700,40)), '#6169f2', 2, 'center')
                    elements.draw_box(surface,(elements.relative(400,315)), (elements.relative(700,40)), '#6169f2', 2, 'center')
                    elements.draw_text('WINDOW MODE', sub, '#FFFFFF', surface, (elements.relative(60,240)),'midleft')
                    elements.draw_text('RESOLUTION', sub, '#FFFFFF', surface, (elements.relative(60,315)),'midleft')
                    
                    displaymode.checkClick(surface,True, '#888888')
                
                    if displaymode.getActive() == 'FULLSCREEN':
                        if Fullscreen == False:
                            surface = pygame.display.set_mode((hardwareDisp), pygame.FULLSCREEN)
                            Fullscreen = True
                    else:
                        Fullscreen = False
                        
                    if displaymode.getActive() == 'BORDERLESS':
                        if Borderless == False:
                            os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
                            surface = pygame.display.set_mode((hardwareDisp), NOFRAME)
                            Borderless = True
                    else:
                        Borderless = False
                    
                    if displaymode.getActive() == 'WINDOWED':
                        if Windowed == False:
                            surface = pygame.display.set_mode((1920,1080), RESIZABLE)
                            Windowed = True
                    else:
                        Windowed = False
                    
                if setting == 'audio':
                    audio.active('#FF0000')
                    
                    #Audio Menu
                    elements.draw_text('Master', sub, '#FFFFFF', surface, (elements.relative(100,200)), 'topleft')
                    
                if setting == 'controls':
                    controls.active('#FF0000')
                    #Controls Menu
                    
                if setting == 'profile':
                    profile.active('#FF0000')
                    #Profile Menu

        else:
            
            #GAME GOES HERE?
            #* I understand that there are better ways to make the game run alongside the menus, but since this is python and since this is last minute this will have to do.
            #* Given the chance to re-do things (if I hadn't already), I would make methods for both the menus and game, where the inputs are grabbed by main and then sent to load, logic and draw functions, ending with a screen update. (following proper game loops.)
            #---------------
            
            level.play()

            
        #Handles events such as window resizing and exiting
        for event in pygame.event.get():
                
            if event.type == pygame.VIDEORESIZE:
                print('resize')
                if Fullscreen == False:
                    surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    
                #Adjusting size of buttons and menus (that have predefined size and pos outside of a loop)
                 #TODO (NOT-TODO) Anthing below happens when the window is resized
                 #! This is super dumb but this is how things resize, I'm also putting this in red to help divide things..
                
                print(elements.relativeNum(20))
                print(round(elements.relativeNum(20)))
                
                #CONTENT
                resume_txt = ('RESUME',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                options_txt = ('OPTIONS',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                exit_txt = ('EXIT',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                
                display_txt = ('DISPLAY',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                audio_txt = ('SOUND',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                controls_txt = ('CONTROLS',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                profile_txt = ('PROFILE',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                
                yes_txt = ('YES',(round(elements.relativeNum(30))),'#FFFFFF','arialblack',True)
                no_txt = ('NO',(round(elements.relativeNum(30))),'#FFFFFF','arialblack',True)
                
                #PAUSE BUTTONS
                resume = elements.button(resume_txt,(elements.relative(400,250)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
                options = elements.button(options_txt,(elements.relative(400,325)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
                exit = elements.button(exit_txt,(elements.relative(400,400)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
                
                #EXIT BUTTONS
                yes = elements.button(yes_txt,(elements.relative(300,300)),(elements.relative(125,65)),('#333333','#FFFFFF'),(5,5))
                no = elements.button(no_txt,(elements.relative(500,300)),(elements.relative(125,65)),('#333333','#FFFFFF'),(5,5))
                
                #OPTION BUTTONS
                display = elements.button(display_txt,(elements.relative(169,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                audio = elements.button(audio_txt,(elements.relative(323,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                controls = elements.button(controls_txt,(elements.relative(477,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                profile = elements.button(profile_txt,(elements.relative(631,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                
                #Option Dropdowns
                displaymode = elements.dropdown(['FULLSCREEN','WINDOWED','BORDERLESS'], (elements.relative(180, 35)), (elements.relative(657,239)), displaymode.getActive())
                resolution = elements.dropdown(['2560 x 1440','1920 x 1080','1280 x 720', '800 x 600', '640 x 480', '500 x 500'], (elements.relative(180, 35)), (elements.relative(657,315)), '800 x 600')
                
                displaymode.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',(round(elements.relativeNum(12))),2)
                resolution.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',(round(elements.relativeNum(12))),2)
                
                #FONTS
                regular = pygame.font.SysFont('arialblack',(round(elements.relativeNum(40))))
                sub = pygame.font.SysFont('arialblack',(round(elements.relativeNum(20))))
                header = pygame.font.SysFont('arialblack',(round(elements.relativeNum(60))))
              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if menu == 'paused':
                        menu = 'null'
                        gamePaused = False
                    else:
                        menu = 'paused'
                        gamePaused = True
                        
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()


        #Believe it or not this updates the display...
        pygame.display.update()
        #This ticks the clock.
        clock.tick(60)