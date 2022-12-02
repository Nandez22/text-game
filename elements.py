import pygame, sys
from pygame.locals import *
#Im also quite mad that all of the comments I had written have been discarded and have to be re-written...
    #* Maybe they are on the github...
        #* nope.

#Elements is a place for premade functions like 'draw_text', just quality of life things...
    #* Scratch that, its a place for everything I need and don't want to make a new file for.
        #* I know thats a little unorganized but given that python can only import from parallel files my hands are kinda tied.
        
# *optional* values do not need to be enterd at the function call and will result in the default value specified by the function overload.

#Im making these two things (relPos / relSize) so that when the user resizes the window, stuff on screen actually adjusts.
    #They are pretty simple so I'm not gonna go too in depth but basically they just grab the current size of the window, divide that by 2 (width and height)
        # -- and then add the desired coords to that, so that everything is x, y distance from center (which is now effectivly 0,0)
        
    #* I am now realizing that relSize does relPos' job better than relPos so, oops?

#Here lies relPos ('You didn't do anything')

#Since I'm too tired to think of a better way to make relative size, I'm just going to make width and height a percentage of the widow size.
    #* Im trying to figure the best way to make it so that all things on screen maintain the same praportionality.
        #After saying that, I guess the best solution would be to make it so that one dimension (say width) is scaled according to the screen size and the width is just adjusted to a given ratio.
        #Im trying to make this in a way that can be implemented to what I currently have, I could make this so that it works in a vaccume or I could just make everything relative to my test window size and be done with it...
        #Im done with it...
def relative(width, height):
    surface = pygame.display.get_surface()
    dynW = surface.get_width()
    dynH = surface.get_height()

    ratio = (width / 800), (height / 600)
    dynSize = (ratio[0] * dynW), (ratio[1] * dynH)
    return dynSize


#This is for setting the screen dimensions, especially helpful when making new windos / menus
#Inputs as follows;
    # -1. Size of the window (set as (width,height))
    # -2. The 'name' of the window (set as "string") *optional* 
        #! If you do not set a window caption / name pygame will automatically set the name of the window to "Window"
    # -3. Set to true if you want the window resizable (input as True or False) *optional*
def set_screen(size, caption = False, resize = False):
    if caption != False:
        pygame.display.set_caption(caption)

    if resize == True:
        return pygame.display.set_mode(((size[0],size[1])), pygame.RESIZABLE)
    else:
        return pygame.display.set_mode(((size[0],size[1])))
#TODO make logic for display resizing to make vido menu functional
        
        

#This is for setting text on the screen
#If it wasnt obvious the inputs are as follows:
    # -1. Text to display
    # -2. Font (defined by font = pygame.font.SysFont("fontName", size))
    # -3. Color (can be any format but RGB must be a tuple and hex must be in quotes (IE; ((R, G, B)) or '#FFFFFF'))
    # -4. The screen surface (defined by set_screen (see above))
    # -5. Position (entered as (x,y))
def draw_text(text, font, color, surface, pos = (0,0), orientation = 'center'):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    
    if orientation == 'center':
        text_rect.center = (pos)
    if orientation == 'topleft':
        text_rect.topleft = (pos)
    if orientation == 'midleft':
        text_rect.midleft = (pos)
    surface.blit(text_obj, text_rect)

