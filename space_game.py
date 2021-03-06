import pygame
import sys
from gun import Gun
import controls
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Space Invaders')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)
        bullets.update()
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bulltes(bullets)


run()
