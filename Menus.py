import pygame, sys, elements
from settings import *
from sprites import *
from level import Level


#Add menu functions / classes here instead of Main
def pause(clock):
    
    
        #ASSETS
    #Display
    surface = elements.set_screen((800,600),'Paused',True)
    
    #Fonts
    regular = pygame.font.SysFont('arialblack',40)
    sub = pygame.font.SysFont('arialblack',20)
    header = pygame.font.SysFont('arialblack',60)
    
        #BUTTONS
    #Text
    resume_txt = ('Resume',20,'#FFFFFF','arialblack',True)
    options_txt = ('Options',20,'#FFFFFF','arialblack',True)
    exit_txt = ('Exit',20,'#FFFFFF','arialblack',True)
    
    display_txt = ('Display',15,'#FFFFFF','arialblack',True)
    audio_txt = ('Sound',15,'#FFFFFF','arialblack',True)
    controls_txt = ('Controls',15,'#FFFFFF','arialblack',True)
    profile_txt = ('Profile',15,'#FFFFFF','arialblack',True)
    
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
    display = elements.button(display_txt,(elements.relative(169,125)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    audio = elements.button(audio_txt,(elements.relative(323,125)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    controls = elements.button(controls_txt,(elements.relative(477,125)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    profile = elements.button(profile_txt,(elements.relative(631,125)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    
    test = elements.button(yes_txt,(elements.relative(400,300)),(elements.relative(125,65)),('#333333','#FFFFFF'),(5,5))
    
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
    screen = pygame.display.set_mode((1200,700),pygame.RESIZABLE)
    clock = pygame.time.Clock()
    level = Level(level_map, screen)
    
    
    
    while True:
        
        surface.fill((121,128,241))
        
        #Paused
        if gamePaused == True:
            if menu == 'paused':
                setting = 'display'
                
                elements.draw_text('PAUSED', header, '#FFFFFF', surface, (elements.relative(400,150)),'center')
                
                resume.draw(surface)
                options.draw(surface)
                exit.draw(surface)
                
                test.draw(surface)
                
                if resume.checkClick(True) == True:
                    gamePaused = False
                if options.checkClick(True) == True:
                    menu = 'options'
                if exit.checkClick(True) == True:
                    menu = 'exit'
                    
            #Options
            if menu == 'exit':
                elements.draw_text('ARE YOU SURE?', header, '#FFFFFF', surface, (elements.relative(400,200)),'center')

                yes.draw(surface)
                no.draw(surface)
                
                if yes.checkClick(True) == True:
                    pygame.QUIT()
                    sys.exit()
                    
                if no.checkClick(True) == True:
                    menu = 'paused'

            if menu == 'options':
                elements.draw_text('OPTIONS', header, '#FFFFFF', surface, (elements.relative(400,75)),'center')
                elements.draw_box(surface,(elements.relative(400,140)), (elements.relative(610,46)), '#6169f2', 10, 'center')
                
                display.draw(surface)
                audio.draw(surface)
                controls.draw(surface)
                profile.draw(surface)
                
                if display.checkClick(True) == True:
                    setting = 'display'
                if audio.checkClick(True) == True:
                    setting = 'audio'
                if controls.checkClick(True) == True:
                    setting = 'controls'
                if profile.checkClick(True) == True:
                    setting = 'profile'
                    
                    
                if setting == 'display':
                    display.active('#FF0000')
                    #Display Menu
                    elements.draw_box(surface,(elements.relative(400,240)), (elements.relative(700,40)), '#6169f2', 2, 'center')
                    elements.draw_box(surface,(elements.relative(400,315)), (elements.relative(700,40)), '#6169f2', 2, 'center')
                    
                    resolution.draw(surface)
                    resolution.drop(True)
                    resolution.checkClick()
                    
                    displaymode.draw(surface)
                    displaymode.drop(True)
                    displaymode.checkClick()
                    
                    elements.draw_text('WINDOW MODE', sub, '#FFFFFF', surface, (elements.relative(60,225)),'topleft')
                    elements.draw_text('RESOLUTION', sub, '#FFFFFF', surface, (elements.relative(60,300)),'topleft')
                    
                    
                    
                    
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


        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamePaused = True
                    menu = 'paused'
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(60)