#This is the oh so amazing button I have been "raving" about. There is way too much code here so pardon me if I go a little fast or a little light on the descriptions.
class button():
    def __init__(self,content,pos,size,colors,radEl):
        
        #Basically this sets default variables and others to be used later.
        #Static variables are not mentet to be changed by the methods while dynamics are (with exceptions, not for any good reason, I'm just lazy.)
        
        
            #Static
        #Modifiers
        self.pressed = False
        self.pos = pos
        self.rad = radEl[0]
        self.elevation = radEl[1]
        
        #Colors
        self.primary = colors[0]
        self.secondary = colors[1]
        
            #Dynamic
        #Modifiers
        self.dyn_Elevation = radEl[1]
            #*Its been like two weeks so Im changing the naming convention (I despise underscores).
        self.dynScale = 1
        
        
        #Colors
        self.dyn_primary = colors[0]
        
        #Recovery Properties
        self.recovP = self.primary
        self.recovDP = self.dyn_primary
        
        #This checks to see if the init has been provided with text or an image to be used
        if type(content[0]) == str:
            #If its text it sets all of the attributes as follows.
            #Rect attributes
            self.size = size
            
            #Text attributes
            self.text = content[0]
            self.font_size = content[1]
            self.txt_color = content[2]
            self.font_name = content[3]
            self.anti_a = content[4]
            #This sets the text attributes so that pygame can understand them // basically loading them in
            self.format = pygame.font.SysFont((self.font_name),(self.font_size))
            #Rect Creation
            #This is where the surfaces of the button are designated.
            #Rects are rectangles and pygame is basically built around them, at this point they have been created but not drawn.
                # -- This means they exist, have a hitbox and be used by functions they just cant be seen. This is also what leads to problems cough* cough* dropdowns
            #Here we create two rectangles, one for the main surface of the button and one for the "chin", (3d looking part of the button)
            #The height difference of the two is determined by the 'elevation' attribute. (when discussing attributes I am just going use their name not "self.name", as I am done typing that fucking word.)
            self.top_rect = pygame.Rect(self.pos,((self.size[0] * self.dynScale),(self.size[1] * self.dynScale)))
            self.bottom_rect = pygame.Rect(self.pos,((self.size[0] * self.dynScale),(self.elevation * self.dynScale)))
            #This sets the center of the button to the provided position
            self.top_rect.center = (self.pos)
            
            #This is what creates (not draws) the text.
            #It also gets the rect from the text box #? Like I said rects are the bread and butter of pygame. (I think I used that expression somewhere in here before, so that may have sounded a little inconsistant with a pervious message)
            #This rect can then be used to do fun things with the text.
            #Text Creation
            self.content_surface = self.format.render(self.text,self.anti_a,self.txt_color)
            self.content_rect = self.content_surface.get_rect(center = self.top_rect.center)
            
        else:
            #If the content provided is an image, these attributes are set
            #Image Attributes
            image = content[0]
            
            #This sorts to see if the size provided is a Tuple (width, height) or a (scaleValue) -- Either an int or float
            if type(content[1]) == tuple:
                img_width = (content[1][0])
                img_height = (content[1][1])
                self.scale = 1
            else:
                self.scale = content[1]
                img_width = content[0].get_width()
                img_height = content[0].get_height()
            
            #This generates pygames version of the image to the size / scale provided
            self.content_surface = pygame.transform.scale(image, (int(img_width * self.scale), int(img_height * self.scale)))
            
            #Rect attributes
            self.size = size
            #This checks to see if the size provided is ('image','image'), if either of the dimensions are 'image' then the size of that dimension will be set to that of the image
            if self.size[0] == 'image':
                self.rect_width = ((img_width * self.scale) * self.dynScale)
            else:
                self.rect_width = (self.size[0] * self.dynScale)
                
            if self.size[1] == 'image':
                self.rect_height = ((img_height * self.scale) * self.dynScale)
            else:
                self.rect_height = (self.size[1] * self.dynScale)
            
            #Rect Creation
            #Same as before, creating rects for later
            self.top_rect = pygame.Rect(self.pos,((self.rect_width * self.dynScale),(self.rect_height * self.dynScale)))
            self.bottom_rect = pygame.Rect(self.pos,((self.rect_width * self.dynScale),(self.elevation * self.dynScale)))
            
            #Image Creation
            #Rects for later
            self.content_rect = (self.content_surface.get_rect())
            self.content_rect.center = (self.pos)
            
            #Centering
            self.top_rect.center = (self.pos)
            self.content_rect.center = self.top_rect.center
    #This method actually puts the button on screen. Initialized with a surface var (it need to know what window to draw on)
    def draw(self,surface):
        #This aligns the rects so that the top rect is centered at the coords provided and that the chin is hanging according to the specified dimentsions
        #Not only that, but making sure that the text or image is properly centered on the top rect
        self.top_rect.y = self.pos[1] - self.dyn_Elevation
        self.top_rect.center = self.pos
        self.content_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyn_Elevation
        
        #These are the functions that actually draw the button on screen. .draw is used for rects and .blit is used for things like text and images.
        pygame.draw.rect(surface, self.secondary, self.bottom_rect, border_radius = self.rad)
        pygame.draw.rect(surface, self.dyn_primary, self.top_rect, border_radius = self.rad)
        surface.blit(self.content_surface, self.content_rect)
        
    #This not only calls the draw method but also give the button its function
    def checkClick(self,surface, hover = False, color = '#FF0000'):
        #calling the .draw method
        self.draw(surface)
        #Getting the position of the mouse to check for collisions
        mouse_pos = pygame.mouse.get_pos()
        #Checking for collisions
        #This basically works as follows
        #   If the mouse is touching any part of the button:
        #       (if hover is set to true), set the color to the designated color
        #       if the mouse is clicked while it is touching the button then set the pressed var to true and "get rid" of the "chin" #* (and return True)
        #   If the mouse isn't hovering over the button, change the color back to default as well as the "chin"
        if self.top_rect.collidepoint(mouse_pos):
            if hover == True:
                self.dyn_primary = color
            if pygame.mouse.get_pressed()[0] == 1:
                self.pressed = True
                self.dyn_Elevation = 0
                
            else:
                self.dyn_Elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    return True
        else:
            self.dyn_primary = self.primary
            self.dyn_Elevation = self.elevation
        
    #Grabs the size of the button and returns it
    def getDimensions(self):
        return self.rect_width, self.rect_height
    
    #Sets the designated button to a certain color and "depress" it. (good to make it look like a button is toggled on)
    def active(self,color):
        self.dyn_primary = color
        self.dyn_Elevation = 0
    
    #Sets the position of the button, named this because there was another method or two somewhere with re-something and I thought it would be fun to keep that going. #? It wasnt fun or funny.
    def rePos(self, pos):
        self.pos = pos
    
    #Some of this is just diagnostic and I'd rather spend more effort declaring that then removing said 'things'
    def getSize(self):
        print(f'Scale: {self.dynScale}')
        print(f'Width: {self.size[0]}')
        print(f'Height: {self.size[1]}')    
    
    #Heres the other re-something! #? This one actully sounds funish.
    #Sets the font size
    def reFont(self,size):
        self.font_size = size
       
       #Heres the damn dropdown
       #? I have a love hate relationship with the dropdown, on one hand there was no tutorial for it and I almost came up with all of it by myself, but on the other hand It's pretty messy and has some "unintended features". 
