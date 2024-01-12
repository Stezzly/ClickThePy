import pygame
import sys
import time
import random

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
INITIAL_COUNTDOWN_TIME = 10
SPAWN_RATE = 2

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

def initialize_game():
    """Initialize the Pygame window and game variables."""
    return pygame.display.set_mode((WIDTH, HEIGHT)), pygame.time.Clock(), INITIAL_COUNTDOWN_TIME, pygame.font.Font(None, 36), pygame.image.load("BlueberryPie.png"), [], 0

def create_falling_object():
    """Create a falling object with random position and speed."""
    x = random.randint(0, WIDTH - 50)
    y = 0
    speed = random.randint(2, 5)
    return {'rect': pygame.Rect(x, y, 50, 50), 'speed': speed}

def handle_events():
    global score
    """Handle Pygame events."""
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
    """Update positions of falling objects."""
    for obj in falling_objects:
        obj['rect'].move_ip(0, obj['speed'])
    falling_objects = [obj for obj in falling_objects if obj['rect'].top <= HEIGHT]

def spawn_new_object():
    """Spawn a new falling object."""
    falling_objects.append(create_falling_object())

def draw_screen(timer_seconds):
    """Draw the game screen."""
    screen.fill(BLACK)
    for obj in falling_objects:
        screen.blit(image, obj['rect'])

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    timer_text = font.render(f"Time: {timer_seconds}", True, WHITE)
    screen.blit(timer_text, (10, 50))

    pygame.display.flip()

def game_over_screen():
    """Display the game over screen."""
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
    pygame.display.flip()
    time.sleep(2)

def main():
    screen, clock, countdown_time, font, image, falling_objects, score = initialize_game()
    frames_per_spawn = int(FPS / SPAWN_RATE)
    spawn_counter = 0

    while countdown_time > 0:
        handle_events()
        update_objects()

        spawn_counter += 1
        if spawn_counter >= frames_per_spawn:
            spawn_new_object()
            spawn_counter = 0

        elapsed_time_seconds = time.time() - start_time
        countdown_time = max(0, INITIAL_COUNTDOWN_TIME - int(elapsed_time_seconds))

        draw_screen(countdown_time)
        clock.tick(FPS)

    game_over_screen()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
