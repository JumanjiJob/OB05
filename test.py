import pygame
import sys

pygame.init()

screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Аэрохоккей для двоих")

# Счетчики выигранных очков
player1 = 0
player2 = 0

# Параметры платформы 1
paddle1_width, paddle1_height = 100, 10
paddle1_x = (screen_width - paddle1_width) // 2  # Центрирование платформы
paddle1_y = screen_height - 40  # Положение платформы 1
paddle1_speed = 20

# Параметры платформы 2
paddle2_width, paddle2_height = 100, 10
paddle2_x = (screen_width - paddle2_width) // 2  # Центрирование платформы
paddle2_y = 30  # Положение платформы 2

# Параметры мяча
ball_radius = 8
ball_x = screen_width // 2  # Начальное положение мяча по X
ball_y = screen_height // 2  # Начальное положение мяча по Y
ball_speed_x = 4
ball_speed_y = -4

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
fps = 60

# Флаг паузы
paused = False

# Запуск основного цикла игры
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Проверка нажатия клавиши P для паузы
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused  # Переключаем состояние паузы

    if not paused:  # Игра продолжается
        # Движение мяча
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Столкновение с краями экрана
        if ball_x <= 0 or ball_x >= screen_width:
            ball_speed_x = -ball_speed_x

        # Подсчет выигранных очков
        if ball_y <= 0:
            ball_x = screen_width // 2
            ball_y = screen_height // 2
            player1 += 1
        if ball_y >= screen_height:
            player2 += 1
            ball_x = screen_width // 2
            ball_y = screen_height // 2

        # Управление движением платформы1 с помощью клавиатуры
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle1_x > 0:
            paddle1_x -= paddle1_speed
        if keys[pygame.K_RIGHT] and paddle1_x < screen_width - paddle1_width:
            paddle1_x += paddle1_speed

        # Управление движением платформы2 с помощью мыши
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            paddle2_x = mouseX - paddle2_width // 2

        # Столкновение с платформами
        if paddle1_x <= ball_x <= paddle1_x + paddle1_width and paddle1_y <= ball_y + ball_radius <= paddle1_y + paddle1_height:
            ball_speed_y = -ball_speed_y

        if paddle2_x <= ball_x <= paddle2_x + paddle2_width and paddle2_y <= ball_y + ball_radius <= paddle2_y + paddle2_height:
            ball_speed_y = -ball_speed_y

    # Очистка экрана перед каждым новым кадром
    screen.fill(BLACK)

    # Рисование объектов
    pygame.draw.rect(screen, GREEN, (paddle1_x, paddle1_y, paddle1_width, paddle1_height))
    pygame.draw.rect(screen, RED, (paddle2_x, paddle2_y, paddle2_width, paddle2_height))
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    # Отображение счета
    font1 = pygame.font.SysFont(None, 36)
    count_text1 = font1.render(f"Игрок 1: {player1}", True, WHITE)
    screen.blit(count_text1, (10, 10))
    font2 = pygame.font.SysFont(None, 36)
    count_text2 = font2.render(f"Игрок 2: {player2}", True, WHITE)
    screen.blit(count_text2, (10, 35))

    # Отображение текста паузы
    if paused:
        pause_font = pygame.font.SysFont(None, 48)
        pause_text = pause_font.render("Игра на паузе", True, WHITE)
        screen.blit(pause_text, (screen_width // 2 - pause_text.get_width() // 2, screen_height // 2 - pause_text.get_height() // 2))

    # Обновление экрана
    pygame.display.flip()

    # Контроль ФПС
    clock.tick(fps)

# Завершение игры
pygame.quit()
sys.exit()