class dropdown:
    def __init__(self, options, size, pos, active):
        #Just setting basic attributes
        self.options = options
        self.size = size
        self.pos = pos
        self.rad = 0
        
        self.dropped = False
        self.pressed = False
        self.active_rect = active
        
        self.txt_selected = '#FFFFFF'
        self.txt_unselected = '#e0e0e0'
        self.format = pygame.font.SysFont('None',17)
        
        self.rect_selected = '#222222'
        self.rect_unselected = '#333333'
        self.dyn_unselected = '#333333'
        
        self.rects = {}
        self.txt_surfaces = {}
        self.txt_rects = {}
        
        #This is where the fun begins...
        #This takes the list of options and adds them to a dictionary assigned a rect as their values
        for option in self.options:
            self.rects[option] = pygame.Rect(pos,size)
 
        #* I guess this is a good place to explain what is going on here, this might get a little long winded so I apologies.
        #* Basically I wanted a dropdown menu that you could add a theoretically infinite ammount of options (ignoring the limits of the compiler, python and computers.)
        #* In python if you want to "generate" something that isn't user defined you typically need to append to a list in a loop.
        #* That's good in all, but even then how do you remember what rect is assigned to what text, etc., etc.; Thats where dictionaries come in.
        
        #* The init() takes a list of options in str form. It cycles through that list and creates a rect for each option (at the pos and size designated).
        #* Now the program knows what rects are assigned to what options (this works because while rects arent something you would typically put in a dictionary, they are objects and have a memory address meaning they can be used in bool expressions)
        
        #* After this we move out of the init() but I want to keep the explination here so I'm sorry if you were trying to follow the code along.
        
        #* Once this first dict is created the next step is to draw them, but when the menu is collapsed we want to only see the active option (this is why an 'activeRect' is a required designation)
        #* This is also where we see the creation of the next two dictionaries. Remember with the button we needed three things, the button surface, the text and text rect.
        #* Just as before the program needs to remember what text and text rect are assigned to what option or nothing will make sense, hence dictionaries.
        #* While it loops through the options to draw the surface rects, it also takes the text from [options] and renders it (render, not blit, it will not show up on screen) afterwards assigns that to a dictionary called txt_surfaces
        #* It also grabs the rect of the text from the above step and adds that (with the option name) to a third dictionary called txt_rects
        #? I hate myself for using underscores here
        #* Draw will only draw the active rect and the text associated with it. (also centers it on the position provided)
        
        #* Now we move onto the .drop() method...
        
        #* This is where I say I lied...
        #* I said that the draw method added all of the text and text rects to the dictionaries, but It only adds the currently active one.
        #* In .drop() that changes.
        #* Besides adding the hover function which I'll explain further down, it designates the order list
        #* When you use a dropdown, you want it to display the active option and the top and the other options below, and hopefully in order.
        #* To do this, the game starts adding the options to the order, when it gets to the currently active option it skips it.
        #* The method then checks to see if the user has clicked the menu yet. If so then it will toggle 'dropped'
        #* When 'dropped' is toggled to true, for all options except the active on it creates their rects, and adds them to the order (again I lied, that happens here not earlier like I had said).
        #* Once the order has been made, the method resets the lstPos var to 0 (think of this as the thing that goes down the order picking out each option)
        #* It then looks through all of the options again, if an option is the 0th item in the order it is drawn with its topMiddle point equal to the bottomMiddle point of the active option
        #* From here it goes down the order drawing each option directly below the option before it.
        #* And yeah, that's the general gist of how I got the dropdown menu to work... There is still some smaller things that need explaining but the comments will be light from here until the next major class
                    
    def draw(self, surface):
        self.surface = surface
        self.mouse_pos = pygame.mouse.get_pos()
        
        #Looks through all options assigns each a rect and adds to a dictionary
        for option in self.options:
            if self.active_rect == option:
                self.rects[option].center = self.pos
                
                self.txt_surfaces[option] = self.format.render(option, True, self.txt_selected)
                self.txt_rects[option] = self.txt_surfaces[option].get_rect(center = self.rects[option].center)
                
                pygame.draw.rect(self.surface, self.rect_selected, self.rects[option], border_radius = self.rad)
                self.surface.blit(self.txt_surfaces[option], self.txt_rects[option])

    def drop(self,Hover = False, color = '#FF0000'):
        
        self.hover = Hover
        self.hover_color = color

        order = []
        #Checks to see if user has clicked on dropdown menu
        if self.rects[self.active_rect].collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.dropped = True
        elif not self.rects[self.active_rect].collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.dropped = False
            
        #This is what happens if the user clicks the dropdown menu
        if self.dropped == True:
            #Looks through the options, if the option is not the active option it will be given text and a text rect, which will be added to their respective dictionaries
            for option in self.options:
                if option != self.active_rect:
                    self.txt_surfaces[option] = self.format.render(option, True, self.txt_unselected)
                    self.txt_rects[option] = self.txt_surfaces[option].get_rect(center = self.rects[option].center)
                    #Adds them to the order
                    order.append(option)
                    lstPos = 0
                    #Looks for the first item in the order, for that item it will position it directly under the active option, its top touching the others bottom
                    #For all others, they are positioned directly under the option in the order before themselfs
                    for option in order:
                        if option == order[0]:
                            self.rects[option].midtop = self.rects[self.active_rect].midbottom
                        else:
                            self.rects[option].midtop = self.rects[order[(lstPos - 1)]].midbottom
                        lstPos += 1
                    
                    #This looks to see if the mouse is hovering over any of the options, if so set them to the designated color, #? except borderless for some reason...
                    #? Thats halarious, I had no clue that was there and I don't beleive it serves any purpose except to fuck over borderless, which would explain why it hates me.
                    #--HOVER / Click DETECTION-------------------------
                    if self.rects[option].collidepoint(self.mouse_pos):
                        if self.hover == True:
                            self.dyn_unselected = self.hover_color
                            if self.rects[option] == 'BORDERLESS':
                                pass
                    else:
                        self.dyn_unselected = self.rect_unselected
                    #--------------------------------------------------
                    #Draws rects
                    pygame.draw.rect(self.surface, self.dyn_unselected, self.rects[option])
                    self.surface.blit(self.txt_surfaces[option], self.txt_rects[option])   
    
    #This method checks to see if the user clicks the menu
    def checkClick(self, surface, Hover = False, color = '#FF0000'):
        
        self.draw(surface)
        self.drop(Hover, color)
        
        #If the users mouse is hovering over an option and they click it, that option becomes the active option
        for option in self.options:
            if self.rects[option].collidepoint(self.mouse_pos) and self.rects[option] != self.active_rect:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.active_rect = option
                    self.pressed = True
                else:
                    if self.pressed == True:
                        self.pressed = False
    #returns the active option      
    def getActive(self):
        return self.active_rect
    #Sets the active option
    def setActive(self,active):
        self.active_rect = active
    #Allows for the changing of different colors and whatnot, much cleaner than doing it all in the init (which has its own problems)
    def style(self, colors = ('#222222','#333333'), txt_colors = ('#FFFFFF','#e0e0e0'), font = 'none', size = 12, rad = 0):
        self.rect_selected = colors[0]
        self.rect_unselected = colors[1]
        self.dyn_unselected = colors[1]
        
        self.txt_selected = txt_colors[0]
        self.txt_unselected = txt_colors[1]
        
        self.format = pygame.font.SysFont(font,size)
        self.rad = rad
        #! RAD not recommended -- Looks like dookie

