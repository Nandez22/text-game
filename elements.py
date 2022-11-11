import pygame, sys
#Elements is a place for premade functions like 'draw_text', just quality of life things...

def draw_text(text, font, color, surface, pos = (0,0)):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (pos)
    surface.blit(text_obj, text_rect)