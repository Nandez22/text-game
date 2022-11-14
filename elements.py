import pygame, sys, button
#Elements is a place for premade functions like 'draw_text', just quality of life things...
# *optional* values do not need to be enterd at the function call and will result in the default value specified by the function overload.


#This is for setting the screen dimensions, especially helpful when making new windos / menus
#Inputs as follows;
    # -1. Size of the window (set as (width,height))
    # -2. The 'name' of the window (set as "string") *optional* 
        #! If you do not set a window caption / name pygame will automatically set the name of the window to "Window"
    # -3. Set to true if you want the window resizable (input as True or False) *optional*
def set_screen(size, caption = False, resize = False):
    if caption != False:
        pygame.display.set_caption(caption)
        
    if resize == True:
        return pygame.display.set_mode(((size[0],size[1])), pygame.RESIZABLE)
    else:
        return pygame.display.set_mode(((size[0],size[1])))


#This is for setting text on the screen
#If it wasnt obvious the inputs are as follows:
    # -1. Text to display
    # -2. Font (defined by font = pygame.font.SysFont("fontName", size))
    # -3. Color (can be any format but RGB must be a tuple and hex must be in quotes (IE; ((R, G, B)) or '#FFFFFF'))
    # -4. The screen surface (defined by set_screen (see above))
    # -5. Position (entered as (x,y))
def draw_text(text, font, color, surface, pos = (0,0), orientation = 'center'):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    
    if orientation == 'center':
        text_rect.center = pos
    if orientation == 'topleft':
        text_rect.topleft = (pos)
    surface.blit(text_obj, text_rect)
