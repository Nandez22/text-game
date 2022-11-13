import pygame,sys

pygame.init()
pygame.font.init()

class button():
    def __init__(self,content,pos,size,colors):
        
        self.pos = pos
        self.primary = colors[0]
        self.secondary = colors[1]
        
        
        if type(content) == tuple:

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
            
            #Text Creation
            self.content_surface = self.format.render(self.text,self.anti_a,self.txt_color)
            self.content_rect = self.content_surface.get_rect(center = self.top_rect.center)
            
            
        else:

            #Rect attributes
            self.image = content
            self.scale = size
            
            #Image Attributes
            
            #Rect Creation
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
            #Image Creation
            
            
            
            
            

    def draw(self,surface):
        pygame.draw.rect(surface, self.primary, self.top_rect)
        screen.blit(self.content_surface, self.content_rect)
        
        
        
sourceTxt = ('Text',12,'#FFFFFF','arialblack',True)        
button1 = button(sourceTxt,((100,100)),((100,100)),('#333333','#333333'))
        
        
        

screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
pygame.display.set_caption('Pussy')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill('#DCDDD8')    
    
    button1.draw(screen)
    
    
    
    pygame.display.update()
    clock.tick(60)