import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill("white")
pygame.display.set_caption("Drawing shapes on surface")

pygame.draw.line(screen, #surface
                 "black", #color
                 (0,0), #start position
                 (400,400), #end position
                 5 #width
                 )

pygame.draw.lines(screen,
                  "orange",
                  False,
                  [(100,100),(200,50),(300,100)],
                  4)

pygame.draw.rect(screen,
                 "red",
                 (50,50,100,100),
                 7)

pygame.draw.circle(screen,
                   "green",
                   (200,200),
                   30,
                   4)
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.display.flip()