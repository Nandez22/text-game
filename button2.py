import pygame,sys,elements

pygame.init()
pygame.font.init()


screen = elements.set_screen((1000,800),'Get Some', True)

class button():
    def __init__(self,content,pos,size,colors):
        
        self.pos = pos
        self.primary = colors[0]
        self.secondary = colors[1]
        
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
            
            #Text Creation
            self.content_surface = self.format.render(self.text,self.anti_a,self.txt_color)
            self.content_rect = self.content_surface.get_rect(center = self.top_rect.center)
            
            
        else:

            #Rect attributes
            self.size = size
            
            #Image Attributes
            width = content[0].get_width()
            height = content[0].get_height()
            
            
            image = content[0]
            self.scale = content[1]
            self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
            

            
            #Rect Creation
            self.top_rect = pygame.Rect(pos,(size[0],size[1]))
            
            #Image Creation
            self.content_rect = self.image.get_rect()
            self.content_rect.topleft = pos
            
            
            
            

    def draw(self,surface):
        pygame.draw.rect(surface, self.primary, self.top_rect)
        #screen.blit(self.content_surface, self.content_rect)
        
def test():  
    txt1 = ('Text',12,'#FFFFFF','arialblack',True)        
    button1 = button(txt1,(100,100),(100,100),('#333333','#333333'))

    sImg = pygame.image.load('AI.png').convert_alpha()
    img1 = (sImg,1)
    button2 = button(img1,(250,250),(200,50),('#333333','#333333'))



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
        
test()