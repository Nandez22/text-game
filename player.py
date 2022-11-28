import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        
    def import_assets(self):
        char_path = '../assets/character/'
        self.animation = {'idle':[], 'run':[], 'jump':[], 'fall':[]}
        
        for animation in self.animations.keys():
            full_path = char_path + animation
        
        
    def work(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.direction.x = 1
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]:
            self.jump()
             
    def jump(self):
        self.direction.y = self.jump_speed
    
    def call_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
      
    def update(self):
        self.work()
        self.rect.x += self.direction.x * self.speed
