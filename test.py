import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image = pygame.image.load("img/picPython1.png")
image_rect = image.get_rect()

speed = 5

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    # Проверка на границы окна
    if image_rect.left < 0:
        image_rect.left = 0
    if image_rect.right > window_size[0]:
        image_rect.right = window_size[0]
    if image_rect.top < 0:
        image_rect.top = 0
    if image_rect.bottom > window_size[1]:
        image_rect.bottom = window_size[1]

    screen.fill((75, 0, 75))
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()
