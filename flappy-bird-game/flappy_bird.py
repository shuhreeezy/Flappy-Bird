"""
Flappy Bird Clone
A simple Flappy Bird clone implemented in Python using the Pygame library.
"""
import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game settings
GRAVITY = 0.25
BIRD_JUMP = -6
PIPE_SPEED = -4
PIPE_WIDTH = 50
PIPE_HEIGHT = 320
PIPE_GAP = 200

# Bird class
class Bird(pygame.sprite.Sprite):
    """
    A class to represent the bird in the game.
    """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((34, 24))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(50, SCREEN_HEIGHT // 2))
        self.velocity = 0

    def update(self):
        """
        Update the bird's position based on velocity.
        """
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def jump(self):
        """
        Make the bird jump when the spacebar is pressed.
        """
        self.velocity = BIRD_JUMP

# Pipe class
class Pipe(pygame.sprite.Sprite):
    """
    A class to represent the pipes in the game.
    """
    def __init__(self, flipped, x_position):
        super().__init__()
        self.image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.image.fill(BLACK)
        if flipped:
            self.rect = self.image.get_rect(midbottom=(x_position, SCREEN_HEIGHT // 2 - PIPE_GAP // 2))
        else:
            self.rect = self.image.get_rect(midtop=(x_position, SCREEN_HEIGHT // 2 + PIPE_GAP // 2))

    def update(self):
        """
        Update the pipe's position on the screen.
        """
        self.rect.x += PIPE_SPEED
        if self.rect.right < 0:
            self.kill()

# Game setup
def main():
    """
    Main function to run the game.
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird()
    bird_group = pygame.sprite.Group(bird)
    pipes = pygame.sprite.Group()
    spawn_pipe_event = pygame.USEREVENT
    pygame.time.set_timer(spawn_pipe_event, 1200)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()
            if event.type == spawn_pipe_event:
                pipes.add(Pipe(False, SCREEN_WIDTH))
                pipes.add(Pipe(True, SCREEN_WIDTH))
        bird_group.update()
        pipes.update()
        screen.fill(WHITE)
        bird_group.draw(screen)
        pipes.draw(screen)
        if pygame.sprite.spritecollideany(bird, pipes):
            running = False
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()