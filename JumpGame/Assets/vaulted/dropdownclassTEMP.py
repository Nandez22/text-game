import pygame, sys, elements

class dropdown:
    def __init__(self, options, size, pos, active):
        self.options = options
        self.size = size
        self.pos = pos
        self.rad = 0
        
        self.dropped = True
        self.pressed = False
        self.active_rect = active
        
        self.txt_selected = '#FFFFFF'
        self.txt_unselected = '#e0e0e0'
        self.format = pygame.font.SysFont('None',17)
        
        self.rect_selected = '#222222'
        self.rect_unselected = '#333333'
        self.dyn_unselected = '#333333'
        
        self.rects = {}
        self.txt_surfaces = {}
        self.txt_rects = {}
        
        
        for option in self.options:
            self.rects[option] = pygame.Rect(pos,size)
            
    def draw(self, surface):
        self.surface = surface
        self.mouse_pos = pygame.mouse.get_pos()
        
        for option in self.options:
            if self.active_rect == option:
                self.rects[option].center = self.pos
                
                self.txt_surfaces[option] = self.format.render(option, True, self.txt_selected)
                self.txt_rects[option] = self.txt_surfaces[option].get_rect(center = self.rects[option].center)
                
                pygame.draw.rect(self.surface, self.rect_selected, self.rects[option], border_radius = self.rad)
                self.surface.blit(self.txt_surfaces[option], self.txt_rects[option])

    def drop(self,Hover = False, color = '#FF0000'):
        self.hover = Hover
        self.hover_color = color

        order = []
        if self.rects[self.active_rect].collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.dropped = True
        elif not self.rects[self.active_rect].collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.dropped = False
                
        if self.dropped == True:
            for option in self.options:
                if option != self.active_rect:
                    self.txt_surfaces[option] = self.format.render(option, True, self.txt_unselected)
                    self.txt_rects[option] = self.txt_surfaces[option].get_rect(center = self.rects[option].center)
                    
                    order.append(option)
                    lstPos = 0
                    for option in order:
                        if option == order[0]:
                            self.rects[option].midtop = self.rects[self.active_rect].midbottom
                        else:
                            self.rects[option].midtop = self.rects[order[(lstPos - 1)]].midbottom
                        lstPos += 1
                    
                    #--HOVER / Click DETECTION-------------------------
                    if self.rects[option].collidepoint(self.mouse_pos):
                        if self.hover == True:
                            self.dyn_unselected = self.hover_color
                    else:
                        self.dyn_unselected = self.rect_unselected
                    #--------------------------------------------------
                    
                    
                    
                    pygame.draw.rect(self.surface, self.dyn_unselected, self.rects[option], border_radius = self.rad)
                    self.surface.blit(self.txt_surfaces[option], self.txt_rects[option])   
                      
    def checkClick(self):
        
        for option in self.options:
            if self.rects[option].collidepoint(self.mouse_pos) and self.rects[option] != self.active_rect:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.active_rect = option
                    self.pressed = True
                else:
                    if self.pressed == True:
                        self.pressed = False
    
    def style(self, colors, txt_colors, font, rad = 0):
        self.rect_selected = colors[0]
        self.rect_unselected = colors[1]
        self.dyn_unselected = colors[1]
        
        self.txt_selected = txt_colors[0]
        self.txt_unselected = txt_colors[1]
        
        self.format = font
        self.rad = rad
        #! RAD not recommended -- Looks like dookie
        
    #! As of current there is very little user customization that needs to change
        #! Still trying to determine if most should be done with setters of if they should be args in '__init__' / 'draw'