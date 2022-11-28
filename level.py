import pygame
from sprites import Tile
from settings import tile_size, screen_width
from player import Player

class Level:
    def __init__(self, map, surface):
        self.surface = surface
        self.gen(map)
        
        self.world_shift = 0
        
    def gen(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                                    
                x = (cell_index * tile_size)
                y = (row_index * tile_size)
                    
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                    
                if cell == 'P':
                    player = Player((x,y))
                    self.player.add(player)
                    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < (screen_width / 5) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0                
        elif player_x > (screen_width - (screen_width / 5)) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
        
    def x_collide(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    
    def y_collide(self):
        player = self.player.sprite
        player.call_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
                    
    def play(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
        self.scroll_x()
        
        self.player.update()
        self.x_collide()
        self.y_collide()
        self.player.draw(self.surface)
        
        
    