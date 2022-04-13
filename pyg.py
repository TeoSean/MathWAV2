import pygame

pygame.init()

screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running=True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running=False