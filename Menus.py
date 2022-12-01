import pygame, sys, elements, os, json, webbrowser
from settings import *
from sprites import *
from level import Level
from pygame.locals import *

#Add menu functions / classes here instead of Main
def mainMenu():
    hardwareDisp = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    app_icon = pygame.image.load('JumpGame/Assets/Icons/AI.png')
    pygame.display.set_icon(app_icon)

    clock = pygame.time.Clock()

    pygame.display.set_caption('Start')
    surface = pygame.display.set_mode((400,450), NOFRAME)
    pygame.display.set_mode((400,450),NOFRAME)

    header = pygame.font.SysFont('arialblack',70)
    sub = pygame.font.SysFont('arialblack',25)
    reg = pygame.font.SysFont('arialblack',17)
    button = 30
    bSize = (269,55)
        #BUTTON THINGS
    #Image
    logoLoad = pygame.image.load('JumpGame/Assets/Icons/AI.png')
    logoimg = (logoLoad,0.05)
    #Text
    startTxt = ('PLAY',button,'#FFFFFF','arialblack',True)
    creditsTxt = ('CREDITS',button,'#FFFFFF','arialblack',True)
    exitTxt = ('EXIT',button,'#FFFFFF','arialblack',True)
    backTxt = ('BACK',button,'#FFFFFF','arialblack',True)
    #Element
    start = elements.button(startTxt,(200,190),bSize,('#333333','#FFFFFF'),(5,5))
    credits = elements.button(creditsTxt,(200,280),bSize,('#333333','#FFFFFF'),(5,5))
    exit = elements.button(exitTxt,(200,370),bSize,('#333333','#FFFFFF'),(5,5))
    back = elements.button(backTxt,(200,370),bSize,('#333333','#FFFFFF'),(5,5))
    logo = elements.button(logoimg,(200,250),('image','image'),('#333333','#FFFFFF'),(5,5))
    cred = False

    while True:
        surface.fill((121,128,241))
        elements.draw_box(surface,(200,125), (340,310), '#6169f2', 5, 'midtop')
        if cred != True:
            elements.draw_text('JUMPR', header, '#FFFFFF', surface, (200, 60))
            elements.draw_text('(For lack of a better name)', reg, '#FFFFFF', surface, (200, 102))
            
            
            if start.checkClick(surface, True) == True:
                run(clock,hardwareDisp)
                break
            if credits.checkClick(surface,True):
                cred = True
            if exit.checkClick(surface,True) == True:
                pygame.quit()
                sys.exit()
        
        else:
            elements.draw_text('CREDITS', header, '#FFFFFF', surface, (200, 60))
            elements.draw_text('Kind of game but mostly menus by:', reg, '#FFFFFF', surface, (200, 110))
            elements.draw_text('ARTIFICIAL IDIOTS', sub, '#FFFFFF', surface, (200, 160))
            
            if logo.checkClick(surface,True) == True:
                webbrowser.open('https://github.com/Nandez22/text-game')
            if back.checkClick(surface,True) == True:
                cred = False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def run(clock,disp):
    hardwareDisp = disp
    try:
        with open('JumpGame/Save/settings.json') as saveFile:
            settings = json.load(saveFile)
    except:
        settings = {
            'displayData':{
                'displaymode':'WINDOWED',
                'resolution':'800 x 600'},
            'audioData':{
                'master':50,
                'music':50,
                'sfx':50,
                'device':'DEFAULT'}}

    loadDisplay = settings['displayData']['displaymode']
    loadResolution = settings['displayData']['resolution']
    loadMaster = settings['audioData']['master']
    loadMusic = settings['audioData']['music']
    loadSfx = settings['audioData']['sfx']
    loadDevice = settings['audioData']['device']
    
    if loadDisplay == 'FULLSCREEN':
        loadResolution = f'{hardwareDisp[0]} x {hardwareDisp[1]}'
    if loadResolution == f'{hardwareDisp[0]} x {hardwareDisp[1]}':
        loadDisplay = 'FULLSCREEN'

    
        #ASSETS
    #Display
    mode = elements.getMode(loadDisplay)
    if mode == FULLSCREEN:
        res = hardwareDisp
    res = elements.getRes(loadResolution)
    
    surface = pygame.display.set_mode(res,mode)
            
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
    
    exitMainTxt = ('MAIN MENU',20,'#FFFFFF','arialblack',True)
    exitDeskTxt = ('DESKTOP',20,'#FFFFFF','arialblack',True)
    exitCancelTxt = ('CANCEL',20,'#FFFFFF','arialblack',True)
    
    #Images
    

    #Attributes
    gamePaused = False
    
    #Pause Buttons
    resume = elements.button(resume_txt,(elements.relative(400,250)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
    options = elements.button(options_txt,(elements.relative(400,325)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
    exit = elements.button(exit_txt,(elements.relative(400,400)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
    
    #Exit Buttons
    exitMain = elements.button(exitMainTxt,(elements.relative(400,250)),(elements.relative(225,50)),('#333333','#FFFFFF'),(5,5))
    exitDesk = elements.button(exitDeskTxt,(elements.relative(400,325)),(elements.relative(225,50)),('#333333','#FFFFFF'),(5,5))
    exitCancel = elements.button(exitCancelTxt,(elements.relative(400,400)),(elements.relative(225,50)),('#222222','#FFFFFF'),(5,5))
    
    #Option Buttons
    display = elements.button(display_txt,(elements.relative(169,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    audio = elements.button(audio_txt,(elements.relative(323,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    controls = elements.button(controls_txt,(elements.relative(477,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
    profile = elements.button(profile_txt,(elements.relative(631,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))

    #Option Dropdowns
    displaymode = elements.dropdown(['FULLSCREEN','WINDOWED','BORDERLESS'], (elements.relative(180, 35)), (elements.relative(657,239)), loadDisplay)
    resolution = elements.dropdown(['2560 x 1440','1920 x 1080','1280 x 720', '800 x 600', '640 x 480', '500 x 500'], (elements.relative(180, 35)), (elements.relative(657,314)), loadResolution)
    displaymode.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
    resolution.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
    
    outDevice = elements.dropdown(['DEFAULT','LIST','HERE','OF','AVALIBLE','AUDIO','DEVICES'],(elements.relative(180, 35)), (elements.relative(657,399)), loadDevice)
    outDevice.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
    
    #Option Sliders
    master = elements.slider(surface, ((121,128,241),'#FFFFFF'), (elements.relative(500,240)))
    music = elements.slider(surface, ((121,128,241),'#FFFFFF'), (elements.relative(500,240)))
    sfx = elements.slider(surface, ((121,128,241),'#FFFFFF'), (elements.relative(500,240)))
    
    #Text Fields
    masterTxt = elements.txtField(('#333333','#FFFFFF'),loadMaster)
    musicTxt = elements.txtField(('#333333','#FFFFFF'),loadMusic)
    sfxTxt = elements.txtField(('#333333','#FFFFFF'),loadSfx)
        #Navigation
    #Menus
    menu = 'null'
    setting = 'display'
    
    #Settings up level
    clock = pygame.time.Clock()
    level = Level(level_map, surface)
    
    #Setters (no not that kind).
    Fullscreen = False
    Borderless = False
    Windowed = True
    
    update = False
    firstItt = True
    isThisTheFirstItterationForASecondTimeBecauseIProgrammedThegetValFunctionForTheSliderClassPoorlySoINeedToRelyOnTwoVariablesToCountTheInitialItterationOfTheLoopBecauseIAmABadProgrammer = True
    usrQuit =False
    save = False
    
#! BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- 
    while True:
        if isThisTheFirstItterationForASecondTimeBecauseIProgrammedThegetValFunctionForTheSliderClassPoorlySoINeedToRelyOnTwoVariablesToCountTheInitialItterationOfTheLoopBecauseIAmABadProgrammer == True:
            update = True
            isThisTheFirstItterationForASecondTimeBecauseIProgrammedThegetValFunctionForTheSliderClassPoorlySoINeedToRelyOnTwoVariablesToCountTheInitialItterationOfTheLoopBecauseIAmABadProgrammer = False
            
        if elements.getRes(resolution.getActive()) != res:
            res = elements.getRes(resolution.getActive())
            if res == hardwareDisp:
                displaymode.setActive('FULLSCREEN')
            surface = elements.set_screen(res,'Jumpr - Paused', elements.getMode(displaymode.getActive()))
            update = True

            
        
        surface.fill((121,128,241))
        #Paused
        if gamePaused == True:
            pygame.display.set_caption('Jumpr - Paused')
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
                elements.draw_text('EXIT GAME ', header, '#FFFFFF', surface, (elements.relative(400,150)),'center')

                if exitMain.checkClick(surface, True) == True:
                    save = True
                    mainMenu()
                    break
                    
                if exitDesk.checkClick(surface, True) == True:
                    save = True
                    usrQuit = True
                    
                if exitCancel.checkClick(surface,True) == True:
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
                    
                    resolution.checkClick(surface,True)
                    displaymode.checkClick(surface,True)
                    
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
                    
                    elements.draw_box(surface,(elements.relative(400,290)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('MUSIC', sub, '#FFFFFF', surface, (elements.relative(60,290)),'midleft')
                    
                    elements.draw_box(surface,(elements.relative(400,340)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('SFX', sub, '#FFFFFF', surface, (elements.relative(60,340)),'midleft')
                    
                    master.addStroke([2,'#000000'],[0])
                    master.draw((elements.relative(200,12)),((elements.relativeNum(8))),(elements.relative(565,240)),((round(elements.relativeNum(5)),round(elements.relativeNum(5)))))
                    masterTxt.draw(surface,(elements.relative(715,240)),(elements.relative(60,30)),(regular,(round(elements.relativeNum(1))),(round(elements.relativeNum(2)))))
                         
                    sfx.addStroke([2,'#000000'],[0])
                    sfx.draw((elements.relative(200,12)),((elements.relativeNum(8))),(elements.relative(565,290)),((round(elements.relativeNum(5)),round(elements.relativeNum(5)))))
                    sfxTxt.draw(surface,(elements.relative(715,290)),(elements.relative(60,30)),(regular,(round(elements.relativeNum(1))),(round(elements.relativeNum(2)))))
                    
                    music.addStroke([2,'#000000'],[0])
                    music.draw((elements.relative(200,12)),((elements.relativeNum(8))),(elements.relative(565,340)),((round(elements.relativeNum(5)),round(elements.relativeNum(5)))))
                    musicTxt.draw(surface,(elements.relative(715,340)),(elements.relative(60,30)),(regular,(round(elements.relativeNum(1))),(round(elements.relativeNum(2)))))
                    
                    elements.draw_box(surface,(elements.relative(400,400)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('AUDIO DEVICE', sub, '#FFFFFF', surface, (elements.relative(60,400)),'midleft')
                    
                    outDevice.checkClick(surface,True)
                    
                    if firstItt == True:
                        master.setVal(loadMaster)
                        music.setVal(loadMusic)
                        sfx.setVal(loadSfx)
                        firstItt = False
                        
                if setting == 'controls':
                    controls.active('#FF0000')
                    #Controls Menu
                    
                if setting == 'profile':
                    profile.active('#FF0000')
                    #Profile Menu

        else:
            pygame.display.set_caption('Jumpr')
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
                    musicTxt.edit(event, music, (True,'#444444'), (round(elements.relativeNum(2)),'#FF0000'))
                    sfxTxt.edit(event, sfx, (True,'#444444'), (round(elements.relativeNum(2)),'#FF0000'))
                    
            if event.type == pygame.VIDEORESIZE or update == True or event.type == FULLSCREEN:
                master.setX(elements.relativeNum(master.getX()))
                music.setX(elements.relativeNum(music.getX()))
                sfx.setX(elements.relativeNum(sfx.getX()))
                #CONTENT
                resume_txt = ('RESUME',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                options_txt = ('OPTIONS',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                exit_txt = ('EXIT',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                
                display_txt = ('DISPLAY',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                audio_txt = ('SOUND',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                controls_txt = ('CONTROLS',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                profile_txt = ('PROFILE',(round(elements.relativeNum(15))),'#FFFFFF','arialblack',True)
                
                exitMainTxt = ('MAIN MENU',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                exitDeskTxt = ('DESKTOP',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                exitCancelTxt = ('CANCEL',(round(elements.relativeNum(20))),'#FFFFFF','arialblack',True)
                
                #PAUSE BUTTONS
                resume = elements.button(resume_txt,(elements.relative(400,250)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
                options = elements.button(options_txt,(elements.relative(400,325)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
                exit = elements.button(exit_txt,(elements.relative(400,400)),(elements.relative(200,50)),('#333333','#FFFFFF'),(5,5))
                
                #EXIT BUTTONS
                exitMain = elements.button(exitMainTxt,(elements.relative(400,250)),(elements.relative(225,50)),('#333333','#FFFFFF'),(5,5))
                exitDesk = elements.button(exitDeskTxt,(elements.relative(400,325)),(elements.relative(225,50)),('#333333','#FFFFFF'),(5,5))
                exitCancel = elements.button(exitCancelTxt,(elements.relative(400,400)),(elements.relative(225,50)),('#222222','#FFFFFF'),(5,5))
                
                #OPTION BUTTONS
                display = elements.button(display_txt,(elements.relative(169,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                audio = elements.button(audio_txt,(elements.relative(323,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                controls = elements.button(controls_txt,(elements.relative(477,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                profile = elements.button(profile_txt,(elements.relative(631,140)),(elements.relative(130,30)),('#333333','#FFFFFF'),(5,1))
                
                #Option Dropdowns
                displaymode = elements.dropdown(['FULLSCREEN','WINDOWED','BORDERLESS'], (elements.relative(180, 35)), (elements.relative(657,240)), displaymode.getActive())
                resolution = elements.dropdown(['2560 x 1440','1920 x 1080','1280 x 720', '800 x 600', '640 x 480', '500 x 500'], (elements.relative(180, 35)), (elements.relative(657,315)), resolution.getActive())
                outDevice = elements.dropdown(['DEFAULT','LIST','HERE','OF','AVALIBLE','AUDIO','DEVICES'],(elements.relative(180, 35)), (elements.relative(657,400)), outDevice.getActive())
                
                displaymode.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',(round(elements.relativeNum(12))),2)
                resolution.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',(round(elements.relativeNum(12))),2)
                outDevice.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',(round(elements.relativeNum(12))),2)
                
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
                        
            if save == True:
                with open('JumpGame/Save/settings.json','w') as saveFile:
                    settings = {
                        'displayData':{
                            'displaymode':displaymode.getActive(),
                            'resolution':resolution.getActive()},
                        'audioData':{
                            'master':masterVal,
                            'music':musicVal,
                            'sfx':sfxVal,
                            'device':outDevice.getActive()}
                    }
                    json.dump(settings, saveFile, indent = 6)
                    saveFile.close()
                        
            if event.type == pygame.QUIT or usrQuit == True:
                
                try:
                    masterVal = master.getVal()
                    musicVal = music.getVal()
                    sfxVal = sfx.getVal()
                except:
                    masterVal = loadMaster
                    musicVal = loadMusic
                    sfxVal = loadSfx

                with open('JumpGame/Save/settings.json','w') as saveFile:
                    settings = {
                        'displayData':{
                            'displaymode':displaymode.getActive(),
                            'resolution':resolution.getActive()},
                        'audioData':{
                            'master':masterVal,
                            'music':musicVal,
                            'sfx':sfxVal,
                            'device':outDevice.getActive()}
                    }
                    json.dump(settings, saveFile, indent = 6)
                    saveFile.close()
                    
                pygame.QUIT()
                sys.exit()

        #Believe it or not this updates the display...
        #* Refreshes everything thats supposed to be there.
            #* Without display just sits there black, hence the need for a literal game loop.
        pygame.display.update()
        #This ticks the clock.
        #* Ticks are the game speed, measured by tps, ever play Minecraft?
        clock.tick(60)