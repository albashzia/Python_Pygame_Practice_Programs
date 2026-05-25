import pygame

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill("white")
pygame.display.set_caption("Key Events")

x = 0
y = 0
rect_width = 50
rect_height = 50
velocity = 5

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.display.flip()