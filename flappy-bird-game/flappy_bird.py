import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
CLOCK = pygame.time.Clock()
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Bird parameters
bird_size = 20
bird_x = SCREEN_WIDTH // 4
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
gravity = 0.25

# Pipe parameters
pipe_width = 50
pipe_gap = 200
pipe_velocity = 3
pipe_list = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), bird_size)

def draw_pipe(x, y, height):
    pygame.draw.rect(screen, BLUE, (x, y, pipe_width, height))
    pygame.draw.rect(screen, BLUE, (x, y + height + pipe_gap, pipe_width, SCREEN_HEIGHT - y - height - pipe_gap))

def game_over():
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (150, 250))

def main():
    global bird_y, bird_velocity, score

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -8

        screen.fill(BLACK)

        # Update bird position
        bird_y += bird_velocity
        bird_velocity += gravity

        # Draw bird
        draw_bird(bird_x, bird_y)

        # Generate pipes
        if len(pipe_list) == 0 or pipe_list[-1][0] < SCREEN_WIDTH // 2:
            pipe_height = random.randint(50, SCREEN_HEIGHT - pipe_gap - 50)
            pipe_list.append((SCREEN_WIDTH, pipe_height))

        # Move pipes
        for i, pipe in enumerate(pipe_list):
            pipe_list[i] = (pipe[0] - pipe_velocity, pipe[1])

            if pipe[0] + pipe_width < 0:
                pipe_list.pop(i)
                score += 1

            # Check collision
            if bird_x + bird_size > pipe[0] and bird_x < pipe[0] + pipe_width:
                if bird_y < pipe[1] or bird_y + bird_size > pipe[1] + pipe_gap:
                    game_over()

        # Draw pipes
        for pipe in pipe_list:
            draw_pipe(pipe[0], pipe[1], SCREEN_HEIGHT - pipe[1] - pipe_gap)

        # Draw score
        score_text = font.render("Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Check if bird hits ground
        if bird_y > SCREEN_HEIGHT:
            game_over()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()

