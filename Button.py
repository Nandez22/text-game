import pygame

class txtButton:
    def __init__(self, text = 'button', size = (0,0), pos = (0,0), modifiers = (0,0), colors('#000000','#FFFFFF')):

        #Setting basic attributes --
        #Dynamic Atributes
        self.pressed = False
        self.cElevation = elevation
        self.primary = primary
        
        #Static Atributes
        self.hPrimary = primary
        self.secondary = colors[1]
        self.elevation = elevation
        self.staticY = pos[1]
        self.size = size
        self.rad = rad
        self.format = pygame.font.Font(None,30)
        
        #Primary button surface
        self.top_rect = pygame.Rect(pos,(size{0},size{1}))     
        #Secondary button surface
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = secondary
        
        #Text
        #-- gui_font.render(what,anti-aliased?,color(hex))
        self.text_plane = self.format.render(text,True,'#FFFFFF')
        #Pos of text relative to the outer rect
        self.text_rect = self.text_plane.get_rect(center = self.top_rect.center)
        
    def draw(self,surface):
        if self.elevation > 0:
            self.top_rect.y = self.staticY - self.cElevation
            self.text_rect.center = self.top_rect.center

            self.bottom_rect.midtop = self.top_rect.midtop
            self.bottom_rect.height = self.top_rect.height + self.cElevation
        #Draw is for shapes, and things that can be "drawn"
        pygame.draw.rect(surface, self.bottom_color, self.bottom_rect, border_radius = self.rad)
        pygame.draw.rect(surface, self.primary, self.top_rect, border_radius = self.rad)

        #Blit is for not drawn things IE; text and other 'objects'
        surface.blit(self.text_plane,self.text_rect)
            
            
    def checkPress(self,hover = False, color = '#333333'):
        #Finds mouse position
        mouse_pos = pygame.mouse.get_pos()     
        #Checks to see if the mouse is overlapping / 'colliding' with the button
        if self.top_rect.collidepoint(mouse_pos):
            if hover == True:
                self.primary = color
            if pygame.mouse.get_pressed()[0] == 1:
                self.pressed = True
                self.cElevation = 0
                return True
            else:
                self.cElevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.cElevation = self.elevation
            self.primary = self.hPrimary
            
class imgButton:
    def __init__(self, image, pos, scale = 1, bgSize = (0,0), colors = ('#000000','#FFFFFF'), RadEl = (0,0)):
        
            #Attributes for press detection and "animations"
        #Static Attributes
        self.pressed = False
        self.yPos = pos[1]
        #Dynamic Attributes
        self.dyn_elevation = RadEl[1]
        self.dyn_primary = colors[0]
        
        
        #Image processing / formatting
        width = image.get_width()
        height = image.get_height()
        
        self.image = image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)
        
        #Button surface (for buttons with an image over a standard backgorund)
        #Colors
        self.primary = colors[0]
        self.secondary = colors[1]
        #Modifiers
        self.rad = RadEl[0]
        self.elevation = RadEl[1]
        #Size
        self.bgWidth = bgSize[0]
        self.bgHeight = bgSize[1]
        #Rect surfaces
        self.top_rect = pygame.Rect(pos,(self.bgWidth,self.bgHeight))
        self.bottom_rect = pygame.Rect(pos,(self.bgWidth,self.elevation))
        #Image centering
        self.img_rect = image.get_rect()
        self.img_rect.center = self.top_rect.center
        
        
    def draw(self,surface):
        
        if self.elevation > 0:
            self.top_rect.y = self.yPos - self.dyn_elevation
            self.img_rect.center = self.top_rect.center
            
            self.bottom_rect.midtop = self.top_rect.midtop
            self.bottom_rect.height = self.top_rect.height + self.dyn_elevation
        
        pygame.draw.rect(surface, self.secondary, self.bottom_rect, border_radius = self.rad)
        pygame.draw.rect(surface, self.primary, self.top_rect, border_radius = self.rad)
        surface.blit(self.image, self.img_rect)
        
    def checkPressed(self, hover = False, color = '#333333'):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.top_rect.collidepoint(mouse_pos) or self.img_rect.collidepoint(mouse_pos):
            if hover == True:
               self.dny_primary = color
            if pygame.mouse.get_pressed()[0] == 1:
                self.pressed = True
                self.dyn_elevation = 0
                return True
            else:
                self.dyn_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dyn_elevation = self.elevation
            self.dny_primary = self.primary
            
            
#BELOW I AM BUILDING THE ULTIMATE BUTTON CLASS
    #FUCK THIS GARBAGE ABOVE IT WAS AN UNOPTIMIZED STEAMING PILE OF SHIT AND I AM HERE TO AMMEND MY MISTAKES
class button():
    def __init__(self, content, size, pos):
        
        #Static Attributes
        self.cont = content
        self.size = size
        self.pos = pos
        #Dynamic Attributes
        
        if type(content) == str:
            #Text button goes here
        else:
            #Image button goes here 