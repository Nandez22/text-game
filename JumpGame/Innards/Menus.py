import pygame, sys, elements, os, json, webbrowser
from settings import *
from sprites import *
from level import Level
from pygame.locals import *

# ^ Imports for stuff to work ^
#* Things like pygame locals need full import for quality of life, hence why its a seperate package and almost all variables from it are in ALLCAPS
#* I'd also prefer it if settings, sprites and level were not fully imported either but I was being lazy when following the tutorial and didn't want to rewrite a bunch of stuff
#! Antthing to do with elements."something" will be explained further in depth in 'elements.py', if you need further explination go there.
#Add menu functions / classes here instead of Main
#This opens the main menu and is the first thing called upon running main (outside of package initilizations)
def mainMenu():
    #Hardware display is here to capture the resolution of the users main or current monitor #*(have not tested monitor switching but I am using two)
    #Typically when you use 'pygame.display.Info()' it grabs the size of the current window, but since no window has been generated yet, pygame grabs the display dimensions instead (thats why it needs to be passed into run() to be used) 
    hardwareDisp = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    #Sets app icon
    app_icon = pygame.image.load('JumpGame/Assets/Icons/AI.png')
    pygame.display.set_icon(app_icon)
    #initilizes game clock
    clock = pygame.time.Clock()

    #Sets up start menu window (400 x 450 and borderless (NOFRAME) with no option to change, captioned 'Start' (which is redundent since you can't see the border))
    pygame.display.set_caption('Start')
    surface = pygame.display.set_mode((400,450), NOFRAME)
    pygame.display.set_mode((400,450),NOFRAME)

    #Declaring some basic text styles for use ('fontName',size)
    header = pygame.font.SysFont('arialblack',70)
    sub = pygame.font.SysFont('arialblack',25)
    reg = pygame.font.SysFont('arialblack',17)
    #These are attributes of the buttons below so I didn't have to keep resizing them individually.
    #Button is font size and bSize is the size of the buttons
    button = 30
    bSize = (269,55)
    
    #* Instead of explaining buttons line by line I am just going to explain them here, and will refrence this section upon encountering other buttons (or not)
        #* Buttons require a few parts
            #* -1. Content -- The specifics of content depends on what you want on the button, (image or text)
                    #* IMAGE BUTTON content
                        #* -1. Image file (must first import image with 'pygame.image.load('imagePath')') 
                        #* -2. Image scale or size, depending on if it recieves a single int or a tuple it will either scale the image by the int(percent scale), or to the size given as (width,height)
                    #* TEXT BUTTON content
                        #* -1. Text ('strText')
                        #* -2. Font Size (size)
                        #* -3. Text color (can be hex or RGB but RGB must be given as a Tuple ((r,g,b))*)
                        #* -4. Font Name ('fontName'), here I've elected to use system fonts, so there is a chance that some instances of this game will not work (need ArialBlack)
                        #* -5. Anti-Aliasing (True if you want a smooth looking typeface, else for a more pixilated one turn to False)
            #* -2. Position -- Given as (xPos, yPos)
            #* -3. Size -- Dependent on content
                    #* IMAGE BUTTON size (respective to the size of the button surface not size of image (will make more sense if you get to 'elements.py')) THERE ARE TWO OPTIONS:
                        #* -1. ('image','image') -- Will make top of button the same size as the image meaning no background will show (unless your image has alpha channles and transparency)
                        #* -2. (width, height) -- Will make top of button the width and height provided (can be smaller or larger than image)
                    #*TEXT BUTTON size
                        #* (Width, Height) -- Will make top of button width and height provided
            #* -4. Colors -- Given as ('primary','secondary') (primary being the top surface of button and secondary being the "chin" (if elevation > 0))
            #* -5. Modifiers -- Given as (cornerRadius, elevation) (cornerRadius being the radius of the corners of the rectangular buttons, elevation being the size of the "chin" (makes the button look 3D))
            
        #BUTTON THINGS
    #Image
    # Loads Image
    #* Should be noted that using "\"'s in the image path works on windows but breaks on macos, but "/"'s work on both curiously.
    logoLoad = pygame.image.load('JumpGame/Assets/Icons/AI.png')
    logoimg = (logoLoad,0.05)
    #Text
    #* The rest of this is button stuff, see above
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
    #Toggle for the credits menu
    cred = False

    #Pygame needs evething to be looped to display properly, hence the while loop
    while True:
        #Sets the background color
        surface.fill((121,128,241))
        #This draws a rect (rectangle) on screen, Its explained further in elements but I'll give it a small go here
        #elements.draw_bos(surfaceToDrawOn, (xPosition, yPosition), (width, height), color, borderRadius, anchor point)
        elements.draw_box(surface,(200,125), (340,310), '#6169f2', 5, 'midtop')
        
        #If the credit button has NOT been pressed...
        if cred != True:
            #Setting basic UI elements
            elements.draw_text('JUMPR', header, '#FFFFFF', surface, (200, 60))
            #This draws text, fun!
            #I'll also explain how this work further in 'elements.py' but heres the basics...
            #elements.draw_text('textToDisplay', font(designated aboce), textColor, surfaceToDrawOn, (xPosition, yPosition))
            elements.draw_text('(For lack of a better name)', reg, '#FFFFFF', surface, (200, 102))
            
            #start is a button and .checkClick() is a button method that draws the button, and checks for hover and clicks
            #checkClick(surfaceToDraw, changeOnHover(optional, default False), hoverColor(optional, default red))
            #checkClick() returns true if a click has been detected.
            if start.checkClick(surface, True) == True:
                #This runs the main game function (found below)
                run(clock,hardwareDisp)
                #Then breaks the loop (which may be redundent as running the run() function opens a new while loop breaking the current one)
                break
            if credits.checkClick(surface,True):
                #Opens credits menu
                cred = True
            if exit.checkClick(surface,True) == True:
                #Quits the game in two ways
                #* Not sure why both but thats the standardl.
                    #? Sue Me.
                pygame.quit()
                sys.exit()
            #If the credits button has been pressed...    
        else:
            #Draw the title, subtitle and the credit info (group name)
            elements.draw_text('CREDITS', header, '#FFFFFF', surface, (200, 60))
            elements.draw_text('Kind of game but mostly menus by:', reg, '#FFFFFF', surface, (200, 110))
            elements.draw_text('ARTIFICIAL IDIOTS', sub, '#FFFFFF', surface, (200, 160))
            
            #Imports group logo #? yeah we have one... sue us.
            #If said logo gets clicked open link to the repository (idk we dont have a website and I'm bad at spelling what else was I supposed to do)
            if logo.checkClick(surface,True) == True:
                webbrowser.open('https://github.com/Nandez22/text-game')
            #If back button below logo button is pressed then return to the main menu
            if back.checkClick(surface,True) == True:
                cred = False

        #display.update() is necessary for anything related to pygame to run. Since it follows standard game loop (getInput --> updateContent --> updateDisplay -- Repeat)
        # -- The display must update each itteration to redraw whats there, or eles it will only display 1 frame once.
        pygame.display.update()
        
        #This cycles through all events, (problematic later)
        for event in pygame.event.get():
            #Looks to see if the game has been told to quit, either window 'X' pressed, pygame.QUIT is run or possibly alt+f4?
            #If so it will quit / forcibly crash the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#This is the meat and potatos now, if some explinations seem a little abreviated I am sorry but I recommend you check 'elements.py' where more in depth explinations of different "elements" can be found
    #*-- There is a metric fuck ton of messy code in hree and If I were to write 1+ lines per line in here we would break 1000 lines (inluding comments) and I don't want that to happen, since I ame still yet to write elements.py's comments
