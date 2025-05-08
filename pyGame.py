import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_x = 100
player_y = 100
speed = 5

running = True
while running:
    screen.fill((0, 0, 0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, 50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
