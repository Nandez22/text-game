import pygame, sys, pygame.locals
#Elements is a place for premade functions like 'draw_text', just quality of life things...
# *optional* values do not need to be enterd at the function call and will result in the default value specified by the function overload.


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
        text_rect.center = pos
    if orientation == 'topleft':
        text_rect.topleft = (pos)
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
            self.top_rect = pygame.Rect(pos,(size[0],size[1]))
            self.bottom_rect = pygame.Rect(pos,(size[0],self.elevation))
            
            self.top_rect.center = (pos)
            
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
            
            if size[0] == 'image':
                self.rect_width = (img_width * self.scale)
            else:
                self.rect_width = size[0]
                
            if size[1] == 'image':
                self.rect_height = (img_height * self.scale)
            else:
                self.rect_height = size[1]
            
            #Rect Creation
            self.top_rect = pygame.Rect(pos,(self.rect_width,self.rect_height))
            self.bottom_rect = pygame.Rect(pos,(self.rect_width,self.elevation))
            
            #Image Creation
            self.content_rect = (self.content_surface.get_rect())
            self.content_rect.center = (pos)
            
            #Centering
            self.top_rect.center = (pos)
            self.content_rect.center = self.top_rect.center

    def draw(self,surface):
        self.top_rect.y = self.pos[1] - self.dyn_Elevation
        self.content_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyn_Elevation
        
        
        pygame.draw.rect(surface, self.secondary, self.bottom_rect, border_radius = self.rad)
        pygame.draw.rect(surface, self.dyn_primary, self.top_rect, border_radius = self.rad)
        surface.blit(self.content_surface, self.content_rect)
        
    def checkClick(self, hover = False, color = '#FF0000'):
        
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
                    else:
                        self.dyn_unselected = self.rect_unselected
                    #--------------------------------------------------
                    
                    
                    
                    pygame.draw.rect(self.surface, self.dyn_unselected, self.rects[option])
                    self.surface.blit(self.txt_surfaces[option], self.txt_rects[option])   
                      
    def checkClick(self):
        
        for option in self.options:
            if self.rects[option].collidepoint(self.mouse_pos) and self.rects[option] != self.active_rect:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.active_rect = option
                    self.pressed = True
                else:
                    if self.pressed == True:
                        self.pressed = False
    
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
    