def run(clock,disp):
    #imports hardwareDisp mentioned earlier
    hardwareDisp = disp
    
    #This opens the save file, well tries to. If no save file exists the game used default settings designated under except:
    try:
        with open('JumpGame/Save/settings.json') as saveFile:
            settings = json.load(saveFile)
    except:
        print('fda')
        settings = {
            'displayData':{
                'displaymode':'WINDOWED',
                'resolution':'800 x 600'},
            'audioData':{
                'master':50,
                'music':50,
                'sfx':50,
                'device':'DEFAULT'}}

    #This converts the double dictionary into usable variables for ease of use while coding.
    loadDisplay = settings['displayData']['displaymode']
    loadResolution = settings['displayData']['resolution']
    loadMaster = settings['audioData']['master']
    loadMusic = settings['audioData']['music']
    loadSfx = settings['audioData']['sfx']
    loadDevice = settings['audioData']['device']
    
    #This is where some things are going to get redundet (specifically with display settings)
        #* Some work some don't which is why there are so many, as some would work in specific instances and I just kept adding them to cover the holes (them is code bits to make sure fullscreen and resolution play nice with eachother)
        #* Also a good time to mention... Borderless is shit on multimonitor and probably shit on single monitor as well, just avoid using it.
        #* (kinda my fault but also there is a lot on the internet saying that pygame is really bad at handling its 'NOFRAME' mode and can only be resolved using os, but that does other wierd things that I don't care to explain just trust that it didn't work)
    #* Enough said:
    #This checks to see if the players settings designate full screen. If so, it will match the resolution setting to their monitor
    #(resolution is not the res of textures like in most games, its actually the winndow size, but also if its glitched out properly it will streatch like a normal game would, but I took that out for consistancy)
    #It will then check to see if the resolution is the same as the display, if so it will set the display setting to full screen
    if loadDisplay == 'FULLSCREEN':
        loadResolution = f'{hardwareDisp[0]} x {hardwareDisp[1]}'
    if loadResolution == f'{hardwareDisp[0]} x {hardwareDisp[1]}':
        loadDisplay = 'FULLSCREEN'

    
        #ASSETS
    #Display
    #get mode gets the mode of the display, (not in str format)
    #Like I mentioned before this essencially does the same thing as above but instead of doing it to the save vars it does it to the active vars that actually change the window size and settings.
    mode = elements.getMode(loadDisplay)
    if mode == FULLSCREEN:
        res = hardwareDisp
    res = elements.getRes(loadResolution)
    
    #sets surface(window) to the settings loaded in and possibly manipulated above.
    surface = pygame.display.set_mode(res,mode)
            
    #Fonts
    regular = pygame.font.SysFont('arialblack',15)
    sub = pygame.font.SysFont('arialblack',20)
    header = pygame.font.SysFont('arialblack',60)
    
        #BUTTONS
    #*More button stuff; explained above and in 'elements.py'
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
    #Sets var to be used later
    gamePaused = False
    
    #*Again Buttons...
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

    #* Oh boy! Dropdowns :(
        #* I've said it before and I will say it again... Go to elements.py if you want to see how dropdowns actually work.
            #* This section will just be explaining how to initilize one and set it on screen.
    #DROPDOWN RUNDOWN
    #   Dropdowns need 4 things to initialize:
    #       1. List of options -- (list not Tuple) (items are strings)
    #       2. Size -- (width, height)
    #       3. Position -- (xPosition, yPosition)
    #       4. Default Value -- Must be an item from the list of options. (Exact same as one of the options)
            #See much easier than a button, unfortunatley there is a touch more...
    #   Dropdowns need 5 things to be styled properly: #* (should be mentioned that active refers to the item that is currently selected and inactive is all else)
    #       1. Rect Colors -- (rectangleActive, rectangleInactive)
    #       2. Text Colors -- (textActive, textInactive)
    #       3. Font -- str(fontName)
    #       4. Font Size -- int(fontSize)
    #       5. Border Radius -- float(borderRadius)

    #Option Dropdowns
    displaymode = elements.dropdown(['FULLSCREEN','WINDOWED','BORDERLESS'], (elements.relative(180, 35)), (elements.relative(657,239)), loadDisplay)
    resolution = elements.dropdown(['2560 x 1440','1920 x 1080','1280 x 720', '800 x 600', '640 x 480', '500 x 500'], (elements.relative(180, 35)), (elements.relative(657,314)), loadResolution)
    displaymode.style(('#333333', '#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
    resolution.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
    
    outDevice = elements.dropdown(['DEFAULT','LIST','HERE','OF','AVALIBLE','AUDIO','DEVICES'],(elements.relative(180, 35)), (elements.relative(657,399)), loadDevice)
    outDevice.style(('#333333','#444444'),('#FFFFFF','#e0e0e0'),'arialblack',12,2)
    
    #Option Sliders
    #? Annnnnd we didn't even make it 20 lines...
    #SLIDERS
    #   Sliders need 3 things to initialize #* Note that the long "range" that the slider is on I call the 'rail' and the dot you drag is the 'slider'
    #       1. Surface -- (surfaceToDrawOn) aka Window
    #       2. Colors -- (railPrimary, sliderSecondary)
    #       3. Position -- (xPosition, yPosition)
    # And thats it. See I've gotten a touch better at this...
    master = elements.slider(surface, ((121,128,241),'#FFFFFF'), (elements.relative(500,240)))
    music = elements.slider(surface, ((121,128,241),'#FFFFFF'), (elements.relative(500,240)))
    sfx = elements.slider(surface, ((121,128,241),'#FFFFFF'), (elements.relative(500,240)))
    
    #Text Fields
    #? Really?
    #TEXT FIELDS
    #   Text Fields need 2 things to initialize:
    #       1. Colors -- (rectColor, textColor)
    #       2. Default Value -- str('number')
    #* Better!
    #* Except not really, I kinda rushed making this, so it only really works in conjunction with sliders, sliders do not need text fields but text fields need sliders.
    masterTxt = elements.txtField(('#333333','#FFFFFF'),loadMaster)
    musicTxt = elements.txtField(('#333333','#FFFFFF'),loadMusic)
    sfxTxt = elements.txtField(('#333333','#FFFFFF'),loadSfx)
        #Navigation
    #* Here I'm creating variables that designate navigation, like where the user is in the menu and setting them to a default state
    #Menus
    menu = 'null'
    setting = 'display'
    
    #* initializing a new clock for some reason?
    #? genuinly not sure about this one, but I'm not going to remove it to be safe...
    level = Level(level_map, surface)
    
    #* Here im just making one off variables that the program needs defined before the loop, I feel there are too many, but I don't want to look into changing it.
    #Setters (no not that kind).
    Fullscreen = False
    #*Here I initialize some parts of the game, again since the game isn't really part of this project I'm not going to explain it.
        #? -- Not that I'm not explaining out of bad practice, but commenting is on the rubric and I don't feel its fair to have something graded that is basically copied from the internet.
    #Settings up level
    clock = pygame.time.Clock()
    Borderless = False
    Windowed = True
    
    update = False
    firstItt = True
    isThisTheFirstItterationForASecondTimeBecauseIProgrammedThegetValFunctionForTheSliderClassPoorlySoINeedToRelyOnTwoVariablesToCountTheInitialItterationOfTheLoopBecauseIAmABadProgrammer = True
    usrQuit =False
    saveData = False
    retrunMain = False
    
#! BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- BIG RED LINE SO I CAN SEE WHERE THE LOOP BEGINS --- 
    #? Wow 319 and not even at the loop :(
    while True:
        #Checks if this is the first itteration of the loop, if so then it will cause the game to reinitialize everything... More on that at the bottom.
        if isThisTheFirstItterationForASecondTimeBecauseIProgrammedThegetValFunctionForTheSliderClassPoorlySoINeedToRelyOnTwoVariablesToCountTheInitialItterationOfTheLoopBecauseIAmABadProgrammer == True:
            update = True
            isThisTheFirstItterationForASecondTimeBecauseIProgrammedThegetValFunctionForTheSliderClassPoorlySoINeedToRelyOnTwoVariablesToCountTheInitialItterationOfTheLoopBecauseIAmABadProgrammer = False
        
        #* Like I mentioned above this is to check to see if display mode and res are playing well togeather.
        if elements.getRes(resolution.getActive()) != res:
            res = elements.getRes(resolution.getActive())
            if res == hardwareDisp:
                displaymode.setActive('FULLSCREEN')
            else:
                displaymode.setActive('WINDOWED')
            surface = elements.set_screen(res,'Jumpr', elements.getMode(displaymode.getActive()))
            update = True
        
        #* Essencially the inverse of whats above, explained towards the top of the doc (roughly 171)
        if  elements.getMode(displaymode.getActive()) != mode:
            mode = elements.getMode(displaymode.getActive())
            if mode == FULLSCREEN:
                resolution.setActive(f'{hardwareDisp[0]} x {hardwareDisp[1]}')
            surface = elements.set_screen(res, 'Jumpr', elements.getMode(displaymode.getActive()))
            
        #* Sets background color (window color technically)
        surface.fill((121,128,241))
        #Paused
        #Checks to see if the user paused the game
        if gamePaused == True:
            #Changes the caption of the window, because why not?
            pygame.display.set_caption('Jumpr - Paused')
            #Checks to see where the user is (paused, options or exit)
            if menu == 'paused':
                #If they are on the paused screen it will default the options tab back to display so its the same every time it's opened
                setting = 'display'
                #Text header
                elements.draw_text('PAUSED', header, '#FFFFFF', surface, (elements.relative(400,150)),'center')
                #If you click the resume button the game resumes 
                #If you click the options button the game goes to the options menu
                #If you click the exit button it will take you to the exit menu
                if resume.checkClick(surface, True) == True:
                    gamePaused = False
                if options.checkClick(surface, True) == True:
                    menu = 'options'
                if exit.checkClick(surface, True) == True:
                    menu = 'exit'
                
            #This is the exit menu
            if menu == 'exit':
                #Draws header
                elements.draw_text('EXIT GAME ', header, '#FFFFFF', surface, (elements.relative(400,150)),'center')
                #If player presses mainmenu button, save and then go back to the main menu
                if exitMain.checkClick(surface, True) == True:
                    save = True
                    retrunMain = True
                #If the player presses exit to desktop then quit (will also save more on that later)
                if exitDesk.checkClick(surface, True) == True:
                    usrQuit = True
                #If they click retrun, set menu back to pause
                if exitCancel.checkClick(surface,True) == True:
                    menu = 'paused'
            #If the menu is set to options open options
            if menu == 'options':
                #Add text
                elements.draw_text('OPTIONS', header, '#FFFFFF', surface, (elements.relative(400,75)),'center')
                elements.draw_box(surface,(elements.relative(400,140)), (elements.relative(610,46)), '#6169f2', 10, 'center')
                #This sets up all of the settings navigation buttons.
                #For each if you click them it will toggle it's respective menu. The default menu (mentioned earlier) is display    
                if display.checkClick(surface, True) == True:
                    setting = 'display'
                if audio.checkClick(surface, True) == True:
                    setting = 'audio'
                if controls.checkClick(surface, True) == True:
                    setting = 'controls'
                if profile.checkClick(surface, True) == True:
                    setting = 'profile'
                
                if setting == 'display':
                    #This sets the display buttons color to the red ('#FF0000')
                    display.active('#FF0000')
                    #Display Menu
                    #This displays the dark rectangles in the background as well as the text on them
                    elements.draw_box(surface,(elements.relative(400,240)), (elements.relative(700,40)), '#6169f2', 2, 'center')
                    elements.draw_box(surface,(elements.relative(400,315)), (elements.relative(700,40)), '#6169f2', 2, 'center')
                    elements.draw_text('WINDOW MODE', sub, '#FFFFFF', surface, (elements.relative(60,240)),'midleft')
                    elements.draw_text('RESOLUTION', sub, '#FFFFFF', surface, (elements.relative(60,315)),'midleft')
                    
                    #This draws the sliders (surface, hover, hoverColor)
                    resolution.checkClick(surface,True)
                    displaymode.checkClick(surface,True)
                #If the selected item is fullscreen set the window to fullscreen and set the toggle var to true and update, if not the set temp var to false
                #This logic applies to the two other display modes
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
                    
                #Opens audio menu
                if setting == 'audio':
                    #Sets audio button to red
                    audio.active('#FF0000')
                    #Audio Menu
                    #Draws the background boxes and text
                    elements.draw_box(surface,(elements.relative(400,240)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('MASTER', sub, '#FFFFFF', surface, (elements.relative(60,240)),'midleft')
                    
                    elements.draw_box(surface,(elements.relative(400,290)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('MUSIC', sub, '#FFFFFF', surface, (elements.relative(60,290)),'midleft')
                    
                    elements.draw_box(surface,(elements.relative(400,340)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('SFX', sub, '#FFFFFF', surface, (elements.relative(60,340)),'midleft')
                    
                    #Adds sliders and a few more gems
                    #.addStroke([strokeSize,color],[strokeSize,color]) for the rail and slider respectivly
                    #.draw((railSize),(sliderSize(float for circle, Tuple for rect)),(railPosition),(railCornerRadius,sliderCornerRadius))
                    
                    #Txt Field
                    #.draw(surface, position, size, font, (font, anti-Aliasing(1 for true), cornerRadius)))
                    
                    #This section adds sliders and their respective textFields
                    master.addStroke([2,'#000000'],[0])
                    master.draw((elements.relative(200,12)),((elements.relativeNum(8))),(elements.relative(565,240)),((round(elements.relativeNum(5)),round(elements.relativeNum(5)))))
                    masterTxt.draw(surface,(elements.relative(715,240)),(elements.relative(60,30)),(regular,(round(elements.relativeNum(1))),(round(elements.relativeNum(2)))))
                         
                    sfx.addStroke([2,'#000000'],[0])
                    sfx.draw((elements.relative(200,12)),((elements.relativeNum(8))),(elements.relative(565,290)),((round(elements.relativeNum(5)),round(elements.relativeNum(5)))))
                    sfxTxt.draw(surface,(elements.relative(715,290)),(elements.relative(60,30)),(regular,(round(elements.relativeNum(1))),(round(elements.relativeNum(2)))))
                    
                    music.addStroke([2,'#000000'],[0])
                    music.draw((elements.relative(200,12)),((elements.relativeNum(8))),(elements.relative(565,340)),((round(elements.relativeNum(5)),round(elements.relativeNum(5)))))
                    musicTxt.draw(surface,(elements.relative(715,340)),(elements.relative(60,30)),(regular,(round(elements.relativeNum(1))),(round(elements.relativeNum(2)))))
                    #Adds more rects and texts
                    elements.draw_box(surface,(elements.relative(400,400)), (elements.relative(700,40)), '#6169f2', round(elements.relativeNum(2)), 'center')
                    elements.draw_text('AUDIO DEVICE', sub, '#FFFFFF', surface, (elements.relative(60,400)),'midleft')
                    #Dropdown menu for audio devices (does nothing functionally, same as all the other audio settings)
                    outDevice.checkClick(surface,True)
                    #Checks to see if this is the first itteration of the loop to avoid locking the slider values
                    #This loads the default (or user set) values from the settings flie (if one exists)
                    if firstItt == True:
                        master.setVal(loadMaster)
                        music.setVal(loadMusic)
                        sfx.setVal(loadSfx)
                        firstItt = False
                
                #Opens controls
                if setting == 'controls':
                    controls.active('#FF0000')
                    #Basically a 404 page
                    elements.draw_text('NOTHING TO SEE HERE.', sub, '#FFFFFF', surface, (elements.relative(400,300)),'center')
                    #Controls Menu
                #Opens profile
                if setting == 'profile':
                    profile.active('#FF0000')
                    #404 page.
                    elements.draw_text('NOTHING TO SEE HERE.', sub, '#FFFFFF', surface, (elements.relative(400,300)),'center')
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
            #   - Starts when the window changes states (event.type == pygame.VIDEORESIZE) or when the update var is triggered (update == True)
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
            #Welcome to the save function .json pt.2:
            #SAVE
            #   1. Tries to grab the user set values from settings
            #   2. If it suceeds it will move on
            #      2b. If it fails it will keep the settings the same.
            #   3. After that it opens the save file (with permission to write), if no file exists it will make one.
            #   4. With the file open it creates a dict of two dicts of settings (dictception) #? NOT "Dick - Ception"
            #   5. It then 'dumps' (saves) the info to the file, overwriting the initial info on it.
            #   6. Closes file and moves on like a boss
            def save():
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
            #Returns to main menu after saving
            if retrunMain == True:
                save()
                mainMenu()
                break
            #Saves the game
            if saveData == True:
                save()
                saveData = False
            #Quits the game
            if event.type == pygame.QUIT or usrQuit == True:
                save()
                pygame.quit()
                sys.exit

        #Believe it or not this updates the display...
        #* Refreshes everything thats supposed to be there.
            #* Without display just sits there black, hence the need for a literal game loop.
        pygame.display.update()
        #This ticks the clock.
        #* Ticks are the game speed, measured by tps, ever play Minecraft?
        clock.tick(60)