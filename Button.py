import pygame
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
                rect_width = (img_width * self.scale)
            else:
                rect_width = size[0]
                
            if size[1] == 'image':
                rect_height = (img_height * self.scale)
            else:
                rect_height = size[1]
            
            #Rect Creation
            self.top_rect = pygame.Rect(pos,(rect_width,rect_height))
            self.bottom_rect = pygame.Rect(pos,(rect_width,self.elevation))
            
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