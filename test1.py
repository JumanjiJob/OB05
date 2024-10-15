import pygame
import sys

pygame.init()

screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Тетрис")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255,0,0)

clock = pygame.time.Clock()
fps = 60

# Параметры платформы
paddle_width, paddle_height = 100, 40
paddle_x = 0
paddle_y = 0
paddle_speed = 6

# Флаг остановки платформы
platform_stopped = False

# Запуск основного цикла игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение платформы
    if not platform_stopped:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        # Проверка, достигла ли платформа низа экрана
        if paddle_y + paddle_height < screen_height:
            paddle_y += paddle_speed  # Платформа движется вниз
        else:
            paddle_y = screen_height - paddle_height  # Останавливается на нижней границе
            platform_stopped = True  # Исправлено имя переменной

    # Очистка экрана перед каждым новым кадром
    screen.fill(BLACK)

    # Рисование объектов
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Обновление экрана
    pygame.display.flip()

    # Контроль ФПС
    clock.tick(fps)

# Завершение игры
pygame.quit()
sys.exit()
