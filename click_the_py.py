import pygame
import sys
import time
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ClickThePy")
clock = pygame.time.Clock()
countdown_time = 10  # Adjusted countdown time for testing
start_time = time.time()
timer_seconds = countdown_time
font = pygame.font.Font(None, 36)
image = pygame.image.load("BlueberryPie.png")
image = pygame.transform.scale(image, (50, 50))
falling_objects = []
score = 0

def create_falling_object():
    x = random.randint(0, WIDTH - 50)
    y = 0
    speed = random.randint(2, 5)
    return {'rect': pygame.Rect(x, y, 50, 50), 'speed': speed}

while timer_seconds > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for obj in falling_objects:
                if obj['rect'].collidepoint(event.pos):
                    falling_objects.remove(obj)
                    score += 1

    for obj in falling_objects:
        obj['rect'].move_ip(0, obj['speed'])
    falling_objects = [obj for obj in falling_objects if obj['rect'].top <= HEIGHT]

    if random.random() < 0.02:
        falling_objects.append(create_falling_object())

    screen.fill(BLACK)

    for obj in falling_objects:
        screen.blit(image, obj['rect'])
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    elapsed_time_seconds = time.time() - start_time
    timer_seconds = max(0, countdown_time - int(elapsed_time_seconds))

    timer_text = font.render(f"Time: {timer_seconds}", True, WHITE)
    screen.blit(timer_text, (10, 50))

    pygame.display.flip()
    clock.tick(FPS)

game_over_text = font.render("Game Over", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
pygame.display.flip()
time.sleep(2)

pygame.quit()
sys.exit()
