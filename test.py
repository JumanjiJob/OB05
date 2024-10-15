import pygame
import sys

pygame.init()

screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Тетрис")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
fps = 60

# Параметры платформы
paddle_width, paddle_height = 100, 40
paddle_speed = 6

# Начальная позиция платформы
def create_new_paddle():
    return (0, 0)  # Платформа появляется в верхней левой части экрана

# Флаг остановки платформы
platform_stopped = False

# Инициализация первой платформы
paddle_x, paddle_y = create_new_paddle()

# Счетчик платформ
paddle_count = 0

# Список для сохранения предыдущих платформ
paddles = []

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
            paddles.append((paddle_x, paddle_y))  # Добавляем остановившуюся платформу в список
            platform_stopped = True  # Устанавливаем флаг остановки
            paddle_count += 1  # Увеличиваем счетчик платформ

    else:
        # Если платформа остановилась, создаем новую платформу
        paddle_x, paddle_y = create_new_paddle()
        platform_stopped = False

    # Очистка экрана перед каждым новым кадром
    screen.fill(BLACK)

    # Рисование всех предыдущих платформ
    for px, py in paddles:
        pygame.draw.rect(screen, WHITE, (px, py, paddle_width, paddle_height))

    # Рисование текущей движущейся платформы
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Отображение счетчика платформ
    font = pygame.font.SysFont(None, 36)
    count_text = font.render(f"Платформы: {paddle_count}", True, WHITE)
    screen.blit(count_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

    # Контроль ФПС
    clock.tick(fps)

# Завершение игры
pygame.quit()
sys.exit()
