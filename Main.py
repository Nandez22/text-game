import pygame, sys
class txtButton:
    def __init__(self, text, width, height, pos):
        
        self.top_rect = pygame.Rect(pos,(width,height))
        self.primary = '#f59542'
    
        self.text_plane = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_plane.get_rect(center = self.top_rect.center)
        
    def draw(self):
        pygame.draw.rect(screen,self.primary,self.top_rect)
        screen.blit(self.text_plane,self.text_rect)
            
            
            
            
            
            
            
            
pygame.init()
screen = pygame.display.set_mode(((500,500)), pygame.RESIZABLE)
pygame.display.set_caption('Name')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)

#INSTANCE DEFINING OF SOME KIND
#------------------------------

testButton = txtButton('Test',200,40,(20,20))

#------------------------------

while True:
    #Exit logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #ACTUAL CONTENT GOES BELOW LINE
    #------------------------------
    screen.fill((121,128,241))
    testButton.draw()
    
    #------------------------------

    
    pygame.display.update()
    clock.tick(60)