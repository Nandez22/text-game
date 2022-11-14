import pygame, elements, sys
pygame.init()
surface = elements.set_screen((800,600),'Test')
clock = pygame.time.Clock()

size = (100,25)
pos = (400,300)

active_rect = 'Fullscreen'
options = ['Fullscreen', 'Windowed Borderless', 'Windowed']
format = pygame.font.SysFont('arialblack',20)
rects = {}
txt_surfaces = {}
txt_rects = {}
primary = '#666666'
actvie = '#FFFFFF'


#Generating background rects
for option in options:
     rects[option] = pygame.Rect(pos,size)
#Generating text rects
for option in options:
    txt_surfaces[option] = format.render(option,True,primary)
    txt_rects[option] = txt_surfaces[option].get_rect()    

print(txt_rects)

print(rects)

while True:
    
    surface.fill((121,128,241))
    
    #if active_rect == 'Fullscreen':
        
      
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gamePaused = True
                menu = 'paused'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)