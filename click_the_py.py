import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ClickThePy")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

countdown_time = 3
start_time = time.time()
timer_seconds = countdown_time

while timer_seconds > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    elapsed_time_seconds = time.time() - start_time
    timer_seconds = max(0, countdown_time - int(elapsed_time_seconds))

    timer_text = font.render(f"Time: {timer_seconds}", True, WHITE)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

game_over_text = font.render("Game Over", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
pygame.display.flip()
time.sleep(2)

pygame.quit()
sys.exit()
