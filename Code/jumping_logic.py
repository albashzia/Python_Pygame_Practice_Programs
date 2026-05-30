import pygame

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Key Events")

x = 0
y = 0
rect_width = 50
rect_height = 50
velocity = 3

clock = pygame.time.Clock()

is_jumping = False
jump_height = 10

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
    if keys[pygame.K_SPACE]:
        is_jumping = True

    if is_jumping:
        if jump_height >= -10:
            neg = 1
            if jump_height < 0:
                neg = -1
            y -= (jump_height**2)*neg*0.5
            jump_height -= 1
        else:
            jump_height = 10
            is_jumping = False

    screen.fill("white")
    pygame.draw.rect(screen,"black",(x,y,rect_width,rect_height))
    clock.tick(60)
    pygame.display.flip()