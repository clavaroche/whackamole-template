import pygame
import random

def initialize_pygame():
    pygame.init()


def create_screen(width, height, caption):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen


def load_mole_image(path, grid_size):
    mi = pygame.image.load(path)
    return pygame.transform.scale(mi, (grid_size, grid_size))


def main():
    try:
        initialize_pygame()

        WIDTH, HEIGHT = 640, 512
        GRID_SIZE = 32
        column, ROWS = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
        backgroundcolor = "light green"
        lc = "black"

        screen = create_screen(WIDTH, HEIGHT, "Whack-a-Mole")
        clock1 = pygame.time.Clock()
        mi = load_mole_image("mole.png", GRID_SIZE)

        moleposition = (0, 0)
        running = True

        def dg():
            for x in range(0, WIDTH + 1, GRID_SIZE):
                pygame.draw.line(screen, lc, (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT + 1, GRID_SIZE):
                pygame.draw.line(screen, lc, (0, y), (WIDTH, y))

        def molemovement():
            x = random.randrange(0, column) * GRID_SIZE
            y = random.randrange(0, ROWS) * GRID_SIZE
            return x, y

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mi.get_rect(topleft=moleposition).collidepoint(event.pos):
                        moleposition = molemovement()

            screen.fill(backgroundcolor)
            dg()
            screen.blit(mi, mi.get_rect(topleft=moleposition))
            pygame.display.flip()
            clock1.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
