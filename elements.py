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


class button():
    def __init__(self,content,pos,size,colors,radEl):
        
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
        
        if type(content[0]) == str:

            #Rect attributes
            self.size = size
            
            #Text attributes
            self.text = content[0]
            self.font_size = content[1]
            self.txt_color = content[2]
            self.font_name = content[3]
            self.anti_a = content[4]
            
            self.format = pygame.font.SysFont((self.font_name),(self.font_size))
            #Rect Creation
            self.top_rect = pygame.Rect(self.pos,((self.size[0] * self.dynScale),(self.size[1] * self.dynScale)))
            self.bottom_rect = pygame.Rect(self.pos,((self.size[0] * self.dynScale),(self.elevation * self.dynScale)))
            
            self.top_rect.center = (self.pos)
            
            #Text Creation
            self.content_surface = self.format.render(self.text,self.anti_a,self.txt_color)
            self.content_rect = self.content_surface.get_rect(center = self.top_rect.center)
            
        else:
            
            #Image Attributes
            image = content[0]
            
            
            if type(content[1]) == tuple:
                img_width = (content[1][0])
                img_height = (content[1][1])
                self.scale = 1
            else:
                self.scale = content[1]
                img_width = content[0].get_width()
                img_height = content[0].get_height()
            
            
            self.content_surface = pygame.transform.scale(image, (int(img_width * self.scale), int(img_height * self.scale)))
            
            #Rect attributes
            self.size = size
            
            if self.size[0] == 'image':
                self.rect_width = ((img_width * self.scale) * self.dynScale)
            else:
                self.rect_width = (self.size[0] * self.dynScale)
                
            if self.size[1] == 'image':
                self.rect_height = ((img_height * self.scale) * self.dynScale)
            else:
                self.rect_height = (self.size[1] * self.dynScale)
            
            #Rect Creation
            self.top_rect = pygame.Rect(self.pos,((self.rect_width * self.dynScale),(self.rect_height * self.dynScale)))
            self.bottom_rect = pygame.Rect(self.pos,((self.rect_width * self.dynScale),(self.elevation * self.dynScale)))
            
            #Image Creation
            self.content_rect = (self.content_surface.get_rect())
            self.content_rect.center = (self.pos)
            
            #Centering
            self.top_rect.center = (self.pos)
            self.content_rect.center = self.top_rect.center

    def draw(self,surface):
        
        self.top_rect.y = self.pos[1] - self.dyn_Elevation
        self.top_rect.center = self.pos
        self.content_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyn_Elevation
        
        
        pygame.draw.rect(surface, self.secondary, self.bottom_rect, border_radius = self.rad)
        pygame.draw.rect(surface, self.dyn_primary, self.top_rect, border_radius = self.rad)
        surface.blit(self.content_surface, self.content_rect)
        
    def checkClick(self,surface, hover = False, color = '#FF0000'):
        
        self.draw(surface)
        
        mouse_pos = pygame.mouse.get_pos()
        
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
            
    def getDimensions(self):
        return self.rect_width, self.rect_height
    
    def active(self,color):
        self.dyn_primary = color
        self.dyn_Elevation = 0

    def rePos(self, pos):
        self.pos = pos
    
    #Some of this is just diagnostic and I'd rather spend more effort declaring that then removing said 'things'
    def getSize(self):
        print(f'Scale: {self.dynScale}')
        print(f'Width: {self.size[0]}')
        print(f'Height: {self.size[1]}')    
    
    def reFont(self,size):
        self.font_size = size
        
class dropdown:
    def __init__(self, options, size, pos, active):
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
        
        
        for option in self.options:
            self.rects[option] = pygame.Rect(pos,size)
            
    def draw(self, surface):
        self.surface = surface
        self.mouse_pos = pygame.mouse.get_pos()
        
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
        if self.rects[self.active_rect].collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.dropped = True
        elif not self.rects[self.active_rect].collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.dropped = False
                
        if self.dropped == True:
            for option in self.options:
                if option != self.active_rect:
                    self.txt_surfaces[option] = self.format.render(option, True, self.txt_unselected)
                    self.txt_rects[option] = self.txt_surfaces[option].get_rect(center = self.rects[option].center)
                    
                    order.append(option)
                    lstPos = 0
                    for option in order:
                        if option == order[0]:
                            self.rects[option].midtop = self.rects[self.active_rect].midbottom
                        else:
                            self.rects[option].midtop = self.rects[order[(lstPos - 1)]].midbottom
                        lstPos += 1
                    
                    #--HOVER / Click DETECTION-------------------------
                    if self.rects[option].collidepoint(self.mouse_pos):
                        if self.hover == True:
                            self.dyn_unselected = self.hover_color
                            if self.rects[option] == 'BORDERLESS':
                                print('Borderless')
                    else:
                        self.dyn_unselected = self.rect_unselected
                    #--------------------------------------------------
                    
                    
                    
                    pygame.draw.rect(self.surface, self.dyn_unselected, self.rects[option])
                    self.surface.blit(self.txt_surfaces[option], self.txt_rects[option])   
                      
    def checkClick(self, surface, Hover = False, color = '#FF0000'):
        
        self.draw(surface)
        self.drop(Hover, color)
        
        for option in self.options:
            if self.rects[option].collidepoint(self.mouse_pos) and self.rects[option] != self.active_rect:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.active_rect = option
                    self.pressed = True
                else:
                    if self.pressed == True:
                        self.pressed = False
                        
    def getActive(self):
        return self.active_rect
    
    def style(self, colors = ('#222222','#333333'), txt_colors = ('#FFFFFF','#e0e0e0'), font = 'none', size = 12, rad = 0):
        self.rect_selected = colors[0]
        self.rect_unselected = colors[1]
        self.dyn_unselected = colors[1]
        
        self.txt_selected = txt_colors[0]
        self.txt_unselected = txt_colors[1]
        
        self.format = pygame.font.SysFont(font,size)
        self.rad = rad
        #! RAD not recommended -- Looks like dookie

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
    
def relativeNum(num, max = False):
    surface = pygame.display.get_surface()
    width = surface.get_width()

    ratio = (num / 800)
    
    
    if max == False:
        return (ratio * width)
    if ratio >= max:
        return max * num