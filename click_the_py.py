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
wave_time = 10

SPAWN_RATE = 2
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
wave_number = STARTING_ROUND
wave_timer = wave_time

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
    )

def create_falling_object():
    global total_objects_spawned
    total_objects_spawned += 1
    x = random.randint(0, WIDTH - 50)
    y = 0
    speed = random.randint(2 , 5)
    return {'rect': pygame.Rect(x, y, 50, 50), 'speed': speed}


def update_objects():
    global falling_objects
    for obj in falling_objects:
        obj['rect'].move_ip(0, obj['speed'])
    falling_objects = [obj for obj in falling_objects if obj['rect'].top <= HEIGHT]

def spawn_new_object():
    falling_objects.append(create_falling_object())

def draw_total_objects_spawned():
    total_objects_text = font.render(f"Total Objects Spawned: {total_objects_spawned}", True, WHITE)
    screen.blit(total_objects_text, (WIDTH // 2 - 150, HEIGHT - 50))

def draw_falling_objects():
    for obj in falling_objects:
        screen.blit(image, obj['rect'])

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
def draw_timer():
    wave_timer_text = font.render(f"Time left: {countdown_time}", True, WHITE)
    screen.blit(wave_timer_text, (10, 50))  # Adjust the position to (10, 50) for left side

def draw_wave_timer(wave_timer_seconds):
    wave_timer_text = font.render(f"Wave Time: {wave_timer_seconds:.2f}", True, WHITE)
    text_rect = wave_timer_text.get_rect()
    text_rect.topright = (WIDTH - 10, 10)
    screen.blit(wave_timer_text, text_rect)


def draw_wave_number(wave_number):
    wave_number_text = font.render(f"Wave #{wave_number}", True, WHITE)
    screen.blit(wave_number_text, (WIDTH - 425, 30))

def draw_SPAWN_RATE():
    SPAWN_RATE_text = font.render(f"Spawn rate is: {SPAWN_RATE}", True, WHITE)
    screen.blit(SPAWN_RATE_text, (WIDTH // 2 - 150, HEIGHT - 100))



def draw_screen(wave_timer_seconds, wave_number):
    screen.fill(BLACK)
    draw_falling_objects()
    draw_score()
    draw_timer()
    draw_wave_timer(wave_timer_seconds)
    draw_wave_number(wave_number)
    draw_total_objects_spawned()
    draw_SPAWN_RATE()
    pygame.display.flip()

def game_over_screen():
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
    pygame.display.flip()
    time.sleep(2)


def change_waves():
    global wave_timer, wave_number, INITIAL_COUNTDOWN_TIME, SPAWN_RATE
    wave_number += 1
    wave_timer = wave_time
    SPAWN_RATE +=1
def handle_events():
    global score, wave_number, wave_timer, countdown_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in falling_objects:
                if obj['rect'].collidepoint(event.pos):
                    falling_objects.remove(obj)
                    score += 1

    if countdown_time <= 0:
        pygame.quit()
        sys.exit()



def main():
    screen, clock, font, image, falling_objects, score, start_time, current_round_time = initialize_game()
    global countdown_time, wave_timer, SPAWN_RATE

    while True:
        handle_events()
        update_objects()

        elapsed_time_seconds = time.time() - start_time
        dt = clock.tick(FPS) / 1000.0  # Convert to seconds

        countdown_time = max(0, INITIAL_COUNTDOWN_TIME - int(elapsed_time_seconds))
        wave_timer = max(0, wave_timer - dt)

        if wave_timer <= 0:
            change_waves()

        # Check if it's time to spawn a new object based on SPAWN_RATE
        if random.random() < SPAWN_RATE * dt:
            spawn_new_object()

        draw_screen(wave_timer, wave_number)
        pygame.display.flip()

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
