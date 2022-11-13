import pygame,sys,elements

pygame.init()
pygame.font.init()

screen = elements.set_screen((1000,800),'Get Some', True)
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
            
            #Text Creation
            self.content_surface = self.format.render(self.text,self.anti_a,self.txt_color)
            self.content_rect = self.content_surface.get_rect(center = self.top_rect.center)
            
        else:
            
            #Image Attributes
            img_width = content[0].get_width()
            img_height = content[0].get_height()
            
            image = content[0]
            self.scale = content[1]
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
            self.content_rect.topleft = (pos)
            
            #Centering
            self.content_rect.center = self.top_rect.center

    def draw(self,surface):
        self.top_rect.y = self.pos[0] - self.dyn_Elevation
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
        else:
            self.dyn_primary = self.primary
        
def test():  
    txt1 = ('Text',20,'#FFFFFF','arialblack',True)        
    button1 = button(txt1,(100,100),(200,50),('#333333','#FFFFFF'),(5,5))

    sImg = pygame.image.load('AI.png').convert_alpha()
    img1 = (sImg,0.08)
    button2 = button(img1,(250,250),(250,'image'),('#333333','#FFFFFF'),(5,5))



    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill('#DCDDD8')    
        
        button1.draw(screen)
        button2.draw(screen)
        button1.checkClick(True)
        button2.checkClick(True,'#FFFFFF')
        
        pygame.display.update()
        clock.tick(60)
        
test()