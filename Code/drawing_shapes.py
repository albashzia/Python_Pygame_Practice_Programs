import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill("white")
pygame.display.set_caption("Drawing shapes on surface")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.display.flip()