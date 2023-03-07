#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
#import keys
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#normal screen size
screen_width = 800
screen_height = 600
#sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Spritesheets')
#enter .jpeg name
sprite_sheet_image = pygame.image.load('sprite name').conver_alpha()


player = Player()

running = True
#Main loop
while running:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    pressed_keys = pygame.key.get_pressed()
    
    player.update(pressed_keys)
    
    screen.fill((255,255,255))
    
    surf = pygame.Surface((50,50))
    
    surf.fill((0,0,0))
    
    rect = surf.get_rect()
    
    screen.blit(player.surf, (screen_width/2, screen_height/2))
    
    pygame.display.flip()

pygame.quit()

