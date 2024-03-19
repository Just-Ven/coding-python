import pygame

pygame.init()
WIDTH = 800
HEIGHT = 500

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Moving Circle')
pygame.display.set_icon(pygame.image.load('lab 7/img/ball-icon.jpg'))

x0 = WIDTH // 2
y0 = HEIGHT // 2
RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60
movement = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x0 > 25:
        x0 -= movement
    elif keys[pygame.K_RIGHT] and x0 < 775:
        x0 += movement
    elif keys[pygame.K_UP] and y0 > 25:
        y0 -= movement
    elif keys[pygame.K_DOWN] and y0 < 475:
        y0 += movement

    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x0, y0), 25)

    pygame.display.update()

    clock.tick(FPS)