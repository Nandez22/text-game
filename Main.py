import pygame, sys


#todo NOTES FOR BUTTON CLASS
#* - Add more cusomizers (things like 'border_radius' should be changable in the class arguments)
#*      -- To add to that, it should not be a required argument and should default to 0 (sharp)
#*          -- To double down, all aspects of the button should have a defualt so calling as little as 'button1 = button()' should be enough to generate something on screen.
#* - I'll add more later I need to poop.
#* -
#* -
class txtButton:
    def __init__(self, text = 'button', width = 200, height = 50, primary = '#000000', pos = (0,0), rad = 0, elevation = 0, secondary = '#FFFFFF',):

        
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
        
        
        #Primary button surface
        self.top_rect = pygame.Rect(pos,(width,height))     
        #Secondary button surface
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = secondary
        
        #Text
        #-- gui_font.render(what,anti-aliased?,color(hex))
        self.text_plane = gui_font.render(text,True,'#FFFFFF')
        #Pos of text relative to the outer rect
        self.text_rect = self.text_plane.get_rect(center = self.top_rect.center)
        
    def draw(self):
        if self.elevation > 0:
            self.top_rect.y = self.staticY - self.cElevation
            self.text_rect.center = self.top_rect.center
        
        #Draw is for shapes, and things that can be "drawn"
        pygame.draw.rect(screen, self.primary, self.top_rect, border_radius = self.rad)
        #Blit is for not drawn things IE; text and other 'objects'
        screen.blit(self.text_plane,self.text_rect)
            
            
    def checkPress(self,hover = False, color = '#333333'):
        #Finds mouse position
        mouse_pos = pygame.mouse.get_pos()     
        #Checks to see if the mouse is overlapping / 'colliding' with the button
        if self.top_rect.collidepoint(mouse_pos):
            if hover == True:
                self.primary = color
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                self.cElevation = 0
                return True
            else:
                self.cElevation = self.elevation
            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False
        else:
            self.primary = self.hPrimary
            
   
            
            
            
pygame.init()
mouse_pos = pygame.mouse.get_pos()       
screen = pygame.display.set_mode(((500,500)), pygame.RESIZABLE)
pygame.display.set_caption('Name')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)

#INSTANCE DEFINING OF SOME KIND
#------------------------------

testButton = txtButton('Test',200,40,'#f59542',(150,230),5,5)

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
    testButton.checkPress(True)
    #------------------------------

    
    pygame.display.update()
    clock.tick(60)