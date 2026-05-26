import pygame

pygame.init()
screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Defining Boundaries")

x = 0
y = 0
rect_width = 50
rect_height = 50
velocity = 3

clock = pygame.time.Clock()

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity

    screen.fill("white")
    pygame.draw.rect(screen,"black",(x,y,rect_width,rect_height))
    clock.tick(60)
    pygame.display.flip()