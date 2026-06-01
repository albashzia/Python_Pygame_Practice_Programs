import pygame

pygame.init()

screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("Background Image")

bg_image = pygame.image.load("../Images/background_house.jpg")
bg_image = pygame.transform.scale(bg_image,(300,300))

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.blit(bg_image,(0,0))
    pygame.display.flip()