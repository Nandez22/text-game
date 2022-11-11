import pygame

class txtButton:
    def __init__(self, text = 'button', width = 200, height = 50, primary = '#000000', pos = (0,0), rad = 0, elevation = 0, secondary = '#FFFFFF'):

        #Setting basic attributes --
        #Dynamic Atributes
        self.pressed = False
        self.cElevation = elevation
        self.primary = primary
        
        #Static Atributes
        self.hPrimary = primary
        self.secondary = secondary
        self.elevation = elevation
        self.staticY = pos[1]
        self.rad = rad
        self.format = pygame.font.Font(None,30)
        
        #Primary button surface
        self.top_rect = pygame.Rect(pos,(width,height))     
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
    def __init__(self, image, pos = (0,0), scale = 1, bgSize = (0,0), primary = '#000000', rad = 0):
        
        #Image processing / formatting
        width = image.get_width()
        height = image.get_height()
        self.image = image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)
        
        #Button surface (for buttons with an image over a standard backgorund)
        self.primary = primary
        
        self.rad = rad
        self.bgWidth = bgSize[0]
        self.bgHeight = bgSize[1]
        
        self.top_rect = pygame.Rect(pos,(self.bgWidth,self.bgHeight))
        self.img_rect = image.get_rect()
        self.img_rect.center = self.top_rect.center
        
        
        
        
    def draw(self,surface):
        
        pygame.draw.rect(surface, self.primary, self.top_rect, border_radius = self.rad)
        surface.blit(self.image, self.img_rect)
        
        