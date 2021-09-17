import pygame
import time
freq = float(input("What oscilation frequency? \n"))
delay = 1/freq
pygame.init()
color = 1 #0 for black 1 for white
screen = pygame.display.set_mode([500, 500])
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                running = False
    if color == 1:
        screen.fill((255, 255, 255))
        time.sleep(delay)
        pygame.display.flip()
        color = 0
    if color == 0:
        screen.fill((0,0,0))
        time.sleep(delay)
        pygame.display.flip()
        color = 1

pygame.quit()
print("Thanks for trying the neural entrainer!")
