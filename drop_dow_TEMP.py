import pygame, elements, sys
pygame.init()
surface = elements.set_screen((800,600),'Test')
clock = pygame.time.Clock()

size = (100,25)
pos = (400,300)

active_rect = 'Fullscreen'
options = ['Fullscreen', 'Windowed Borderless', 'Windowed']
format = pygame.font.SysFont('arialblack',10)

primary = '#666666'
actvie = '#FFFFFF'

rects = {}
txt_surfaces = {}
txt_rects = {}
#TODO This may get condenced into one dict containing Tuples as values, still need to determine if that is worth the conversion...
#Generating background rects
for option in options:
     rects[option] = pygame.Rect(pos,size)
#Generating text rects
for option in options:
    txt_surfaces[option] = format.render(option,True,primary)
    txt_rects[option] = txt_surfaces[option].get_rect(center = rects[option].center)    

print(txt_rects)

print(rects)

while True:
    
    surface.fill((121,128,241))
    
    for option in options:
        if active_rect == option:
            rects[option].center = pos
        else:
            rects[option].midtop = rects[active_rect].midbottom
    
    for option in options:
        pygame.draw.rect(surface, primary, rects[option], border_radius = 5)
        surface.blit(txt_surfaces[option], txt_rects[option])
    
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