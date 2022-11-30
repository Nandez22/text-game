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
    regular = pygame.font.SysFont('arialblack',15)
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
    
    #Option Sliders
    master = elements.slider(surface, ((121,128,241),'#FFFFFF'), (elements.relative(500,240)))
    
    #Text Fields
    masterTxt = elements.txtField(('#333333','#FFFFFF'),'50')
    
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
    
    update = False
    
    while True:
        surface.fill((121,128,241))
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
                            update = True
                    else:
                        Fullscreen = False
                        
                    if displaymode.getActive() == 'BORDERLESS':
                        if Borderless == False:
                            
                            surface = pygame.display.set_mode((hardwareDisp), NOFRAME)
                            Borderless = True
                            update = True
                    else:
                        Borderless = False
                    
                    if displaymode.getActive() == 'WINDOWED':
                        if Windowed == False:
                            surface = pygame.display.set_mode((1920,1080), RESIZABLE)
                            Windowed = True
                            update = True
                    else:
                        Windowed = False
                    
                if setting == 'audio':
                    audio.active('#FF0000')
                    #Audio Menu
                    elements.draw_box(surface,(elements.relative(400,240)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('MASTER', sub, '#FFFFFF', surface, (elements.relative(60,240)),'midleft')
                    
                    master.addStroke([2,'#000000'],[1,'#000000'])
                    master.draw((elements.relative(200,12)),((elements.relativeNum(8))),(elements.relative(565,240)),((round(elements.relativeNum(5)),round(elements.relativeNum(5)))))
                    masterTxt.draw(surface,(elements.relative(715,240)),(elements.relative(60,30)),(regular,(round(elements.relativeNum(1))),(round(elements.relativeNum(2)))))
                         
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
            #* Actually it was more of a me thing... I digress (again), if I had a complaint about how I did something it would be the section up next...
            #---------------
            
            level.play()

        
        #Handles events such as window resizing and exiting
        #* I hate this
            #* - This section of the program not the comments, I love the comments.
            #I hope this section looks familiar because it is. One thing I lacked when making a dropdown menu / buttons was foresight.
                #I didn't realize that to make things scale properly with window resizes I needed to initialize them within the game loop, or at least the size and pos for each (among other items).
                #This sucks because I'm not completley redoing the button for a 3rd time, nor am I making heavy modifications for the 1000th.
                #Again, heindsight is 50/50 and although this is not elegant by any means, it at least allows me to adjust things for screen size.
                
            #Ranting aside it works as follows:
            #   - Starts when the window changes states (event.type == pygame.VIDEORESIZE) or when the update var is triggered (update == True)\
            #   - At that point all items that are not initialized within the game loop (everything listed below) will re-initalize to adjust for the new screen size.
            #   - This mostly uses two functions that I wrote that take the ratio of a number (or number set) compared to the origin window (800 x 600) and apply it to the new window size
            #       - These functions are super simple, I'm just stating this so there is no need to wander all the way to elements.py (trust me you don't want to go there.)
            #   - Once it is done re-initalizing it resets the update var to false (if the game reinitializes every loop itteration everything breaks, not to mention is horribly slow)
            #       - Thats done to prevent the game from constantly re-initalizing the on screen elements (as stated above; I just ran out of space and hate scrolling).
        for event in pygame.event.get():
            if gamePaused == True:
                if setting == 'audio':
                    masterTxt.edit(event, master, (True,'#444444'), (round(elements.relativeNum(2)),'#FF0000'))
                        
            if event.type == pygame.VIDEORESIZE or update == True:
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
                regular = pygame.font.SysFont('arialblack',(round(elements.relativeNum(15))))
                sub = pygame.font.SysFont('arialblack',(round(elements.relativeNum(20))))
                header = pygame.font.SysFont('arialblack',(round(elements.relativeNum(60))))
                
                #RESET
                update = False
            
            # This handles the user input, well some of it. (Actually its handled really inconsistantly and doesn't follow proper game loop flow what so ever).
            #   Works as follows:
            #   - Looks to see if a key is pressed
            #   - If so, what key
            #   - If key is the escape key do something
            #   - Something is tell the game to go to the paused menu
            #       - If the game is already there go back to the game
            #       - If game is not there bring it there
            
            #   - If the user quits game (hits 'X' on window or alt f4's, etc.)
            #       - Quit
            #       - Exit (quit but with a different package)
            
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
        #* Refreshes everything thats supposed to be there.
            #* Without display just sits there black, hence the need for a literal game loop.
        pygame.display.update()
        #This ticks the clock.
        #* Ticks are the game speed, measured by tps, ever play Minecraft?
        clock.tick(60)