#One of my wonderful quality of life functions, all it really does is draw a rect on screen with the given paramaters
#Unfortunatley it can't be used to do much else, since you cant recover any rect data from this, making it useless for anything logic based.
def draw_box(surface, pos, size, color, rad, alignment = 'topleft'):

    box = pygame.Rect(pos,size)

    if alignment == 'topleft':
        box.topleft = (pos)
    if alignment == 'center':
        box.center = (pos)
    if alignment == 'midtop':
        box.midtop = (pos)
    if alignment == 'midbottom':
        box.midbottom = (pos)
        
    pygame.draw.rect(surface, color, box, border_radius = rad)

#Another wonderful one (kind of redundent if I wasn't lazy)
#Takes a number and gets the ratio of that number to 800 (the default screen width) -- num:800 
    #* This works because I designed everything in a 800 x 600 window, meaning that instead of providing (windowSize/num) as dimensions, I just scale everything according to that 800 x 600 window.
def relativeNum(num, max = False):
    surface = pygame.display.get_surface()
    width = surface.get_width()

    ratio = (num / 800)
    
    if max == False:
        return (ratio * width)
    if ratio >= max:
        return max * num
       
#Here's another big fucker, not the biggest fucker but a big one indeed.
#Range sliders were another thing that lacked much for tutorials online, while there was a tiny bit of info I basically just went into a new file and went from scratch.
class slider:
    def __init__(self,surface, colors, startPos):
        #Setting default / necessary values
        self.surface = surface
        self.sPos = []
        
        for coord in startPos:
            self.sPos.append(coord)
            
        self.rWidth = 0
        self.sWidth = 0
        
        self.rPrimary = colors[0]
        self.sPrimary = colors[1]
        self.dynPrimary = colors[1]
        
        self.stick = False

    #Like the dropdown I'll just explain how it works here...
    #   For a slider you need two things.
    #       1. A 'rail' (as I call it), basically the range that the slider slides along (the constraints)
    #       2. The 'slider' the dot (or rectangle) that the user drags along the 'rail' #? Yes I'm aware I'm flying close to the sun with that. (The sun being circular definitions)
    #   Compared to a lot of things here, thats an easy start.
    #   First we draw out the rail then the slider on top of it
    #   We also need to constrain the slider's y position to the x position of the rail.
    #   We can then tell it to look for a mouse hover and click and hold.
    #   When that happens set the x position of the slider to the x position of the mouse
    #       But we can only allow that to happen withing the range of the rail.
    #       This is where it grabs the coords of the rail's end points, if at any point it passes one of the end points the x position of the slider gets set to that endpoint
    
    #Theres a little more to it than that, but thats the general / basic idea.

    def draw(self, rail, slider, pos, mod = (0,0)):
        
        self.pos = pos
        
        self.rSize = rail
        self.rRad = mod[0]
        
        self.rail = pygame.rect.Rect(pos, self.rSize)
        self.rail.center = self.pos
        
        self.sRad = mod[1]
        
        #This disserns weather the "programmer" is trying to designate the radius or (width,height) of the slider, it then assigns the slider as a circle or rect respectivly.
        if type(slider) == float:
            self.rad = slider
            self.shape = 'circle'
        else:
            self.sSize = slider
        #Makin dat rect.
        #If a stroke is added using a later method, then this draws the rect.
        #Keep in mind that the order that the rects are drawn matters, so a stroke has to be drawn first.
            #* Reminds me that I forgot to explain stroke...
                #* In pygame, rects have no stroke attribute, meaning you have to draw a rect behind it that is slightly bigger to get the look of a stroke.
                #* The order is important because the stroke has to be drawn before the main rect to appear behind it. (Think of it as being drawn over)
        if self.rWidth > 0:
            self.rStroke = pygame.rect.Rect(self.pos,(self.rSize[0] + self.rWidth, self.rSize[1] + self.rWidth))
            self.rStroke.center = self.rail.center
            pygame.draw.rect(self.surface, self.rSecondary, self.rStroke, border_radius = self.rRad)
        #Puts the rain on screen
        pygame.draw.rect(self.surface, self.rPrimary, self.rail, border_radius = self.rRad)    
        #Stroke but in circle form
        #This is also a great time to mention how much much I hate pygame circles (I say that like I have expirence with any other type of circle or programming at that.)
            #Like mentioned before in pygame when you define a rect it doesn't appear on screen, meaning you can use it in your logic without it appearing when you don't want. (whilst avoiding errors)
            #Unkile rects, circles can not be defined, they can only be drawn (Technically they are defined and drawn at the same time) Meaning you can't use them in logic until they appear on screen.
            #This can be woked around, like making a rect for the circle that is the same size, that stays invisible and drawing the circle on the coords of that rect, but still way more annoying than just being able to define a circle seperatly.
            #Im explaining this because the code here is in a super wierd and disorganized order, but that is to work around drawing things in the proper order and circles being circles
        if self.sWidth > 0:
            if self.shape == 'circle':
                self.sStroke = pygame.draw.circle(self.surface, self.sSecondary, self.sPos, (self.rad + self.sWidth))
            else:
                self.sStroke = pygame.rect.Rect(self.sPos, (self.sSize + self.sWidth))
                self.sStroke.center = self.sPos
                pygame.draw.rect(self.surface, self.sSecondary, self.sStroke, border_radius = self.sRad)
        
        if type(slider) == float:
            self.slider = pygame.draw.circle(self.surface, self.dynPrimary, (self.sPos[0], self.pos[1]), self.rad)
        else:
            self.slider = pygame.rect.Rect(self.sPos, self.sSize)
            self.slider.center = self.sPos
            pygame.draw.rect(self.surface, self.dynPrimary, self.slider, border_radius = self.sRad)
    #Adds a stroke, well tells .draw() to add one
    def addStroke(self, rail, slider):
         
        self.rWidth = rail[0]
        self.rSecondary = rail[1]
        
        self.sWidth = slider[0]
        self.sSecondary = rail[1]
    #This makes the slider actually, well you know "slide"
    def drag(self, hover, color = '#FF0000'):
    
    #HOVER LOGIC // DRAG LOGIC
        #gets mouse position
        mousePos = pygame.mouse.get_pos()
        #Checks to see if the mouse is hovering over the slider and or rail
        if self.slider.collidepoint(mousePos) or self.rail.collidepoint(mousePos):
            #If so and hover is set to true, set the color of the slider to designated color
            if hover == True:
                self.dynPrimary = color
                #If the user clicks on either, set stick to true (var that tells how to position slider)
                if pygame.mouse.get_pressed()[0] == 1:
                    self.stick = True
        else:
            self.dynPrimary = self.sPrimary
            #If not change stuff back to normal (color)
        
        #If the left mouse button is lifted back up, turn off stick
        #* This is done so that the user doesn't have to constantly keep the mouse over the rail while trying to drag the slider, as long as the left key is depressed the slider will follow the mouse (within its given constraints)
        if pygame.mouse.get_pressed()[0] == 0:
            self.stick = False 
        #This also keeps the hovor color turned on even if the mouse is not over the rail (so long as left click is held down)
        if self.stick == True:
            if hover == True:
                self.dynPrimary = color
                
            #This keeps the slider on the rail, it looks to see if the slider breaks either the left or right plane of the slider
            #If that happens it will set the mouse x to the x of plane broken
            if self.sPos[0] >= self.rail.midleft[0] and self.sPos[0] <= self.rail.midright[0]:
                self.sPos[0] = mousePos[0]
        if self.sPos[0] < self.rail.midleft[0]:
            self.sPos[0] = self.rail.midleft[0]
        if self.sPos[0] > self.rail.midright[0]:
            self.sPos[0] = self.rail.midright[0]
        #This turns the position of the slider into a usable numberical value and returns it
        self.val = round(((self.sPos[0] - self.rail.midleft[0]) / self.rSize[0]),2)
        return self.val
    
    def setVal(self, num):
        #Takes a percentage input IE 90% - the % sign and converts back to coords to set the slider pos.
        val = num / 100
        newVal =((val * self.rSize[0]) + self.rail.midleft[0])
        self.sPos[0] = newVal
    
    #Gets the current percentage of the slider
    def getVal(self):
        return (self.val * 100)
    #Gets the current x value of the slider
    def getX(self):
        return self.sPos[0]
    #Sets the current x value of the slider
    def setX(self, x):
        self.sPos[0] = x
    
