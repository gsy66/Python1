
import time
import pygame
import sys


pygame.init()

bg_color1 = (0,128,128)
bg_color2 = (60,60,60)
bg_color3 = (255,0,255)

screen_image=pygame.display.set_mode((800,600))
screen_rect = screen_image.get_rect()

pygame.display.set_caption('Alien invasion')
screen_image.fill(bg_color1)
ship_image = pygame.image.load('feiji.bmp')
ship_rect = ship_image.get_rect()
ship_rect.center = screen_rect.center
screen_image.blit(ship_image,ship_rect)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pass
