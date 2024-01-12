import pygame
import sys
import time
import random

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
INITIAL_COUNTDOWN_TIME = 60
SPAWN_RATE = 2
ROUND_TIME = 10
STARTING_ROUND = 1

# Initialize Pygame
pygame.init()

# Set up game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ClickThePy")
clock = pygame.time.Clock()

# Set game variables
start_time = time.time()
countdown_time = INITIAL_COUNTDOWN_TIME
font = pygame.font.Font(None, 36)
image = pygame.image.load("BlueberryPie.png")
image = pygame.transform.scale(image, (50, 50))
falling_objects = []
score = 0
total_objects_spawned = 0
round_number = STARTING_ROUND
current_round_time = ROUND_TIME

def initialize_game():
    return (
        pygame.display.set_mode((WIDTH, HEIGHT)),
        pygame.time.Clock(),
        pygame.font.Font(None, 36),
        pygame.image.load("BlueberryPie.png"),
        [],
        0,
        time.time(),
        STARTING_ROUND,
        ROUND_TIME,  # Initialize current_round_time correctly
    )

def create_falling_object():
    global total_objects_spawned
    total_objects_spawned += 1
    x = random.randint(0, WIDTH - 50)
    y = 0
    speed = random.randint(2 + round_number, 5 + round_number)
    return {'rect': pygame.Rect(x, y, 50, 50), 'speed': speed}

def draw_total_objects_spawned():
    total_objects_text = font.render(f"Total Objects Spawned: {total_objects_spawned}", True, WHITE)
    screen.blit(total_objects_text, (WIDTH // 2 - 150, HEIGHT - 50))

def draw_falling_objects():
    for obj in falling_objects:
        screen.blit(image, obj['rect'])

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
def draw_timer(time):
    wave_timer_text = font.render(f"Wave Time: {countdown_time}", True, WHITE)
    screen.blit(wave_timer_text, (10, 50))  # Adjust the position to (10, 50) for left side

def draw_wave_timer(wave_timer_seconds):
    wave_timer_text = font.render(f"Wave Time: {wave_timer_seconds}", True, WHITE)
    screen.blit(wave_timer_text, (WIDTH - 200, 50))

def draw_SPAWN_RATE():
    SPAWN_RATE_text = font.render(f"Spawn rate is: {SPAWN_RATE}", True, WHITE)
    screen.blit(SPAWN_RATE_text, (WIDTH - 250, 30))

def draw_screen(timer_seconds, wave_timer_seconds):
    screen.fill(BLACK)
    draw_falling_objects()
    draw_score()
    draw_timer(timer_seconds)
    draw_wave_timer(wave_timer_seconds)
    draw_total_objects_spawned()  # Display total objects spawned
    draw_SPAWN_RATE()
    pygame.display.flip()


def handle_events():
    global score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for obj in falling_objects:
                if obj['rect'].collidepoint(event.pos):
                    falling_objects.remove(obj)
                    score += 1

def update_objects():
    global falling_objects
    for obj in falling_objects:
        obj['rect'].move_ip(0, obj['speed'])
    falling_objects = [obj for obj in falling_objects if obj['rect'].top <= HEIGHT]

def spawn_new_object():
    falling_objects.append(create_falling_object())

def game_over_screen():
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
    pygame.display.flip()
    time.sleep(2)


def main():
    screen, clock, font, image, falling_objects, score, start_time, round_number, current_round_time = initialize_game()
    frames_per_spawn = int(FPS / SPAWN_RATE)
    spawn_counter = 0

    while True:
        handle_events()
        update_objects()

        spawn_counter += 1
        if spawn_counter >= frames_per_spawn:
            spawn_new_object()
            spawn_counter = 0

        elapsed_time_seconds = time.time() - start_time
        countdown_time = max(0, INITIAL_COUNTDOWN_TIME - int(elapsed_time_seconds))
        wave_timer = max(0, current_round_time - int(elapsed_time_seconds))

        draw_screen(countdown_time, wave_timer)
        clock.tick(FPS)


if __name__ == "__main__":
    main()