#Finally the home streatch!
#? I am so tired, my eyes hurt and I have put in at leat 20 - 25+ house of coding this week easily. (Wake up code nonstop (unless class), gym (if not coding), eat, code, sleep)

#Ok, text fields...
#While there was stuff out on the world wide web about these, I still gave it my own apporach, the only thing I had to look up was the code for getting the keystroke input from the user.
    #I knew how to get single key inputs, but not everything (done with event.unicode as an fyi)
#Shoot I broke my patter, see you in the init()
class txtField:
    def __init__(self, colors, default):
        #setting default and necessary values
        self.val = f'{default}%'
        self.typing = False
        
        self.primary = colors[0]
        self.dynPrimary = colors[0]
        self.textColor = colors[1]
        
        self.stroke = False
        self.input = ''
        
        #Ok, text fields again...
        #   First off is the easy part, get a rectangle and throw some text on it
        #   Easy enough, create a rect object, text object and draw them
        #   Now we need to see if the user clicks on it, simple enough, just get the mouse pos and check for collide and left click.
        
        #   Now for the logic piece.
        #   We know when the user clicks on the box, and can toggle an edit mode, but what do we do then.
        #   First off we need to look at events, which is done with 'for event in pygame.events.get()', which is gret and all but that can't go in the method
        #   That loop runs well when itterated once throughout the main game loop, but when it's ran many times it tends to slow things way down, so we need to make a method to go in that loop in the game loop (loopception)
        #   We then check for a key press with, 'if event.type() == KEYDOWN:', now we know when the user hits a key
        #   We then need to get the users keyboard input, which can be done with 'event.unicode' (which is great but we still need to know if the user presses backspace or enter)
        #   Those are checked with 'event.key == K_BACKSPACE' and 'event.key == K_RETURN' respectivly.

        #To set the text to something, it needs new text, so a string is created.
        #To start the string is blank, but as the user types, the unicode from each event is added to the string.
        #In this lies a problem, since we only want number, but text can be added to the string. This is fine until it tries to convert the string to a float in order to set the slider to the correct value.
        #This is where try: comes in. Try will attempt to convert the event unicode into a float, which will only work the unicode is a number. If it fails, instead of giving a type error, it will just pass using except:
        #Using that the program can construct a string of all number that can be converted to a float and provide to a slider error free.
        
        #Now back to the other keys, backspace and return...
        #When back space is pressed we want it to delete the most recent character in the string, so string[:-1] is triggered, deleting the last item.
        #When return is hit, it sets the value of the slider to the number entered and exits the edit mode (clicking outside of the box also exits edit mode.)
        
        #And thats basically it for text fields...
        
    def draw(self, surface, pos, size, style):
        #Setting attributes
        self.surface = surface
        self.pos = pos
        self.size = size
        self.rad = style[2]
        
        self.font = style[0]
        self.antiAlias = style[1]
        #Defining rects
        self.fieldRect = pygame.Rect(self.pos, self.size)
        self.fieldRect.center = self.pos
        #Checks to see if the user is typing, if so then the box color is set to the hover color (if one exisits)
        if self.typing == True:
            self.dynPrimary = self.hPrimary
            #If there is a stroke declared, the stroke color will change to the color provided.
            if self.stroke == True:
                self.sRect = pygame.Rect(self.fieldRect.center,(self.size[0] + self.sRad, self.size[1] + self.sRad))
                self.sRect.center = self.fieldRect.center
                pygame.draw.rect(self.surface, self.secondary, self.sRect, border_radius = self.rad)
        #This draws the main surface rect
        pygame.draw.rect(self.surface, self.dynPrimary, self.fieldRect, border_radius = self.rad)
        #This defines the text and draws it on screen #* (blit not draw)
        self.txtObj = self.font.render(self.val ,self.antiAlias, self.textColor)
        self.txtRect = self.txtObj.get_rect()
        self.txtRect.center = self.fieldRect.center
        self.surface.blit(self.txtObj, self.txtRect)
    
    #Where the "magic" happends
    def edit(self,event, rail, hover = (False,'#FF0000'), stroke = (0,'#000000')):
        #Defining attributes
        self.slid = round(100 * (rail.drag(True)))
        
        self.hover = hover[0]
        self.hPrimary = hover[1]
        self.sRad = stroke[0]
        self.secondary = stroke[1]
        
        self.val = f'{self.slid}%'
        #Sets stroke if necessary
        if stroke[0] > 0:
            self.stroke = True
        else:
            self.stroke = False
        #Gets mouse position
        mousePos = pygame.mouse.get_pos()
        #Checks if mouse is hovering over the box
        if self.fieldRect.collidepoint(mousePos):
            #Sets hover color if applicable
            self.dynPrimary = self.hPrimary
            #Checks for a left click
            if pygame.mouse.get_pressed()[0] == 1:
                #Clears the text box
                self.input = ''
                #Enables "edit mode"
                self.typing = True
        else:
            #if not, reset colors
            self.dynPrimary = self.primary
            #When the user lets go of left click, let of of "edit mode"
            if pygame.mouse.get_pressed()[0] == 1:
                self.typing = False
        #Checks for a key depression
        if event.type == KEYDOWN:
            #If a key has been depressed and "edit mode" is enabled
            if self.typing == True:
                #If the key is return, set the slider to the current value displayed, if its empty the value will revert to what it was before the edit #* and stops editing
                if event.key == K_RETURN:
                    try:
                        rail.setVal(float(self.input))
                    except:
                        pass
                    self.typing = False
                #If the key is backspace, delete the most recent character in the string, if no character exist, set the value to zero
                elif event.key == K_BACKSPACE:
                    self.input = self.input[:-1]
                    if not len(self.input) == 0:
                        rail.setVal(float(self.input))
                    else:
                        rail.setVal(0)
                else:
                    #The program tries to convert the keypress (if not return or backspace) to a number, if that fails it will pass over it.
                    #If it converts, then the str version will be added to the string
                    #It will then set the slider to the value of the string, so it updates as the user types.
                    #This all happens only if the value is less than 100%, if not, then the value will stick at 100 until a character is deleted.
                    try:
                        if self.slid <= 100:
                            if type(float(event.unicode)) == float:
                                self.input += event.unicode
                                rail.setVal(float(self.input))
                    except:
                        pass
#This takes the str resolution value set as ('xRes x yRes') and converts it to a Tuple
#Takes the characters, adds all number to a list, and seperates them at the x buy converting it to a comma.
#Then it turns that into a Tuple and returns it
def getRes(resolution):
    res = ''
    for char in  resolution:
        try:
            int(char)
            res += char
        except:
            if char == 'x':
                res += ','
            pass
    res = res.split(',')
    res = int(res[0]),int(res[1])
    return res

#This gets the pygame.locals value of the str display mode.
#A little less cool than the getRes() function, but works none the less.
def getMode(input):
    if input == 'FULLSCREEN':
        mode = FULLSCREEN
    if input == 'BORDERLESS':
        mode = NOFRAME
    if input == 'WINDOWED':
        mode = RESIZABLE
    return mode

#? I AM DONE THANK THE LORD, and thank you Matt Priem <3