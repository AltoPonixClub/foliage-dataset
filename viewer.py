import pygame

pygame.init()
width = 350
height = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Viewer')
running = True
counter = 0;
while(running):
    counter += 1
    image = pygame.image.load(counter + ".png").convert()
    imageMask = pygame.image.load(counter + ".png").convert()
    x = 20
    y = 30
    screen.blit(image, (x, y))
    s = pygame.Surface((1000, 750))
    s.set_alpha(128)
    s.fill((255, 255, 255))
    screen.blit(s, (x, y))
    pygame.display.flip()
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
pygame.quit()